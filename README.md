# Simpletron
Lab 1

The program will prompt the user to enter the program manually or enter the file name.
The program then walks the user through their choice in order to enter a program.

Format of line in files:
Four digit non-negative address, then 1-6 digit integer word, then an optional comment denoted by a ;

A word that the Simpletron tries to execute is an instruction
A word that the Simpletron uses in an instruction is data
The first 2 digits of an instruction are the operation code, the other 4 are the operand
If an instruction is negative, then the operand will be read as a negative number
If data is negative, it is simply used as a negative number
Instructions should start at line 0000

Optionally, you can forgo the four digit address and replace it with a * to use an incremental address
A * will add one to the previously used address value and use it as the address for the following word
Starting with a * will set the first line to address 0000

Error checking:
The simpletron will not accept files with incorrect line formats
Runtime errors, all of which terminate the program and dump the first 10 pages of memory:
Accumulator overflow
Index register overflow
Divide by zero
Address out of bounds (index error)
Illegal instruction code

Each sml program will have its own small README in the form of comments at the start