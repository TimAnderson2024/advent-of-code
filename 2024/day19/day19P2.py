import sys
from functools import cache

towels = set()
@cache
def build_design(design, max_towel_len):
    if len(design) == 0:
        return 1
    
    legal_designs = 0
    sub_len = min(len(design), max_towel_len)
    for i in range(sub_len, 0, -1):
        sub_str = design[0:i]
        print(f"Examining {sub_str}")
        if sub_str in towels:
            legal_designs += build_design(design[i:], max_towel_len)
    return legal_designs

def check_designs(designs):
    max_towel_len = get_longest_towel()
    legal_designs = 0
    for design in designs:
        print(f"Checking design {design}")
        legal_designs += build_design(design, max_towel_len)
    return legal_designs

def get_longest_towel():
    max_len = 0
    for towel in towels:
        max_len = max(max_len, len(towel))
        
    return max_len

def read_input(towel_input, design_input):
    with open(towel_input, 'r') as file:
        lines = file.readlines()
        for line in lines:
            for towel in map(str.strip, line.split(",")):
                towels.add(towel)
                
    with open(design_input, 'r') as file:
        lines = file.readlines()
        designs = []
        for line in lines:
            designs.append(line.strip())
    print(f"Towels: {towels}")
    print(f"Designs: {designs}")
    return designs
                

def main():
    designs = read_input(sys.argv[1], sys.argv[2])
    print(f"Num Legal Designs {check_designs(designs)}")

if __name__ == "__main__":
    main()