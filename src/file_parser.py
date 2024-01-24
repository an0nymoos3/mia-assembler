"""
    This file parses the text content of the .ass file.
    It then returns the instructions with all the extra
    symbols and blank lines stripped.
"""

def parse_file(ass_file) -> []:
    lines = []
    with open(ass_file) as f:
        for line in f.readlines():
            line = line.strip()
            line = line.split(", ")
            lines.append(line)

    return lines