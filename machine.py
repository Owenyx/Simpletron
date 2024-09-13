# Contains functions for Simpletron other than instructions

import main

def core_dump(start, end): # Param are start and end of the range of pages to print

    global mem
    global acc
    global ic
    global ir
    global idx

    oc = ir / 10000 # Set the operation code to the left 2 digits of the instruction register
    op = int(str(ir)[2:6]) # set the operand to the right 4 digits of the instruction register

    for page in mem:
        
        print(f"PAGE # {page:2d}") # Print page number

        # Dump registers
        print("\nREGISTERS:\n")
        print(f"Accumulator        {acc:6d}")
        print(f"InstructionCounter   {ic:4d}")
        print(f"IndexRegister        {idx:4d}")
        print(f"OperationCode          {oc:2d}")
        print(f"Operand              {op:4d}")

        # Dump memory one page at a time
        print("\nMEMORY\n   ")
        for i in range(10):
            print(f"{i:6d} ") # print ones index on top for page

        # Dump the words of the page
        for line in range(10):
            print(f"{(line*10):2d}") # Print the tens index
            # Dump the words on this line
            for i in range(10):
                print(f" {page[line * i]:6d}")