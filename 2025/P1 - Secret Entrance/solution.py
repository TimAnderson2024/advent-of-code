INPUT_FILEPATH = "D1 - Secret Entrance/input.txt"

# Count the number of times the vault will be exactly zero
def part_one(instructions):
    cur_pos = 50
    num_zero = 0

    for dir, dist in instructions:
        if dir == "L":
            cur_pos = (cur_pos - dist) % 100
        else:
            cur_pos = (cur_pos + dist) % 100
        
        if cur_pos == 0:
            num_zero += 1
    
    return num_zero

def part_two(instructions):
    cur_pos = 50
    num_zero = 0

    for dir, dist in instructions:
        for i in range(0, dist):
            if dir == "L":
                cur_pos -= 1
            else:
                cur_pos += 1

            if cur_pos % 100 == 0:
                num_zero += 1

    return num_zero

# Read input as a series of tuples (dir, num)
def read_input(input_file):
    instructions = []
    with open(input_file, "r") as file:
        for line in file:
            input = line.strip()
            instructions.append((input[0], int(input[1:])))
    
    return instructions

def main():
    instructions = read_input(INPUT_FILEPATH)
    solution = part_two(instructions)
    print(solution)


if __name__ == "__main__":
    main()
