# Contains functions for Simpletron other than instructions

import main

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
        print(f"InstructionCounter   {main.ic:04d}")
        print(f"IndexRegister        {main.idx:04d}")
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
    return

def manual_data_entry():
    