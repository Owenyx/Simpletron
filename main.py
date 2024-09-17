import sys
import machine

def main():

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
            return 0

    # Begin executing the users program
    while True:
        page = int(str(machine.ic).zfill(4)[0:2])
        word = int(str(machine.ic).zfill(4)[2:4])
        machine.ir = machine.mem[page][word] # load the instruction from the address of the ic into the ir
        machine.ic += 1
        exit_code = machine.execute_ir() # exit code is 1 to quit, 0 to continue

        if exit_code == 1:
            break
    return 0
        
if __name__ == "__main__":
    main()