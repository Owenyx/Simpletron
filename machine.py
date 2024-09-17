# Contains functions for Simpletron other than instructions

import re
import instructions

# create memory, 100 pages of 100 words each, 10,000 words total
pages, words = 100, 100

mem = [["0"] * words for _ in range(pages)] 
# Memory has to be strings for annoying reasons
# The strings will all contain integers or 2 digits followed by an integer

# Create registers
acc = 0 # accumulator
ic = 0 # instruction counter
ir = '0' # instruction register, has to be a string as it will contain instructions which can have 2 digits followd by a negative
idx = 0 # index register

# List of functions of all the instructions - Size of list = highest op_code + 1
# used in execute_ir()
instr = [0] * 46 
instr[10] = instructions.READ
instr[11] = instructions.WRITE
instr[20] = instructions.LOAD
instr[21] = instructions.LOADIM
instr[22] = instructions.LOADX
instr[23] = instructions.LOADIDX
instr[25] = instructions.STORE
instr[26] = instructions.STOREIDX
instr[30] = instructions.ADD
instr[31] = instructions.ADDX
instr[32] = instructions.SUBTRACT
instr[33] = instructions.SUBTRACTX
instr[34] = instructions.DIVIDE
instr[35] = instructions.DIVIDEX
instr[36] = instructions.MULTIPLY
instr[37] = instructions.MULTIPLYX
instr[38] = instructions.INC
instr[39] = instructions.DEC
instr[40] = instructions.BRANCH
instr[41] = instructions.BRANCHNEG
instr[42] = instructions.BRANCHZERO
instr[43] = instructions.SWAP
instr[45] = instructions.HALT

def dump_core(start, end): # Param are start and end of the range of pages to print

    print("\n*** Program halted, dumping memory now... ***\n")

    global mem
    global acc
    global ic
    global ir
    global idx

    oc = int(ir[0:2]) # Set the operation code to the left 2 digits of the instruction register
    op = int(ir.zfill(6)[2:6]) # set the operand to the right 4 digits of the instruction register

    # Dump registers and page data for each page within the range
    for page_num in range(start, end+1):
        
        print(f"PAGE # {page_num:02d}") # Print page number

        # Dump registers
        print("\nREGISTERS:\n")
        print(f"Accumulator        {acc:06d}")
        print(f"InstructionCounter {ic:06d}")
        print(f"IndexRegister      {idx:06d}")
        print(f"OperationCode          {oc:02d}")
        print(f"Operand              {op:04d}")

        # Dump memory one page at a time
        print("\nMEMORY",end="\n\n   ")
        for i in range(10):
            print(f"{i:6d} ",end="") # print ones index on top for page
        print()

        # Dump the words of the page
        for line in range(10):
            print(f"{(line*10):02d}",end="") # Print the tens index
            # Dump the words on this line
            for i in range(10):
                print(f" {mem[page_num][10*line + i].zfill(6)}",end="") # Print the word at the current page and current line and index
            print()
        print("\n")
    return 0

def manual_data_entry():

    global mem

    print("*** Please enter your program one instruction (or data word) at a time                 ***")
    print("*** I will type the location number and a question mark (?).                           ***")
    print("*** You then type the word for that location. Type the word GO to execute your program ***")

    for page in range(len(mem)):
        for word in range(len(mem[0])):

            # Block takes input and checks input validity
            valid = False
            while not valid:
                entry = input(f"{page:02d}{word:02d} ? ") # Get input from user

                # Check exit
                if entry.upper() == "GO":
                    return 0
                
                # If entry is an instruction with a negative operand, it's valid
                if re.match(r"^\d\d-\d(\d?){3}$", entry): break
                
                # Check valid input - must be a 6 digit number or fewer
                if not re.match(r"^-?\d+$", entry): # If entry isn't an integer value, try again
                    print("Input must be a number or \"GO\"")
                    continue
                
                # ensures input is 6 or fewer digits
                if not re.fullmatch(r"^-?\d(\d?){5}$", entry):
                    print("Entry must be 6 digits or fewer")
                    continue

                valid = True
                
            # Input is valid, enter to memory
            mem[page][word] = entry          
    return 0 # Reached end of memory

# !!! File must have 4 digit line numbers at the start of each line !!!
# ; are for comments
def file_data_entry(file_name):

    global mem

    try:
        with open(file_name, 'r') as file:
            # Process SML line by line
            for line in file:
                entry = ''.join(line.split()) # Remove all whitespace from data entry for easier processing

                if len(line) == 0 or len(line) == 1 or line[0] == ";": continue # If line is empty or just a comment, move on
                # For some reason the length of an empty line was coming out as 1

                # Check if entry matches the correct line format of SML
                match = re.match(r"^\d{4}((-?\d(\d?){5})|(\d\d-\d(\d?){3}))(;(.+)?)?$", entry) # have fun with that regex
                # Accepted format:
                # Must have 4 digits (memory location) followed by either:
                # a 1-6 digit value which can be negative
                # or a 2 digit number (instruction code) followed by a 1-4 digit number that can be negative
                # then optionally followed by a comment denoted by a ;
                # Whitespace does not matter
                if not match:
                    print("File is not in proper SML format")
                    return 1 # 1 = something bad, kill program

                # Split data
                entry = entry.split(';')[0] # Remove the comment if there is one
                page = entry[0:2] # First 2 digits are page
                word = entry[2:4] # digits 3 and 4 are word
                entry = entry[4:] # Actual data is the rest
                mem[int(page)][int(word)] = entry

    except FileNotFoundError:
        print("The file does not exist")
        return 1

    return 0 

def execute_ir():

    global mem
    
    op_code = int(ir[0:2]) # op code is first 2 digits
    # if operand is negative, then the 3rd character of ir will be the - sign and the other 4 will be the operand value
    if len(ir) > 2 and ir[2] == '-': operand = '-' + ir[3:7].zfill(4)
    # otherwise, the 4 digits after the op code will be the operand
    else: operand = ir[2:6].zfill(4) # operand is digits 3-6

    global instr

    if isinstance(instr[op_code], int):
        print("Illegal instruction: Terminating")
        return 1 # Invalid operation code

    exit_code = instr[op_code](operand)
    # if a string is returned, then an error has occured
    if isinstance(exit_code, str):
        print(exit_code)
        return 1 # signifies error in order to terminate
    return exit_code