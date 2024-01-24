#!/usr/bin/env python3
import sys

from file_parser import parse_file
from assembler import assemble

def print_program(program) -> None:
    """  Prints final program to terminal. """
    line_nr = 0
    for line in program:
        print(f"line: {line_nr} | {line}")
        line_nr += 1


def main() -> None:
    """ main() """
    # Assume user sends .ass file as first arg
    file = sys.argv[1]
    
    text_program = parse_file(file)
    hex_program = assemble(text_program)
    print_program(hex_program)


if __name__ == "__main__":
    main()