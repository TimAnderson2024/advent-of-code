import sys

def check_corner(i, j, char, search):
    if 0 <= i < len(search) and 0 <= j < len(search[0]) and search[i][j] == char:
        return True

def find_cross(i, j, search):
    for corner in [(1, 1), (1, -1)]:
        primary_i, primary_j = i + corner[0], j + corner[1]
        secondary_i, secondary_j = i - corner[0], j - corner[1]
        
        # Check primary and secondary corner
        if check_corner(primary_i, primary_j, "M", search) and check_corner(secondary_i, secondary_j, "S", search) \
            or check_corner(primary_i, primary_j, "S", search) and check_corner(secondary_i, secondary_j, "M", search):
            continue # Continue to check other primary corner
        
        # No cross found
        else:
            return False
        
    return True
            
def find_a(search):
    total_xmas = 0
    for i, row in enumerate(search):
        for j, char in enumerate(row):
            if char == "A" and find_cross(i, j, search):
                total_xmas += 1
                print(f"X-MAS found at ({i}, {j})")
    return total_xmas

def read_input(input_file):
    grid = []
    with open(input_file, "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid
    
    
def main():
    search = read_input(sys.argv[1])
    print("Found: " + str(find_a(search)))
    
if __name__ == "__main__":
    main()