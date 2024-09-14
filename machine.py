# Contains functions for Simpletron other than instructions

import main
import re
import instructions

def core_dump(start, end): # Param are start and end of the range of pages to print

    global mem
    global acc
    global ic
    global ir
    global idx

    oc = int(main.ir / 10000) # Set the operation code to the left 2 digits of the instruction register
    op = int(str(main.ir).zfill(6)[2:6]) # set the operand to the right 4 digits of the instruction register

    # Dump registers and page data for each page within the range
    for page_num in range(start, end):
        
        print(f"PAGE # {page_num:02d}") # Print page number

        # Dump registers
        print("\nREGISTERS:\n")
        print(f"Accumulator        {main.acc:06d}")
        print(f"InstructionCounter {main.ic:06d}")
        print(f"IndexRegister      {main.idx:06d}")
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
                print(f" {main.mem[page_num][line * i]:06d}",end="") # Print the word at the current page and current line and index
            print()
        print("\n")
    return 0

def manual_data_entry():

    global mem

    print("*** Please enter your program one instruction (or data word) at a time                 ***")
    print("*** I will type the location number and a question mark (?).                           ***")
    print("*** You then type the word for that location. Type the word GO to execute your program ***")

    entry = ""
    for page in range(len(main.mem)):
        for word in range(len(main.mem[0])):

            # Block takes input and checks input validity
            valid = False
            while not valid:
                entry = input(f"{page:02d}{word:02d} ? ") # Get input from user

                # Check exit
                if entry.upper() == "GO":
                    return 0
                
                # Check valid input - must be a 6 digit number or fewer
                if not entry.isdigit():
                    print("Input must be a number or GO")
                    continue
                entry = int(entry)
                if entry > 999999 or entry < -999999:
                    print("Entry must be 6 digits or fewer")
                    continue

                valid = True
                
            # Input is valid, enter to memory
            main.mem[page][word] = entry          
    return 0 # Reached end of memory

# !!! File must have 4 digit line numbers at the start of each line !!!
# ; are for comments
def file_data_entry(file_name):
    
    global mem

    try:
        with open(file_name, 'r') as file:
            # Process SML line by line
            for line in file:
                entry = line.replace(" ", "") # Remove spaces from data entry for easier processing

                # Check if entry matches the correct line format of SML
                pattern = "^\d{4}\d{6}(;(.+)?)?$"
                match = re.match(pattern, entry)
                if not match:
                    print("File is not in proper SML format")
                    return 1 # 1 = something bad, kill program

                # Enter data
                page = entry[0:2] # First 2 digits are page
                word = entry[2:4] # digits 3 and 4 are word
                entry = entry[4:10] # Actual data is the 6 digits after
                main.mem[page][word] = entry

    except FileNotFoundError:
        print("The file does not exist")
        return 1

    return 0 

def execute_ir():
    global ir
    
    op_code = int(str(main.ir)[0:2])
    operand = int(str(main.ir)[2:6])

    instr = [0] * 46 # List of functions all the instructions - Size of list = highest op_code + 1
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

    exit_code = instr[op_code](operand)
    return exit_code