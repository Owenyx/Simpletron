
import re
import machine

# If an instruction returns a string, it is an error message
# Operands will always be an integer of 4 digits or fewer, possibly negative

# Errors invloving out of memory bounds, divide by zero, invalid operands, and accumulator overflow are covered
# Another error covered is if an instruction tries to convert an instruction with a negative operand to
# an int, which will not convert properly - this error is "Error: Data at memory location must be an integer value"

def READ(op):

    if op<0: return "Error: Out of memory bounds" # operand tries to access out of memory bounds

    inp = input("? ")
    
    # check input validity
    while not re.match(r"^-?\d(\d?){5}$", inp): # if input is not as 6 or fewer digit integer, terminate with an error
        print("Invalid entry, try again")
        inp = input(f"{op} ? ")

    machine.mem[page][word] = inp
    return 0

def WRITE(op):
    if op<0: return "Error: Out of memory bounds" 

    print(machine.mem[page][word])
    return 0

def LOAD(op):
    if op<0: return "Error: Out of memory bounds" 
    if neg_operand_at(op): return "Error: Data at memory location must be an integer value"

    machine.acc = int(machine.mem[page][word])
    return 0

def LOADIM(op):
    machine.acc = int(op)
    return 0

def LOADX(op):
    if op<0: return "Error: Out of memory bounds" 
    if neg_operand_at(op): return "Error: Data at memory location must be an integer value"

    machine.idx = int(machine.mem[page][word])
    return 0

def LOADIDX(op):
    if machine.idx < 0: return "Error: Out of memory bounds" 
    if neg_operand_at(machine.idx): return "Error: Data at memory location must be an integer value"
    page, word = address_split(machine.idx)
    machine.acc = int(machine.mem[page][word])
    return 0

def STORE(op):
    if op<0: return "Error: Out of memory bounds" 

    machine.mem[page][word] = str(machine.acc)
    return 0

def STOREIDX(op):
    if machine.idx < 0: return "Error: Out of memory bounds" 
    page, word = address_split(machine.idx)
    machine.mem[page][word] = str(machine.acc)
    return 0

def ADD(op):
    if op<0: return "Error: Out of memory bounds" 
    if neg_operand_at(op): return "Error: Data at memory location must be an integer value"
    if acc_overflow(op): return "Error: Accumulator overflow"

    machine.acc += int(machine.mem[page][word])
    return 0

def ADDX(op):
    if machine.idx < 0: return "Error: Out of memory bounds" 
    if neg_operand_at(machine.idx): return "Error: Data at memory location must be an integer value"
    if acc_overflow(machine.idx): return "Error: Accumulator overflow"
    page, word = address_split(machine.idx)
    machine.acc += int(machine.mem[page][word])
    return 0

def SUBTRACT(op):
    if op<0: return "Error: Out of memory bounds" 
    if neg_operand_at(op): return "Error: Data at memory location must be an integer value"
    if acc_overflow(op): return "Error: Accumulator overflow"

    machine.acc -= int(machine.mem[page][word])
    return 0

def SUBTRACTX(op):
    if machine.idx < 0: return "Error: Out of memory bounds" 
    if neg_operand_at(machine.idx): return "Error: Data at memory location must be an integer value"
    if acc_overflow(machine.idx): return "Error: Accumulator overflow"
    page, word = address_split(machine.idx)
    machine.acc -= int(machine.mem[page][word])
    return 0

def DIVIDE(op):
    if op<0: return "Error: Out of memory bounds" 
    if neg_operand_at(op): return "Error: Data at memory location must be an integer value"

    if int(machine.mem[page][word]) == 0: return "Error: Divide by zero"
    machine.acc //= int(machine.mem[page][word])
    return 0

def DIVIDEX(op):
    if machine.idx < 0: return "Error: Out of memory bounds" 
    page, word = address_split(machine.idx)
    if int(machine.mem[page][word]) == 0: return "Error: Divide by zero"
    machine.acc //= int(machine.mem[page][word])
    return 0

def MULTIPLY(op):
    if acc_overflow(op): return "Error: Accumulator overflow"
    if neg_operand_at(op): return "Error: Data at memory location must be an integer value"
    if op<0: return "Error: Out of memory bounds" 

    machine.acc *= int(machine.mem[page][word])
    return 0

def MULTIPLYX(op):
    if machine.idx < 0: return "Error: Out of memory bounds" 
    if neg_operand_at(machine.idx): return "Error: Data at memory location must be an integer value"
    if acc_overflow(machine.idx): return "Error: Accumulator overflow"
    page, word = address_split(machine.idx)
    machine.acc *= int(machine.mem[page][word])
    return 0

def INC(op):
    if machine.idx == 999999: return "Error: Index register overflow"
    machine.idx += 1
    return 0

def DEC(op): 
    if machine.idx == -999999: return "Error: Index register overflow"
    machine.idx -= 1
    return 0

def BRANCH(op):
    if op<0: return "Error: Out of memory bounds" 
    machine.ic = int(op) 
    return 0

def BRANCHNEG(op):
    if op<0: return "Error: Out of memory bounds"
    if machine.acc >= 0:
        return 0 # Do nothing if positive
    #else branch
    machine.ic = int(op) 
    return 0

def BRANCHZERO(op):
    if op<0: return "Error: Out of memory bounds" 
    if machine.acc != 0:
        return 0 # Do nothing if not zero
    #else branch
    machine.ic = int(op)
    return 0

def SWAP(op):
    machine.acc, machine.idx = machine.idx, machine.acc
    return 0

def HALT(op):
    if op<0: return "Error: Out of memory bounds" 
    start = op/100
    end = op%100
    machine.dump_core(start, end)
    return 1

# Checks if the accumulator goes over the limit of 999,999 or under the limit of -999,999
def acc_overflow(address):
    sum = int(machine.mem[address]) + machine.acc 
    if sum > 999999 or sum < -999999:
        return True
    return False

# Returns whether data in memory is an istruction with a negative operand
def neg_operand_at(address): 
    if len(machine.mem[address]) < 4: return False # an instruction with a nagative operand must have 2 digits before and 1 after the neagtive sign
    if machine.mem[page][word][2] == '-':
        return True
    return False