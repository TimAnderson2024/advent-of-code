import re

INPUT_FILEPATH = "D2 - Gift Shop/input.txt"

def part_one(ranges):
    invalid = 0
    for lower, upper in ranges:
        for i in range(lower, upper + 1):
            str_i = str(i)
            
            if len(str_i) % 2 == 0 and str_i[:len(str_i) // 2] == str_i[len(str_i) // 2:]:
                invalid += i
    return invalid

def part_two(ranges):
    invalid = 0
    for lower, upper in ranges:
        for i in range(lower, upper + 1):
            str_i = str(i)
            if detect_repeat(str_i):
                invalid += i
    return invalid

def detect_repeat(num: str):
    len_repeat = 1
    while len_repeat <= len(num) // 2:
        cur_repeat = num[:len_repeat]
        if cur_repeat * (len(num) // len_repeat) == num:
            return True
        len_repeat += 1

# Read input as a series of tuples (dir, num)
def read_input(input_file):
    with open(input_file, "r") as file:
        input = file.readline().strip()
        input = re.split(r"[,-]+", input)

    bounds = []
    while len(input) > 1:
        bounds.append((int(input.pop(0)), int(input.pop(0))))

    return bounds


def main():
    input = read_input(INPUT_FILEPATH)
    print(part_one(input))
    print(part_two(input))

if __name__ == "__main__":
    main()
