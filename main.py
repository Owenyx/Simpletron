import sys
import machine

# create memory, 100 pages of 100 words each, 10,000 words total
pages, words = 100, 100

mem = [[0] * words for _ in range(pages)]

# Create registers
acc = 0 # accumulator
ic = 0 # instruction counter
ir = 0 # instruction register
idx = 0 # index register

def main():

    global mem
    global acc
    global ic
    global ir
    global idx

    # Introduction
    print("*** Welcome to Simpletron V2! ***")
    # Input decision
    ans = input("*** Do you have a file that contains your SML program (Y/N) ? ").upper()
    while ans != 'Y' and ans != 'N':
        print("Invalid input.")
        ans = input("*** Do you have a file that contains your SML program (Y/N) ? ").upper()

    # Program and data entry
    if ans == 'N':
        machine.manual_data_entry()
    else:
        file_name = input("*** Enter the name of the file: ")
        exit_code = machine.file_data_entry(file_name)
        if exit_code == 1:
            machine.end_execution()

    # Begin executing the users program
    while True:
        ir = mem[ic] # load the instruction from the address of the ic into the ir
        ic += 1
        exit_code = machine.execute_ir() # exit code is 1 to quit, 0 to continue

        if exit_code == 1:
            break
    return 0
        
if __name__ == "__main__":
    main()