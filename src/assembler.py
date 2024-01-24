"""
    This file handles the conversion of lines of text to lines of hexadecimal machine code.

    Each line of the program is expected to contain 4 words or args. Therefore when 1 is missing
    the assembler needs to fill in the gaps.
    General structure: instruction, register, mode, adr

    also valid example: instruction, adr

    It will also handle the logic of special features, such as filling in blanks on parameters,
    or converting names to jumps.
"""

def assemble(program) -> []:
    """ Converts text representation of .ass program to hex representation """
    bin_program = text_to_bin(program)

    hex_program = []
    for line in bin_program:
        hex_program.append(bin_to_hex(line))

    return hex_program


def text_to_bin(program) -> []:
    """ Converts text representation to binary """
    bin_program = []

    # Go through each line
    for line in program:
        bin_line = "" # Start with an empty string

        bin_line += get_instruction(line)
        bin_line += get_register(line)
        bin_line += get_mode(line)
        bin_line += get_adr(line)

        if len(bin_line) != 16:
            print(f"Error assembling program! \nLine is not 16 bits long! \nLine: {line} \nResult: {bin_line}")
            exit(1)

        bin_program.append(bin_line)

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
        "HALT": "1111",
    }

    # Check if there's no instruction
    if line[0] not in ops:
        print(f"Error assembling program! \nNo instruction detected! \nLine: {line}")
        exit(1)

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
    
    # Logical Shift Right edge case, doesn't use ADR, instead passes a constant Y
    if line[0] == "LSR":
        return dec_to_bin(line[-1])

    # Else error
    print(f"Error assembling program! \nNo ADR detected or in invalid position! \nLine: {line}")
    exit(1)


def hex_to_bin(hex) -> str:
    """ Converts a hex number (likely address) to binary representation """
    hex = hex.strip("$")
    hex = hex.lower()
    return "{0:08b}".format(int(hex, 16)) 
    

def bin_to_hex(bin) -> str:
    """ Converts a bin number (program instruciton) to hexadecimal representation """
    return "{0:04X}".format(int(bin, 2))

def dec_to_bin(Y) -> str:
    """ Covers LSR instruction which uses Y instead of ADR """
    return "{0:08b}".format(int(Y, 10))