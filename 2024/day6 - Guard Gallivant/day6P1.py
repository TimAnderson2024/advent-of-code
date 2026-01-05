import sys

def on_map(row, col, map):
    return 0 <= row < len(map) and 0 <= col <= len(map[0])

MOVES = {
    "N" : (-1, 0),
    "E" : (0, 1),
    "S" : (1, 0),
    "W" : (0, -1)
}
TURN_ORDER = ["N", "E", "S", "W"]
def simulate_moves(map, start):
    row, col = start[0], start[1]
    dir = "N"
    visited = {start}
    while on_map(row, col, map):
        new_r, new_c = row + MOVES[dir][0], col + MOVES[dir][1]
        
        if not on_map(new_r, new_c, map):
            return visited
        elif map[new_r][new_c] == "#":
            dir = TURN_ORDER[(TURN_ORDER.index(dir) + 1) % 4]
        else:
            row, col = new_r, new_c
            visited.add((row, col))
        
    return visited

def find_start(map):
    for i, row in enumerate(map):
        for j, _, in enumerate(row):
            if map[i][j] == "^":
                return (i, j)

def read_input(input_file):
    grid = []
    with open(input_file, "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid

def main():
    map = read_input(sys.argv[1])
    start = find_start(map)
    visited = simulate_moves(map, start)
    print(len(visited))
    
if __name__ == "__main__":
    main()