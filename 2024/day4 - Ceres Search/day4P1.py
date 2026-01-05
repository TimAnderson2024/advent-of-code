import sys


# Iterate over each character
# If character is an "X":
    # Iterate each direction, looking for M, then A, then S
# E, SE, S, SW, 
MOVES = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
LETTERS = ["M", "A", "S"]
def find_word(i, j, search):
    xmas_found = 0
    for move in MOVES:
        print(f"Checking move {move}")
        new_i, new_j = i, j
        for letter in LETTERS:
            new_i, new_j = new_i + move[0], new_j + move[1]
            print(f"Looking for {letter} at {new_i}, {new_j}")
            # print(len(search[1]))
            if new_i < 0 or new_j < 0 or new_i >= len(search) or new_j >= len(search[1]):
                print(f"ILLEGAL: Out of bounds")
                break
            elif search[new_i][new_j] != letter:
                print(f"ILLEGAL, was looking for letter {letter} but found {search[new_i][new_j]}")
                break
            elif letter == "S":
                print(f"XMAS Found")
                xmas_found += 1
    return xmas_found
    
def find_x(search):
    total_xmas = 0
    for i, row in enumerate(search):
        for j, char in enumerate(row):
            if char == "X":
                print(f"X found at ({i}, {j})")
                total_xmas += find_word(i, j, search)
    return total_xmas

def read_input(input_file):
    grid = []
    with open(input_file, "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid
    
    
def main():
    search = read_input(sys.argv[1])
    print("Found: " + str(find_x(search)))
    
if __name__ == "__main__":
    main()