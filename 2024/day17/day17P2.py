import sys

reg_a = 0
reg_b = 0
reg_c = 0
ip = 0
output = []

def get_combo(operand):
    global reg_a, reg_b, reg_c
    if operand == 4:
        return reg_a
    elif operand == 5:
        return reg_b
    elif operand == 6:
        return reg_c
    return operand

# Division on reg_a
def adv(operand):
    global reg_a
    reg_a = int((reg_a / (2 ** get_combo(operand))))
    
# Division on reg_b
def bdv(operand):
    global reg_b
    reg_b = int((reg_a / (2 ** get_combo(operand))))

# Division on reg_c
def cdv(operand):
    global reg_c
    reg_c = int((reg_a / (2 ** get_combo(operand))))
    
# Bitwise XOR on reg_b
def bxl(operand):
    global reg_b
    reg_b = reg_b ^ operand

# Save lowest 3 bits to reg_b
def bst(operand):
    global reg_b
    reg_b = get_combo(operand) % 8

# Move instruction pointer to operand - 1. Does nothing if A = 0
def jnz(operand):
    global ip
    if reg_a != 0:
        ip = operand - 2

# Bitwise XOR on rebB and regC, store in regB
def bxc(operand):
    global reg_b, reg_c
    reg_b = reg_b ^ reg_c

# Save lowest 3 bits of combo operand to output
def out(operand):
    global output
    output.append(get_combo(operand) % 8)
    print(output)

FUNCTION_LOOKUP = {
    0 : adv,
    1 : bxl,
    2 : bst,
    3 : jnz,
    4 : bxc,
    5 : out,
    6 : bdv,
    7:  cdv
}

def execute_program(instructions):
    global ip, reg_a, reg_b, reg_c
    while ip + 1 < len(instructions):
        print(f"Instruction: {instructions[ip]}, Operand: {instructions[ip + 1]}, registers: {reg_a}, {reg_b}, {reg_c}")
        FUNCTION_LOOKUP[instructions[ip]](instructions[ip + 1])
        ip += 2

# Read the instruction file 
def read_instructions(input_file):
    with open(input_file, 'r') as file:
        return list(map(int, file.readline().strip().split(",")))

# Set the register to the starting values
def set_registers(input_file):
    global reg_a, reg_b, reg_c
    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line_num, line in enumerate(lines):
            line = line.strip()
            if line_num == 0:
                reg_a = int(line.split(":")[1])
            elif line_num == 1:
                reg_b = int(line.split(":")[1])
            else:
                reg_c = int(line.split(":")[1])

def main():
    global output
    instructions = read_instructions(sys.argv[1])
    set_registers(sys.argv[2])
    execute_program(instructions)
    
    print(','.join(map(str, output)))

if __name__ == "__main__":
    main()