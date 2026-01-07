INPUT_FILEPATH = "P6 - Trash Compactor/input.txt"

def part_one(nums):
    values = nums[:4]
    ops = nums[4]
    total = 0

    for i, op in enumerate(ops):
        if op == "*":
            total += (values[0][i] * values[1][i] * values[2][i] * values[3][i])
        elif op == "+":
            total += (values[0][i] + values[1][i] + values[2][i] + values[3][i])

    return total

def part_two(nums):
    rows = []
    print(len(nums))
    with open(INPUT_FILEPATH, "r") as f:
        for line in f:
            rows.append(list(line))
    
    grand_total = 0
    ops = rows[len(nums) - 1]
    op_pos = 0
    next_op_pos = 0
    while op_pos < len(ops):
        op = ops[op_pos]
        next_op_pos = op_pos + 1

        while next_op_pos < len(ops) and ops[next_op_pos] == " ":
            next_op_pos += 1
        
        merged = [[] for _ in range(op_pos, next_op_pos - 1)]
        # Collate numbers using Cephalopod notation
        for r in range(len(nums) - 1):
            for c in range(op_pos, next_op_pos):
                if rows[r][c] != " ":
                    print(c, op_pos, c - op_pos)
                    merged[c - op_pos].append(int(rows[r][c]))
        print(merged)
        merged = [''.join([str(n) for n in num]) for num in merged]
        print(merged)

        # Do operations
        result = 0
        if op == "*":
            result = 1
            for num in merged:
                result *= int(num)
        elif op == "+":
            result = 0
            for num in merged:
                result += int(num)
        grand_total += result

        op_pos = next_op_pos
    return grand_total


def read_input(input_file):
    input = []
    with open(input_file, "r") as file:
        for line in file:
            input.append([int(x) if x.isdigit() else x for x in line.strip().split()])

    return input

def main():
    nums = read_input(INPUT_FILEPATH)
    # print(nums)
    # print(part_one(nums))
    print(part_two(nums))


if __name__ == "__main__":
    main()