# My Ass

## About this
My Ass is an program I wrote to convert an assembly like program to hexadecimal 
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
| BNE         | ADR         | PC:= PC+1                   |
| HALT        |             | Exits program               |

### Other features
- Omitting M. If M is not detected by assembler it will assume the mode is 00.


## Planned features
- Branch/jump to name rather than relative instructions.
Example: 
```
BNE #BRANCH
...

#BRANCH
...
```

- Python/ shell style comments using # to declare a comment.