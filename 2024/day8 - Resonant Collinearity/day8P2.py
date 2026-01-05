import sys

MAP = []

def print_map():
    global MAP
    for row in MAP:
        print("".join(row))

def in_bounds(antinode):
    return 0 <= antinode[0] < len(MAP) and 0 <= antinode[1] < len(MAP[0]) 

def find_antinodes(coordinates):
    antinodes = set()
    for i, coordA in enumerate(coordinates):
        for j, coordB in enumerate(coordinates[i+1:]):
            slopeR = coordB[0] - coordA[0] 
            slopeC = coordB[1] - coordA[1]
            
            antinodeA = coordA
            antinodeB = coordB

            # antinodeA = (coordA[0] - slopeR, coordA[1] - slopeC)
            # antinodeB = (coordB[0] + slopeR, coordB[1] + slopeC)
            
            while in_bounds(antinodeA):
                MAP[antinodeA[0]][antinodeA[1]] = "#"
                antinodes.add(antinodeA)
                
                antinodeA = (antinodeA[0] - slopeR, antinodeA[1] - slopeC)
            
            while in_bounds(antinodeB):
                MAP[antinodeB[0]][antinodeB[1]] = "#"
                antinodes.add(antinodeB)
                
                antinodeB = (antinodeB[0] + slopeR, antinodeB[1] + slopeC)
                
    return antinodes
        

def process_signals(antennas):
    antinodes = set()
    for signal_type in list(antennas.keys()):
        new_antinodes = find_antinodes(antennas[signal_type])
        antinodes.update(new_antinodes)
    return len(antinodes)

def read_input(input_file):
    global MAP
    grid = []
    antennas = {}
    with open(input_file, "r") as file:
        for row, line in enumerate(file):
            grid.append(list(line.strip()))
            for col, char in enumerate(line.strip()):
                if char != ".":
                    antennas[char] = antennas.get(char, []) + [(row, col)]
    MAP = grid
    return antennas
    
def main():
    antennas = read_input(sys.argv[1])
    num_anti = process_signals(antennas)
    print_map()
    print(num_anti)
    
if __name__ == "__main__":
    main()