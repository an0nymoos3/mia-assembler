"""
    This file handles the conversion of lines of text to lines of hexadecimal machine code.

    Each line of the program is expected to contain 4 words or args. Therefore when 1 is missing
    the assembler needs to fill in the gaps.
    General structure: instruction, register, mode, adr

    also valid example: instruction, adr

    It will also handle the logic of special features, such as filling in blanks on parameters,
    or converting names to jumps.
"""

def assemble(program) -> list:
    """ Converts text representation of .ass program to hex representation """
    
    
    remove_comments(program) # Need to do this for line jump calculations to work

    #for line in program:
    #    print(line)

    calc_branch_jmps(program)
    remove_branch_names(program)

    bin_program = text_to_bin(program)

    hex_program = []
    for line in bin_program:
        hex_program.append(bin_to_hex(line))

    return hex_program


def text_to_bin(program) -> []:
    """ Converts text representation to binary """
    bin_program = []
    line_num = 0

    # Go through each line
    for line in program:
        try:
            bin_line = "" # Start with an empty string

            # Check if line is value, used for imidiate modes
            if "@" in line[0]:
                bin_line = imi_hex_to_bin(line[0])
            else:
                bin_line += get_instruction(line)
                bin_line += get_register(line)
                bin_line += get_mode(line)
                bin_line += get_adr(line)

            if len(bin_line) != 16:
                print(f"Error assembling program! \nLine is not 16 bits long! \nLine: {line_num} | {line} \nResult: {bin_line}")
                exit(1)

            bin_program.append(bin_line)

        except Exception as e:
            print(f"Error compiling line: {line_num} | {line} \n{e}")
            exit(1)

        line_num += 1

    return bin_program


def get_instruction(line) -> str:
    """ Returns the binary encoding of the ass instruction. """
    ops = {
        "LOAD": "0000",
        "STORE": "0001",
        "ADD": "0010",
        "SUB": "0011",
        "AND": "0100",
        "LSR": "0101",
        "BRA": "0110",
        "BNE": "0111",
        "BEQ": "1000",
        "BGE": "1001",
        "CMP": "1010",
        "RAR": "1011",
        "HALT": "1111",
    }

    # Check if there's no instruction
    if line[0] not in ops:
        print(f"Error assembling program! \nNo instruction detected!")

    # Else return instruction in binary
    return ops[line[0]]


def get_register(line) -> str:
    """ Returns the binary value of the register to use. """
    regs = {
        "GR0": "00",
        "GR1": "01",
        "GR2": "10",
        "GR3": "11",
    }

    # Halt edge case
    if len(line) == 1:
        return "00"

    # No register detected
    if line[1] not in regs:
        return "00"

    return regs[line[1]]


def get_mode(line) -> str:
    """ Returns the mode from line of ass code."""
    modes = ["00", "01", "10", "11"]

    for word in line:
        if word in modes:
            return word

    return "00"


def get_adr(line) -> str:
    """ Returns the ADR part of the line of code. """
    
    #Since ADR is always part of a line of ass code we can assume 2 scenarios.
    # Eitherits second, or 4th
    for word in line:
        if "$" in word:
            return hex_to_bin(word)
    
    # Check if halt instruction
    if line[0] == "HALT":
        return "00000000"
    
    # Check if halt instruction
    if line[0] == "RAR":
        return "00000000"

    # Logical Shift Right edge case, doesn't use ADR, instead passes a constant Y
    if line[0] == "LSR":
        return dec_to_bin(line[-1])

    # Else error
    print(f"Error assembling program! \nNo ADR detected or in invalid position!")


def remove_comments(program) -> list:
    """ Program of all its comments. Leaving only lines of code. """
    empty_lines = []

    # Strip comments and look for empty lines afterwards
    for i in range(len(program)):
        line = program[i]

        for j in range(len(line)):
            if ";" in line[j]:
                line[j] = remove_content_from_word(line[j], ";")
        
        if line[0] == '' or line[0] == ' ':
            empty_lines.append(i)

    # Remove any empty lines
    for line_nr in empty_lines:
        program.remove(program[line_nr])

    return program


def remove_content_from_word(word, symbol) -> str:
    """ Due to the nature of the assembler, comments on same line as 
    code will be part of the final argument or word or the line.
    Therefore we check for the # and remove anything after it."""
    for i in range(len(word)):
        if word[i] == symbol:
            return word[:i]
            

def remove_branch_names(program) -> list:
    """ Removes #BRANCH_NAME from lines of code. """
    empty_lines = []

    # Strip comments and look for empty lines afterwards
    for i in range(len(program)):
        line = program[i]

        for j in range(len(line)):
            if "#" in line[j]:
                line[j] = remove_content_from_word(line[j], "#")
        
        if line[0] == '' or line[0] == ' ':
            empty_lines.append(i)

    # Remove any empty lines
    for line_nr in empty_lines:
        program.remove(program[line_nr])

    return program


def hex_to_bin(hex) -> str:
    """ Converts a hex number (likely address) to binary representation """
    hex = hex.strip("$")
    hex = hex.strip(" $")
    hex = hex.lower()
    return "{0:08b}".format(int(hex, 16)) 
    

def bin_to_hex(bin) -> str:
    """ Converts a bin number (program instruciton) to hexadecimal representation """
    return "{0:04X}".format(int(bin, 2))


def dec_to_bin(Y) -> str:
    """ Covers LSR instruction which uses Y instead of ADR """
    return "{0:08b}".format(int(Y, 10))


def dec_to_hex(dec) -> str:
    """ Returns decimal number in hexadecimal. """
    return "{0:02X}".format(int(dec, 10))


def imi_hex_to_bin(hex) -> str:
    """ Takes the @value and converts it to binary to be ready for PM """
    hex = hex.strip("@")
    hex = hex.lower()
    return "{0:016b}".format(int(hex, 16))


def calc_branch_jmps(program) -> list:
    """ Replaces all jumps to #NAME with the proper relative jump numbers """
    for i in range(len(program)):
        line = program[i]

        if line[0] == "BNE" or line[0] == "BRA" or line[0] == "BEQ" or line[0] == "BGE":
            if "#" in line[1]:
                branch_name = line[1].strip()
                branch_line_num = find_branch(program, branch_name) - 2

                if i < branch_line_num:
                    rel_jump = branch_line_num - i
                else:
                    rel_jump = 255 - (i - branch_line_num)

                # Replace name with an ADR looking hex number, 
                # so that it gets parsed to binary later in assember
                line[1] = "$" + dec_to_hex(str(rel_jump))

    return program


def find_branch(program, branch_name) -> int:
    """ This function assumes there will be a brach with the name specified. """
    for i in range(len(program)):
        if "BNE" not in program[i] and "BGE" not in program[i] and "BEQ" not in program[i] and "BRA" not in program[i]:
            for word in program[i]:
                if branch_name in word:
                    return i

    print(f"No branch found with name '{branch_name}'")