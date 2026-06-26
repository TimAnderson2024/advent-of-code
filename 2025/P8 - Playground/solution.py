INPUT_FILEPATH = "input.txt"

def part_one(input):
    
    pass

def part_two(input):
    pass

def read_input(input_file):
    input = []
    with open(input_file, "r") as file:
        for line in file:
            input.append(list(line.strip().split(',')))

    return input


def main():
    input = read_input(INPUT_FILEPATH)
    print(part_one(input))
    print(part_two(input))

if __name__ == "__main__":
    main()