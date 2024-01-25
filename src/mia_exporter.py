from assembler import dec_to_hex

def write_to_file(file_name, program) -> None:
    """ Exports the program to a .mia file"""
    pm_mem = """PM:
"""

    for i in range(len(program)):
        pm_mem += dec_to_hex(str(i)).lower() + ": " + program[i] + "\n"

    for i in range(len(program), 256): # Fill the remaining PM to $FF with 0000
        pm_mem += dec_to_hex(str(i)).lower() + ": " + "0000" + "\n"
        
    mia_program = pm_mem + get_cpu_setup()

    with open(file_name, 'w') as f:
        f.writelines(mia_program)

def get_cpu_setup() -> str:
    """ String containing setup for """
    u_mem_str = """
MyM:
00: 00f8000
01: 008a000
02: 0004100
03: 0078080
04: 00fa080
05: 0078000
06: 00b8080
07: 0240000
08: 0984000
09: 0138080
0a: 00b0180
0b: 0190180
0c: 0830000
0d: 0880000
0e: 0730180
0f: 0380000
10: 0a80000
11: 0730180
12: 0380000
13: 0c80000
14: 0730180
15: 0041000
16: 0380000
17: 0000613
18: 1a00a91
19: 0730180
1a: 01da180
1b: 0000214
1c: 0002180
1d: 0000000
1e: 0000000
1f: 0000000
20: 0000000
21: 0000000
22: 0000000
23: 0000000
24: 0000000
25: 0000000
26: 0000000
27: 0000000
28: 0000000
29: 0000000
2a: 0000000
2b: 0000000
2c: 0000000
2d: 0000000
2e: 0000000
2f: 0000000
30: 0000000
31: 0000000
32: 0000000
33: 0000000
34: 0000000
35: 0000000
36: 0000000
37: 0000000
38: 0000000
39: 0000000
3a: 0000000
3b: 0000000
3c: 0000000
3d: 0000000
3e: 0000000
3f: 0000000
40: 0000000
41: 0000000
42: 0000000
43: 0000000
44: 0000000
45: 0000000
46: 0000000
47: 0000000
48: 0000000
49: 0000000
4a: 0000000
4b: 0000000
4c: 0000000
4d: 0000000
4e: 0000000
4f: 0000000
50: 0000000
51: 0000000
52: 0000000
53: 0000000
54: 0000000
55: 0000000
56: 0000000
57: 0000000
58: 0000000
59: 0000000
5a: 0000000
5b: 0000000
5c: 0000000
5d: 0000000
5e: 0000000
5f: 0000000
60: 0000000
61: 0000000
62: 0000000
63: 0000000
64: 0000000
65: 0000000
66: 0000000
67: 0000000
68: 0000000
69: 0000000
6a: 0000000
6b: 0000000
6c: 0000000
6d: 0000000
6e: 0000000
6f: 0000000
70: 0000000
71: 0000000
72: 0000000
73: 0000000
74: 0000000
75: 0000000
76: 0000000
77: 0000000
78: 0000000
79: 0000000
7a: 0000000
7b: 0000000
7c: 0000000
7d: 0000000
7e: 0000000
7f: 0000780

K1:
00: 0a
01: 0b
02: 0c
03: 0f
04: 12
05: 15
06: 1a
07: 1b
08: 00
09: 00
0a: 00
0b: 00
0c: 00
0d: 00
0e: 00
0f: 7f

K2:
00: 03
01: 04
02: 05
03: 07

PC:
00

ASR:
00

AR:
0000

HR:
0000

GR0:
0000

GR1:
0000

GR2:
0000

GR3:
0000

IR:
0000

MyPC:
00

SMyPC:
00

LC:
00

O_flag:

C_flag:

N_flag:

Z_flag:

L_flag:
End_of_dump_file"""
    return u_mem_str