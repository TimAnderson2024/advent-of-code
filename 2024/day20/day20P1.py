import sys
from collections import deque

def findPathBFS(asciiMap, goal, start):
    # Initialize data structures
    frontier = deque([start])
    backtrack = {start : None}

    while len(frontier) > 0:
        # Get the state with the lowest priority score (cheapest to get to)
        cur_pos = frontier.popleft()
        print(f"New state: {cur_pos}")
        
        # If we've reached the goal, stop searching
        if cur_pos == goal:
            break
        
        # Neighbors = [N, E, S, W]
        neighbors = getNeighbors(asciiMap, cur_pos)
        print(f"Neighbors: {neighbors}")
        for neighbor in neighbors:
            # If we haven't reached this pos yet
            if neighbor not in backtrack:
                frontier.append(neighbor)
                backtrack[neighbor] = cur_pos
    
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

def backtrack(backtrack, start, goal, asciiMap):
    path = []
    cur_pos = goal
    print(f"Cur_pos: {cur_pos}")
    num_steps = 0
    while cur_pos != start:
        path.append(cur_pos)
        asciiMap[cur_pos[0]][cur_pos[1]] = "!"
        
        cur_pos = backtrack[cur_pos]
        num_steps += 1
        print(f"{cur_pos}")
    
    return path, asciiMap, num_steps

def findSG(ascii_map):
    start, goal = -1, -1
    for r, row in enumerate(ascii_map):
        for c, _ in enumerate(row):
            if ascii_map[r][c] == "S":
                start = (r, c)
            elif ascii_map[r][c] == "E":
                goal = (r, c)
    
    return start, goal

def read_ascii_map(file_path):
    with open(file_path, 'r') as file:
        ascii_map = [list(line.strip()) for line in file]   
    return ascii_map

def append_ascii_map_to_file(ascii_map, output_file):
    with open(output_file, 'a') as file:
        for row in ascii_map:
            file.write(''.join(row) + '\n')
        file.write("\n")

def main():
    ascii_map = read_ascii_map(sys.argv[1])
    start, goal = findSG(ascii_map)
    print(start, goal)
    path = findPathBFS(ascii_map, start, goal)
    
    actualPath, solvedMap, num_steps = backtrack(path, start, goal, ascii_map)
    append_ascii_map_to_file(solvedMap, "output1.txt")
    
if __name__ == "__main__":
    main()