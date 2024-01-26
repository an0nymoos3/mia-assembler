# MIA Assembler

## About this
MIA Assembler is an program I wrote to convert an assembly like program to hexadecimal 
representation to avoid doing it by hand. It is specifically designed for 
our instruction set.  
This is a very basic program, just usnig string manipulations to accomplish the assembling.  

## Usage
Currently the assembler doesn't check if the program is valid, other than ensuring that the 
binary encoding of each .ass line is exactly 16 bits long. Therefore each .ass
program has to be validated by the programmer to guarantee a successful assemble.

```
./src/main.py <your_program>.ass
```
The program exports the result into a .mia file in the working directory. If you want to see how it 
generated your assembly code to machine code you can use the `--debug` flag.

```
./src/main.py <your_program>.ass --debug
```

## Features
### Instructions

| Instruction |     Args    |           Meaning           |
| ----------- | ----------- | --------------------------- |
| LOAD        | GRx, M, ADR | GRx := PM(A)                |
| STORE       | GRx, M, ADR | PM(A) := GRx                |
| ADD         | GRx, M, ADR | GRx :=GRx+PM(A)             |
| SUB         | GRx, M, ADR | GRx :=GRx-PM(A)             |
| AND         | GRx, M, ADR | GRx :=GRx & PM(A)           |
| LSR         | GRx, M, Y   | Logical shift right Y steps |
| BRA         | ADR         | PC :=PC+1+ADR               |
| BNE         | ADR         | PC:= PC+1+ADR, if Z=0       |
| BGE         | ADR         | PC:= PC+1+ADR, if N=1       |
| BEQ         | ADR         | PC:= PC+1+ADR, if Z=1       |
| CMP         | GRx, M, ADR | GRx-PM(A)                   |
| HALT        |             | Exits program               |

### Other features
- Omitting M. If M is not detected by assembler it will assume the mode is 00.
- Comments! Write comments using ;. Either on the same line as code or seperate lines!
```
...
; This is a line of comments
...

... ; This is a comment on the same line as code.
```

- Absolute jumps with branch names. Example:
```
BRA, #JUMP_HERE
...
LOAD, GRx, $AB #JUMP_HERE
```
Is the same as: 

```
BRA, $02
...
LOAD, GRx, $AB

```
