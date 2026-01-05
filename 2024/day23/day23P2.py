import sys
import itertools

def find_max_clique(graph: dict):
    max_clique = []
    for node in graph.keys():
        neighbors = graph[node]
        # Start with max possible subset and get smaller
        for subset_len in range(len(neighbors), 2, -1):
            # Test all combinations of this subset len
            for subset in itertools.combinations(neighbors, subset_len):
                if is_clique(subset, graph):
                    max_clique = max(max_clique, [node] + list(subset), key=len)
                    # print(f"Max Clique: {max_clique}")

    return max_clique

def is_clique(subset, graph):
    # Iterate over each node in subset
    for node in range(0, len(subset)): 
        # Compare each node with each neighbor
        for neighbor in range(node + 1, len(subset)): 
            # If node does not appear in neighbor adjacency, then not a clique
            if subset[node] not in graph[subset[neighbor]]: 
                return False
    
    return True

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
    print(adjacency_graph)
    max_clique = find_max_clique(adjacency_graph)
    max_clique.sort()
    print(",".join(max_clique))
    
    
if __name__ == "__main__":
    main()