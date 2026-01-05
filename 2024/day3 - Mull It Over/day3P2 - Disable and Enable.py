import sys
import re

def match_mul(input):
    mults = re.findall(r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))", input)
    
    sum = 0
    active = True
    for mult in mults:
        if mult[0] != "" and mult[1] != "" and active:
            sum += int(mult[0]) * int(mult[1])
        elif mult[2] == "don't()":
            active = False
        elif mult[3] == "do()":
            active = True 
    
    return sum

def read_input(input_file):
    with open(input_file, 'r') as file:
        return file.read()

def main():
    input = read_input(sys.argv[1])
    sum = match_mul(input)
    print(sum)
    
if __name__ == "__main__":
    main()