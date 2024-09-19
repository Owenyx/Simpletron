# Contains functions for Simpletron other than instructions

import re
import instructions

# create memory, 100 pages of 100 words each, 10,000 words total
pages, words = 100, 100

# Actual memory is not divided internally
mem = [0] * (pages * words)

# Create registers
acc = 0 # accumulator
ic = 0 # instruction counter
ir = 0 # instruction register
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

    # since instructions may have no operand, it could be less than 6 digits, 
    # so for instruction execution we fill the op code and operand with zeroes on the right
    if ir < 0: # handle extra - sign at start
        padded = int('-' + str(ir)[1:3].zfill(2) + str(ir)[3:7].zfill(4))
    else:
        padded = int(str(ir)[0:2].zfill(2) + str(ir)[2:6].zfill(4))

    op_code = abs(padded//10000) # op code is first 2 digits
    operand = padded%10000 # operand is the other 4

    # Dump registers and page data for each page within the range
    for page_num in range(start, end+1):
        
        print(f"PAGE # {page_num:02d}") # Print page number

        # Dump registers
        print("\nREGISTERS:\n")
        print(f"Accumulator        {acc:0{7 if acc < 0 else 6}d}") # format is to sure length of output is 6 even when number is negative
        print(f"InstructionCounter {ic:0{7 if acc < 0 else 6}d}")
        print(f"IndexRegister      {idx:0{7 if acc < 0 else 6}d}")
        print(f"OperationCode          {op_code:0{3 if acc < 0 else 2}d}")
        print(f"Operand              {operand:0{5 if acc < 0 else 4}d}")

        # Dump memory one page at a time
        print("\nMEMORY",end="\n\n   ")

        # print ones index on top for page
        for i in range(10):
            print(f"{i:6d} ",end="") 
        print()

        # Dump the words of the page
        for line in range(10):
            print(f"{(line*10):02d}",end="") # Print the tens index
            # Dump the words on this line
            for i in range(10):
                # Print the word at the current page and current line and index
                print(f" {mem[page_num*100 + 10*line + i]:0{7 if acc < 0 else 6}d}",end="") 
            print()
        print("\n")
    return 0

def manual_data_entry():

    global mem
    global pages
    global words

    print("*** Please enter your program one instruction (or data word) at a time                 ***")
    print("*** I will type the location number and a question mark (?).                           ***")
    print("*** You then type the word for that location. Type the word GO to execute your program ***")

    for page in range(pages): # for each page in memory
        for word in range(words): # for each word in that page

            # loop takes input and checks input validity
            valid = False
            while not valid:
                entry = input(f"{page:02d}{word:02d} ? ") # Get input from user

                # Check exit
                if entry.upper() == "GO":
                    return 0

                # ensure input is valid
                if not re.fullmatch(r"^-?\d(\d?){5}$", entry):
                    print("Entry must be a 6 or fewer digit integer or \"GO\"")
                    continue

                valid = True
                
            # Input is valid, enter to memory
            mem[page * 100 + word] = int(entry)          
    return 0 # Reached end of memory

# !!! File must have 4 digit line numbers at the start of each line !!!
# ; are for comments
def file_data_entry(file_name):

    global mem

    star_address = "0000"
    # Star is used for incremental addresses, starting at 0000 or from the previous specified address

    try:
        with open(file_name, 'r') as file:
            # Process SML line by line
            for line in file:
                entry = ''.join(line.split()) # Remove all whitespace from data entry for easier processing

                if len(entry) == 0 or entry[0] == ";": continue # If line is empty or just a comment, move on
                # For some reason the length of an empty line was coming out as 1

                # Star check:
                if entry[0] == "*":
                    entry = star_address + entry[1:] # replaces the star with the star address 

                # Check if entry matches the correct line format of SML
                match = re.match(r"^\d{4}-?\d(\d?){5}(;(.+)?)?$", entry)
                # Accepted format:
                # Must have 4 digits (memory location) followed by
                # a 1-6 digit value which can be negative
                # then optionally followed by a comment denoted by a ;
                # Whitespace does not matter
                if not match:
                    print("File is not in proper SML format")
                    return 1 # 1 = something bad, kill program

                # Split data
                entry = entry.split(';')[0] # Remove the comment if there is one
                address = int(entry[0:4]) # First 4 digits are address
                entry = entry[4:] # Actual data is the rest
                mem[address] = int(entry)
                star_address = str(address + 1).zfill(4)

    except FileNotFoundError:
        print("The file does not exist")
        return 1

    return 0 

def execute_ir():

    global mem
    global ir

    # since instructions may have no operand, it could be less than 6 digits, 
    # so for instruction execution we fill the op code and operand with zeroes on the right
    if ir < 0: # handle extra - sign at start
        padded = int('-' + str(ir)[1:3].zfill(2) + str(ir)[3:7].zfill(4))
    else:
        padded = int(str(ir)[0:2].zfill(2) + str(ir)[2:6].zfill(4))

    op_code = abs(padded//10000) # op code is first 2 digits
    operand = padded%10000

    global instr

    if isinstance(instr[op_code], int): # if instr[op_code] doesn't map to an instruction function
        print("Illegal instruction: Terminating")
        return 2 # Invalid operation code

    exit_code = instr[op_code](operand)
    # if a string is returned, then an error has occured
    if isinstance(exit_code, str):
        print(exit_code)
        return 2 # signifies error in order to terminate
    return exit_code