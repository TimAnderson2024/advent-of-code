import sys
import heapq
from math import sqrt

def findPathDijkstra(asciiMap, start_state, goal_pos):
    # Initialize data structures
    frontier = []
    backtrack = dict()
    lowest_cost = {}
    iterations = 0
    
    # Add starting cell to data
    lowest_cost[start_state] = 0
    heapq.heappush(frontier, (0, start_state))
    backtrack[start_state] = (None, 0)

    while len(frontier) > 0:
        iterations += 1
        # Get the state with the lowest priority score (cheapest to get to)
        priority, cur_state = heapq.heappop(frontier)
        cur_pos, cur_dir = cur_state
        print(f"New state: {cur_pos}, {cur_dir}")
        
        # If we've reached the goal, stop searching
        if cur_pos == goal_pos:
            break
        
        # Neighbors = [move straight, turn left, turn right]
        # Neighbors = [[cost, ((r, c), dir)], [cost, ((r, c), dir)]...]
        neighbors = getNeighbors(asciiMap, cur_state)
        print(f"Neighbors: {neighbors}")
        for neighbor in neighbors:
            neighbor_cost, neighbor_state = neighbor[0], neighbor[1]
            neighbor_pos, neighbor_dir = neighbor_state[0], neighbor_state[1]
            
            # Cost to reach neighbor state on this path
            new_cost = lowest_cost[cur_state] + neighbor_cost

            # If we haven't reached this state or this is the cheapest way to get here
            if neighbor_state not in lowest_cost or new_cost < lowest_cost[neighbor_state]:
                # Set the new cost to get here 
                lowest_cost[neighbor_state] = new_cost 
                
                # Add this neighbor state to the frontier and add backtrack link
                priority = new_cost
                new_state = (neighbor_pos, neighbor_dir)
                heapq.heappush(frontier, (priority, new_state))
                backtrack[neighbor_state] = (cur_state, priority)
        # print(f"Frontier: {frontier}")
        # print(f"Costs: {lowest_cost}\n")
    
    print(f"Iterations: {iterations}")                
    return backtrack, cur_state
        
# Neighbors = [move straight, turn left, turn right]
# Neighbors = [[cost, (r, c), dir], [cost, (r, c), dir]...]       
DIRECTIONS = ['N', 'E', 'S', 'W']
MOVES = {
    'N': (-1, 0),  # Move up
    'S': (1, 0),   # Move down
    'E': (0, 1),   # Move right
    'W': (0, -1)   # Move left
} 
  
def getNeighbors(asciiMap, cur_state):
    neighbors = []
    cur_pos, cur_dir = cur_state
    
    # Calculate going straight
    straight_pos = (cur_pos[0] + MOVES[cur_dir][0], cur_pos[1] + MOVES[cur_dir][1])
    if asciiMap[straight_pos[0]][straight_pos[1]] != "#":
        neighbors.append([1, (straight_pos, cur_dir)])
    
    # Calculate turning right
    right_dir = DIRECTIONS[(DIRECTIONS.index(cur_dir) + 1) % 4]
    right_pos = (cur_pos[0] + MOVES[right_dir][0], cur_pos[1] + MOVES[right_dir][1])
    if asciiMap[right_pos[0]][right_pos[1]] != "#":
        neighbors.append([1000, (cur_pos, right_dir)])
    
    # Calculate turning left
    left_dir = DIRECTIONS[(DIRECTIONS.index(cur_dir) - 1) % 4]
    left_pos = (cur_pos[0] + MOVES[left_dir][0], cur_pos[1] + MOVES[left_dir][1])
    if asciiMap[left_pos[0]][left_pos[1]] != "#":
        neighbors.append([1000, (cur_pos, left_dir)])
        
    return neighbors

def estimateDistance(curPos, goalPos):
    r1, c1 = curPos
    r2, c2 = goalPos
    return sqrt(pow(c2 - c1, 2) + pow(r2 - r1, 2))

def backtrack(backtrack, start_state, goal_state, asciiMap):
    path = []
    cur_state = goal_state
    
    while cur_state != start_state:
        path.append(cur_state)
        cur_pos = cur_state[0]
        asciiMap[cur_pos[0]][cur_pos[1]] = "!"
        
        cur_state, score= backtrack[cur_state]
        print(f"{cur_state}, {score}")
    
    return path, asciiMap

def findSG(asciiMap):
    start = -1
    goal = -1
    for r, row in enumerate(asciiMap):
        for c, _ in enumerate(row):
            if asciiMap[r][c] == "S":
                start = (r, c)
            elif asciiMap[r][c] == "E":
                goal = (r, c)
                
            if start != -1 and goal != -1:
                return start, goal


def read_ascii_map(file_path):
    with open(file_path, 'r') as file:
        # Read lines, strip newlines, and split each line into a list of characters
        map_2d_array = [list(line.strip()) for line in file]
    return map_2d_array

def append_ascii_map_to_file(ascii_map, output_file):
    with open(output_file, 'a') as file:
        for row in ascii_map:
            file.write(''.join(row) + '\n')
        file.write("\n")

def print_ascii_map(ascii_map):
    for row in ascii_map:
        print(''.join(row))  

def main():
    asciiMap = read_ascii_map(sys.argv[1])
    print_ascii_map(asciiMap)
    start_pos, goal_pos = findSG(asciiMap)
    start_state = (start_pos, "E")
    path, goal_state = findPathDijkstra(asciiMap, start_state, goal_pos)

    actualPath, solvedMap = backtrack(path, start_state, goal_state, asciiMap)
    # append_ascii_map_to_file(solvedMap, "output.txt")

if __name__ == "__main__":
    main()