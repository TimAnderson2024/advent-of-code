import sys
import re

def match_mul(input):
    sum = 0
    mults = re.findall(r"mul\((\d+),(\d+)\)", input)
    for mult in mults:
        sum += int(mult[0]) * int(mult[1])
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