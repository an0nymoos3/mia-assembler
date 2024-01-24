def assemble(program):
    """ Converts text representation of .ass program to hex representation """
    bin_program = text_to_bin(program)

    hex_program = []
    for line in bin_program:
        hex_program.append(bin_to_hex(line))

    return hex_program

def text_to_bin(program):
    """ Converts text representation to binary """
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

    regs = {
        "GR0": "00",
        "GR1": "01",
        "GR2": "10",
        "GR3": "11",
    }

    bin_program = []

    # Go through each line
    for line in program:
        bin_line = ops[line[0]]

        # Go through each word in the line
        for i in range(1, len(line)):
            # Check if current wordeter is an address
            if "$" in line[i]:
                bin_line += hex_to_bin(line[i])

            # Check for register
            elif "GR" in line[i]:
                bin_line += regs[line[i]]

            # Else it's a value
            else:
                bin_line += line[i]

        if len(bin_line) != 16:
            print(f"Error assembling program! \nLine is not 16 bits long! \nLine: {line} \nResult: {bin_line}")
            exit(1)

        bin_program.append(bin_line)

    return bin_program

def hex_to_bin(hex: str) -> str:
    """ Converts a hex number (likely address) to binary representation """
    hex = hex.strip("$")
    hex = hex.lower()
    return "{0:08b}".format(int(hex, 16)) 
    

def bin_to_hex(bin) -> str:
    """ Converts a bin number (program instruciton) to hexadecimal representation """
    return "{0:04X}".format(int(bin, 2))