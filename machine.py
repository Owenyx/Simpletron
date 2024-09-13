# Contains functions for Simpletron other than instructions

def core_dump(mem):

    oc = irg / 10000 # Set the operation code to the left 2 digits of the instruction register
    op = int(str(irg)[2:6]) # set the operand to the right 4 digits of the instruction register

    for page in mem:

        printf("PAGE # %2d", page)
        print("\nREGISTERS:\n")
        printf("Accumulator        %6d", acc)
        printf("InstructionCounter   %4d", itc)
        printf("IndexRegister        %4d", idx)
        printf("OperationCode          %2d", oc)
        printf("Operand              %4d", op)
        print("\nMEMORY\n   ")
        for i in range(10):
            printf("%6d ", i)

        for word in page:
            print(word)