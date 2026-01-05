import sys
from collections import deque

START = (0, 0)

def findPathBFS(asciiMap, goal):
    # Initialize data structures
    frontier = deque([START])
    backtrack = {START : None}

    while len(frontier) > 0:
        # Get the state with the lowest priority score (cheapest to get to)
        cur_pos = frontier.popleft()
        # print(f"New state: {cur_pos}")
        
        # If we've reached the goal, stop searching
        if cur_pos == goal:
            return backtrack
        
        # Neighbors = [N, E, S, W]
        neighbors = getNeighbors(asciiMap, cur_pos)
        # print(f"Neighbors: {neighbors}")
        for neighbor in neighbors:
            # If we haven't reached this pos yet
            if neighbor not in backtrack:
                frontier.append(neighbor)
                backtrack[neighbor] = cur_pos
    
    print("NO PATH FOUND")
    return backtrack
        
 
MOVES = {
    'N': (-1, 0),  # Move up
    'S': (1, 0),   # Move down
    'E': (0, 1),   # Move right
    'W': (0, -1)   # Move left
} 
def getNeighbors(asciiMap, cur_pos):
    neighbors = []
    cur_r, cur_c = cur_pos
        
    for move in ['N', 'S', 'E', 'W']:
        new_r, new_c = cur_r + MOVES[move][0], cur_c + MOVES[move][1]
        if new_r >= 0 and new_r < len(asciiMap) and new_c >= 0 and new_c < len(asciiMap[0]) and asciiMap[new_r][new_c] != "#":
            neighbors.append((new_r, new_c))
            
    return neighbors


def backtrack(backtrack, goal, asciiMap):
    path = []
    cur_pos = goal
    num_steps = 0
    while cur_pos != START:
        path.append(cur_pos)
        asciiMap[cur_pos[0]][cur_pos[1]] = "!"
        
        cur_pos = backtrack[cur_pos]
        num_steps += 1
        # print(f"{cur_pos}")
    
    return path, asciiMap, num_steps

def checkPath(path, asciiMap):
    for pos in path:
        if asciiMap[pos[0]][pos[1]] == "#":
            return False
    
    return True

# Generates the map after num_bytes from file_path have fallen
def generate_ascii_map(file_path, num_bytes):
    with open(file_path, 'r') as file:
        r, c = map(int, file.readline().strip().split(","))
        new_map = [["." for _ in range(c)] for _ in range(r)]
        goal = (r - 1, c - 1)
        
        for i, line in enumerate(file.readlines()):
            if i >= num_bytes:
                break
            c, r = map(int, line.strip().split(","))
            new_map[r][c] = '#'
                        
    return new_map, goal

def append_ascii_map_to_file(ascii_map, output_file):
    with open(output_file, 'a') as file:
        for row in ascii_map:
            file.write(''.join(row) + '\n')
        file.write("\n")

def print_ascii_map(ascii_map):
    for row in ascii_map:
        print(''.join(row))  

def find_illegal_map_bf():
    num_bytes = 1024
    ascii_map, goal = generate_ascii_map(sys.argv[1], num_bytes)
    path = findPathBFS(ascii_map, goal)

    while goal in path:
        num_bytes += 1
        ascii_map, _ = generate_ascii_map(sys.argv[1], num_bytes)
        path = findPathBFS(ascii_map, goal)
    
    return ascii_map, num_bytes


def main():
    ascii_map, max_bytes = find_illegal_map_bf()
    append_ascii_map_to_file(ascii_map, "output.txt")
    print(max_bytes)

if __name__ == "__main__":
    main()