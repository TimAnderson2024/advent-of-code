import sys
from collections import deque

def topological_sort(graph):
    ordering = deque()
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            DFS(graph, vertex, ordering, visited)
    return ordering

def DFS(graph, vertex, ordering : deque, visited : set):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            DFS(graph, neighbor, ordering, visited)
    ordering.appendleft(vertex)            
    
def test_trailheads(map, graph, trailheads, trailends):
    sorted_graph = topological_sort(graph)
    for node in sorted_graph:
        print(node, map[node[0]][node[1]])
    
    trail_score = 0
    for trailhead in trailheads:
        num_paths = {}
        num_paths[trailhead] = 1
            
        for node in sorted_graph:
            for neighbor in graph[node]:
                num_paths[neighbor] = num_paths.get(node, 0) + num_paths.get(neighbor, 0)
        
        for trailend in trailends:
            trail_score += num_paths.get(trailend, 0)
    
    return trail_score

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
    trailend = []
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
            elif int(num) == 9:
                trailend.append((r,c))
                
          
    
    return graph, trailheads, trailend
                    

def read_input(input_file):
    map = []
    with open(input_file, "r") as file:
        map = [list(line.strip()) for line in file]
    
    for r, line in enumerate(map):
        for c, char in enumerate(line):
            if char == ".":
                map[r][c] = -1
                
    return map

def main():
    map = read_input(sys.argv[1])
    graph, trailheads, trailends = make_graph(map)
    trail_score = test_trailheads(map, graph, trailheads, trailends)
    print(trail_score)

    
if __name__ == "__main__":
    main()