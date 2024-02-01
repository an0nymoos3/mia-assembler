#!/usr/bin/env python3
import sys

from file_parser import parse_file
from assembler import assemble, dec_to_hex
from mia_exporter import write_to_file


def export_program(program, source_code, file_name, debug, vs_code_lines) -> None:
    """Prints final program to terminal."""
    file_name = file_name.replace(".ass", ".mia")
    file_name = file_name.replace(".asm", ".mia")

    if debug:
        for i in range(len(program)):
            print(
                f"PM: {dec_to_hex(str(i))} (line: {vs_code_lines[i]}) | {program[i]} < {source_code[i]}"
            )

    print(f"Exporting to: {file_name}...")
    write_to_file(file_name, program)
    print("Done!")


def main() -> None:
    """main()"""
    # Assume user sends .ass file as first arg
    file_name = sys.argv[1]
    debug = False

    if len(sys.argv) > 2:
        if sys.argv[2] == "--debug":
            debug = True

    if (".ass" and ".asm") not in file_name:
        print("Invalid argument! \n.ass file not detected!")
        exit(1)

    print(f"Assembling {file_name}...")
    code, vs_code_lines = parse_file(file_name)
    hex_program = assemble(code)

    export_program(hex_program, code, file_name, debug, vs_code_lines)


if __name__ == "__main__":
    main()
