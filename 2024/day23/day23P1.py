import sys

def find_chief(graph):
    chief_char = 't'
    triangles = set()
    
    for computer in list(graph.keys()): # Iterate over every computer
        if computer[0] == chief_char: # If the computer starts with t
            for neighbor in graph[computer]: # Look over each neighbor
                for neighbor_2 in graph[neighbor]: # Look over each 2nd neighbor
                    if neighbor_2 in graph[computer] and neighbor_2 in graph[neighbor]:
                        trio = [computer, neighbor, neighbor_2]
                        trio.sort()
                        trio = tuple(trio)
                        triangles.add(trio)
                        
    return triangles

def build_adjacency_graph(input_pairs):
    graph = {}
    for pair in input_pairs:
        input1, input2 = pair[0], pair[1]
        graph.setdefault(input1, set()).add(input2)
        graph.setdefault(input2, set()).add(input1)
    return graph

def print_sets(set_list):
    for set in set_list:
        print(f"{set}")
    print(f"Num Sets: {len(set_list)}")
        
def read_input_file(file_name):
    with open(file_name, 'r') as file:
        input_pairs = list((line.strip().split('-')) for line in file)
    return input_pairs

def main():
    input_pairs = read_input_file(sys.argv[1])
    adjacency_graph = build_adjacency_graph(input_pairs)
    trios = find_chief(adjacency_graph)
    print(trios)
    print_sets(trios)
    
    
if __name__ == "__main__":
    main()