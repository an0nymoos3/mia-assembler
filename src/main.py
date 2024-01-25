#!/usr/bin/env python3
import sys

from file_parser import parse_file
from assembler import assemble, dec_to_hex

def print_program(program) -> None:
    """  Prints final program to terminal. """
    line_nr = 0
    for line in program:
        print(f"line: {dec_to_hex(str(line_nr))} | {line}")
        line_nr += 1


def main() -> None:
    """ main() """
    # Assume user sends .ass file as first arg
    file_name = sys.argv[1]

    if ".ass" not in file_name:
        print("Invalid argument! \n.ass file not detected!")
        exit(1)
    
    text_program = parse_file(file_name)
    hex_program = assemble(text_program)
    print_program(hex_program)


if __name__ == "__main__":
    main()