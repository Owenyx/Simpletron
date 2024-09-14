import main
import machine

def READ(op):
    global mem
    page, word = address_split(op)
    main.mem[page][word] = int(input("? ")) #add input check???
    return 0

def WRITE(op):
    global mem
    page, word = address_split(op)
    print(main.mem[page][word])
    return 0

def LOAD(op):
    global mem
    global acc
    page, word = address_split(op)
    main.acc = main.mem[page][word]
    return 0

def LOADIM(op):
    global acc
    main.acc = op
    return 0

def LOADX(op):
    global mem
    global idx
    page, word = address_split(op)
    main.idx = main.mem[page][word]
    return 0

def LOADIDX(op):
    global mem
    global idx
    page, word = address_split(idx)
    main.acc = main.mem[page][word]
    return 0

def STORE(op):
    global mem
    global acc
    page, word = address_split(op)
    main.mem[page][word] = main.acc
    return 0

def STOREIDX(op):
    global mem
    global idx
    page, word = address_split(idx)
    main.mem[page][word] = main.acc
    return 0

def ADD(op):
    global mem
    global acc
    page, word = address_split(op)
    main.acc += main.mem[page][word]
    return 0

def ADDX(op):
    global mem
    global acc
    global idx
    page, word = address_split(idx)
    main.acc += mem[page][word]
    return 0

def SUBTRACT(op):
    global mem
    global acc
    page, word = address_split(op)
    main.acc -= main.mem[page][word]
    return 0

def SUBTRACTX(op):
    global mem
    global acc
    global idx
    page, word = address_split(idx)
    main.acc -= mem[page][word]
    return 0

def DIVIDE(op):
    global mem
    global acc
    page, word = address_split(op)
    main.acc //= main.mem[page][word]
    return 0

def DIVIDEX(op):
    global mem
    global acc
    global idx
    page, word = address_split(idx)
    main.acc //= mem[page][word]
    return 0

def MULTIPLY(op):
    global mem
    global acc
    page, word = address_split(op)
    main.acc *= main.mem[page][word]
    return 0

def MULTIPLYX(op):
    global mem
    global acc
    global idx
    page, word = address_split(idx)
    main.acc *= mem[page][word]
    return 0

def INC(op):
    global idx
    main.idx += 1
    return 0

def DEC(op):
    global idx
    main.idx -= 1
    return 0

def BRANCH(op):
    global ic
    main.ic = op 
    return 0

def BRANCHNEG(op):
    global acc
    if main.acc >= 0:
        return 0 # Do nothing if positive
    #else branch
    global ic
    main.ic = op 
    return 0

def BRANCHZERO(op):
    global acc
    if main.acc != 0:
        return 0 # Do nothing if not zero
    #else branch
    global ic
    main.ic = op 
    return 0

def SWAP(op):
    global acc
    global idx
    main.acc, main.idx = main.idx, main.acc
    return 0

def HALT(op):
    start, end = address_split(op)
    machine.dump_core(start, end)
    machine.end_execution()
    return 1

# Not an instruction, just helpful within them
# Takes a memory address and returns the page index, word index
def address_split(address):
    return int(str(address)[0:2]), int(str(address)[2:4])