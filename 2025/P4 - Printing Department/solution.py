INPUT_FILEPATH = "P4 - Printing Department/input.txt"

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

def check_adjacent(map, row, col):
    rolls = 0

    for dx, dy in DIRECTIONS:
        next_row = row + dx
        next_col = col + dy

        if 0 <= next_row < len(map) and 0 <= next_col < len(map[0]):
            if map[next_row][next_col] == "@":
                rolls += 1

    return rolls < 4

def part_one(map):
    forklifts = 0
    for r, row in enumerate(map):
        for c, char in enumerate(row):
            if char == "@" and check_adjacent(map, r, c):
                forklifts += 1

    return forklifts

def part_two(map):
    total_removed = 0
    last_removed = -1
    while last_removed != 0:
        last_removed = 0
        next_map = [row.copy() for row in map]

        for r, row in enumerate(map):
            for c, char in enumerate(row):
                if char == "@" and check_adjacent(map, r, c):
                    last_removed += 1
                    next_map[r][c] = "."

        total_removed += last_removed
        map = next_map

    return total_removed

def read_input(input_file):
    map = []
    with open(input_file, "r") as file:
        for line in file:
            map.append(list(line.strip('\n')))

    return map

def main():
    map = read_input(INPUT_FILEPATH)
    print(part_one(map))
    print(part_two(map))


if __name__ == "__main__":
    main()