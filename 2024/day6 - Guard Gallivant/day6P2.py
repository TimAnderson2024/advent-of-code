import sys
import copy
import time

def on_map(row, col, map):
    return 0 <= row < len(map) and 0 <= col < len(map[0])

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

def test_loop(map, start):
    row, col = start[0], start[1]
    dir = "N"
    visited = {(row, col, dir)}
    while on_map(row, col, map):
        new_r, new_c = row + MOVES[dir][0], col + MOVES[dir][1]

        if not on_map(new_r, new_c, map):
            return False, visited
        elif map[new_r][new_c] == "#":
            dir = TURN_ORDER[(TURN_ORDER.index(dir) + 1) % 4]
        else:
            row, col = new_r, new_c
        
        if (row, col, dir) in visited:
            return True, visited
        visited.add((row, col, dir))

    return False, visited

def print_path(map, path):
    for coord in path: 
        map[coord[0]][coord[1]] = "X" 
    
    for row in map:
        print(row)
        
def test_obstacles(map, start):
    path = simulate_moves(map, start)
    loops = 0
    for r, c in list(path):
        test_map = copy.deepcopy(map)
        if (r, c) != start:
            print(f"Testing obstacle at {r}, {c}")
            test_map[r][c] = "#"
            is_loop, path = test_loop(test_map, start)
            if is_loop:
                print("Is loop")
                loops += 1
            else:
                print("Not loop")
            # print_path(test_map, path)
    return loops

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
    start_time = time.time()
    loops = test_obstacles(map, start)
    end_time = time.time()
    print(loops)
    print(end_time - start_time)
    
if __name__ == "__main__":
    main()