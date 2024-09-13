import sys

# create memory, 100 pages of 100 words each, 10,000 words total
pages, words = 100, 100

mem = [[0] * words for _ in range(pages)]

# Create registers
acc = 0 # accumulator
ic = 0 # instruction counter
ir = 0 # instruction register
idx = 0 # index register

def main():

    # Introduction
    print("*** Welcome to Simpletron V2! ***")
    print("*** Enter 1 if you would like to enter your program one instruction( or data word ) at a time ***")
    print("*** Enter 2 if you would rather enter a file with the instructions and data ***")

    # Input decision
    ans = int(input("*** Your answer: "))
    while ans != 1 and ans != 2:
        print("Invalid input.")
        ans = int(input("*** Your answer: "))

    # Program and data entry
    if ans == 1:
        print("*** I will type the location number and a question mark (?). ***")
        print("*** You then type the word for that location. Type the word GO to execute your program ***")
        manual_data_entry()
    else:
        file_name = input("*** Enter the name of the file: ")
        file_data_entry(file_name)

    # Begin executing the users program
    while True:
        load_irg() # loads the instruction from the address of the itc into the irg
        itc += 1
        exit_code = execute_irg() # exit code is 1 to quit, 0 to continue

        if exit_code:
            end_execution()
        
if __name__ == "__main__":
    main()