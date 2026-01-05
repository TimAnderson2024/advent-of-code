import sys
from collections import deque

def DFS(map, graph, trailhead):
    score = 0
    visited = set()
    frontier = deque()
    
    visited.add(trailhead)
    frontier.append(trailhead)
    
    while len(frontier) != 0:
        cur = frontier.pop()
        
        if cur not in visited and int(map[cur[0]][cur[1]]) == 9:
            score += 1
        else:
            for edge in graph[cur]:
                if edge not in visited:
                    frontier.appendleft(edge)
        
        visited.add(cur)
    
    return score
                
    
def test_trailheads(map, graph, trailheads):
    total_score = 0
    for trailhead in trailheads:
        print(trailhead)
        total_score += DFS(map, graph, trailhead)
    
    return total_score

# N, E, S, W
MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def get_neighbors(map, coord):
    r, c = coord
    neighbors = []
    for move in MOVES:
        new_r, new_c = r + move[0], c + move[1]
        
        if 0 <= new_r < len(map) and 0 <= new_c < len(map):
            neighbors.append((new_r, new_c))
    
    return neighbors
    

def make_graph(map):
    graph = {}
    trailheads = []
    for r, row in enumerate(map):
        for c, num in enumerate(row):
            edges = []
            neighbors = get_neighbors(map, (r, c))
            
            for neighbor in neighbors: 
                if int(map[neighbor[0]][neighbor[1]]) == int(num) + 1:
                    edges.append((neighbor[0], neighbor[1]))
            
            graph[(r, c)] = edges
                
            if int(num) == 0:
                trailheads.append((r, c))
                
          
    
    return graph, trailheads
                    

def read_input(input_file):
    map = []
    with open(input_file, "r") as file:
        map = [list(line.strip()) for line in file]
    return map

def main():
    map = read_input(sys.argv[1])
    graph, trailheads = make_graph(map)
    for key in graph.keys():
        print(key, graph[key])
    score = test_trailheads(map, graph, trailheads)
    print(score)
    
if __name__ == "__main__":
    main()