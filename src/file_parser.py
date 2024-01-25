"""
    This file parses the text content of the .ass file.
    It then returns the instructions with all the extra
    symbols and blank lines stripped.
"""

def parse_file(ass_file) -> (list, list):
    lines = []
    vs_code_nrs = []
    line_nr = 0
    with open(ass_file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            
            # Split each instruction
            line = line.split(",")

            if len(line) == 1:
                if line[0] != '' and line[0] != ' ':
                    lines.append(line)
                    vs_code_nrs.append(line_nr + 1)

            if len(line) > 1:
                lines.append(line)
                vs_code_nrs.append(line_nr + 1)

            line_nr += 1

    # Remove all spaces
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j].strip()

    return (lines, vs_code_nrs)
