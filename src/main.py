#!/usr/bin/env python3
import sys

from file_parser import parse_file
from assembler import assemble, dec_to_hex
from mia_exporter import write_to_file

def export_program(program, source_code, file_name, debug) -> None:
    """  Prints final program to terminal. """
    file_name = file_name.replace(".ass", ".mia")

    if debug:
        line_nr = 0

        for i in range(len(program)):
            print(f"line: {dec_to_hex(str(line_nr))} | {source_code[i]} => <{program[i]}>")
            line_nr += 1

    print(f"Exporting to: {file_name}...")
    write_to_file(file_name, program)
    print("Done!")


def main() -> None:
    """ main() """
    # Assume user sends .ass file as first arg
    file_name = sys.argv[1]
    debug = False

    if len(sys.argv) > 2:
        if sys.argv[2] == "--debug":
            debug = True

    if ".ass" not in file_name:
        print("Invalid argument! \n.ass file not detected!")
        exit(1)
    
    print(f"Compiling {file_name}...")
    text_program = parse_file(file_name)
    hex_program = assemble(text_program)
    export_program(hex_program, text_program, file_name, debug)


if __name__ == "__main__":
    main()