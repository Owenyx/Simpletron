
import re
import machine

def READ(op):
    page, word = address_split(op)
    inp = input("? ")
    
    # check input validity
    while not re.match(r"^-?\d(\d?){5}$", inp): # if input is not as 6 or fewer digit integer, terminate with an error
        print("Invalid entry, try again")
        inp = input(f"{op} ? ")

    machine.mem[page][word] = inp
    return 0

def WRITE(op):
    page, word = address_split(op)
    print(machine.mem[page][word])
    return 0

def LOAD(op):
    page, word = address_split(op)
    machine.acc = int(machine.mem[page][word])
    return 0

def LOADIM(op):
    machine.acc = int(op)
    return 0

def LOADX(op):
    page, word = address_split(op)
    machine.idx = int(machine.mem[page][word])
    return 0

def LOADIDX(op):
    page, word = address_split(machine.idx)
    machine.acc = int(machine.mem[page][word])
    return 0

def STORE(op):
    page, word = address_split(op)
    machine.mem[page][word] = str(machine.acc)
    return 0

def STOREIDX(op):
    page, word = address_split(machine.idx)
    machine.mem[page][word] = str(machine.acc)
    return 0

def ADD(op):
    page, word = address_split(op)
    machine.acc += int(machine.mem[page][word])
    return 0

def ADDX(op):
    page, word = address_split(machine.idx)
    machine.acc += int(machine.mem[page][word])
    return 0

def SUBTRACT(op):
    page, word = address_split(op)
    machine.acc -= int(machine.mem[page][word])
    return 0

def SUBTRACTX(op):
    page, word = address_split(machine.idx)
    machine.acc -= int(machine.mem[page][word])
    return 0

def DIVIDE(op):
    page, word = address_split(op)
    machine.acc //= int(machine.mem[page][word])
    return 0

def DIVIDEX(op):
    page, word = address_split(machine.idx)
    machine.acc //= int(machine.mem[page][word])
    return 0

def MULTIPLY(op):
    page, word = address_split(op)
    machine.acc *= int(machine.mem[page][word])
    return 0

def MULTIPLYX(op):
    page, word = address_split(machine.idx)
    machine.acc *= int(machine.mem[page][word])
    return 0

def INC(op):
    machine.idx += 1
    return 0

def DEC(op): 
    machine.idx -= 1
    return 0

def BRANCH(op):
    machine.ic = int(op) 
    return 0

def BRANCHNEG(op):
    if machine.acc >= 0:
        return 0 # Do nothing if positive
    #else branch
    machine.ic = int(op) 
    return 0

def BRANCHZERO(op):
    if machine.acc != 0:
        return 0 # Do nothing if not zero
    #else branch
    machine.ic = int(op)
    return 0

def SWAP(op):
    machine.acc, machine.idx = machine.idx, machine.acc
    return 0

def HALT(op):
    start, end = address_split(op)
    machine.dump_core(start, end)
    return 1

# Not an instruction, just helpful within them
# Takes a memory address and returns the page index, word index as ints
def address_split(address):
    return int(str(address).zfill(4)[0:2]), int(str(address).zfill(4)[2:4])