import sys

def multipleMove(map, moves, x1, y1):
    print(moves)
    for move in moves:
        map, x1, y1 = moveRobot(map, x1, y1, move)
        append_ascii_map_to_file(map, str(move), "output.txt")
    return map

    
def moveRobot(map, x1, y1, move):
    x2, y2 = x1, y1
    boxStack = [(map[y2][x2], (y2, x2))]
    while map[y2][x2] != "#" and map[y2][x2] != ".":
        if move == "^":
            y2 -= 1
        elif move == ">":
            x2 += 1
        elif move == "v":
            y2 += 1
        elif move == "<":
            x2 -= 1
        boxStack.append((map[y2][x2], (y2, x2)))
    
    # print(move, boxStack)
    if boxStack[-1][0] != "#":
        while len(boxStack) > 1:
            finalChar, (y2, x2) = boxStack.pop()
            prevChar, (y1, x1) = boxStack[-1]
            map[y2][x2] = prevChar
        robotChar, (yf, xf) = boxStack[-1]
        map[yf][xf] = "."
        return map, x2, y2
        
    return map, x1, y1

def calculateGPSScore(asciiMap):
    sumGPS = 0
    for r, row in enumerate(asciiMap):
        for c, col, in enumerate(row):
            if asciiMap[r][c] == "O":
                sumGPS += (100 * r) + c
    return sumGPS
    

def find_start(asciiMap):
    for r, row in enumerate(asciiMap):
        for c, col in enumerate(row):
            if asciiMap[r][c] == "@":
                return r, c
    
def read_ascii_map(file_path):
    with open(file_path, 'r') as file:
        # Read lines, strip newlines, and split each line into a list of characters
        map_2d_array = [list(line.strip()) for line in file]
    append_ascii_map_to_file(map_2d_array, "start", "output.txt")
    return map_2d_array

def print_ascii_map(ascii_map):
    for row in ascii_map:
        print(''.join(row))  # Join the characters in each row and print as a single line

def append_ascii_map_to_file(ascii_map, move, output_file):
    """
    Appends an ASCII map to the specified output file.

    :param ascii_map: A 2D list representing the ASCII map.
    :param output_file: The file path to which the ASCII map will be appended.
    """
    with open(output_file, 'a') as file:
        file.write("Move: " + move + '\n')
        for row in ascii_map:
            file.write(''.join(row) + '\n')
        file.write("\n")

def readMoves(filename):
    with open(filename, 'r') as file:
        moves = file.read().replace('\n', '')
        moveList = list(moves)
    return moveList


def main():
    asciiMap = read_ascii_map(sys.argv[1])
    moveList = readMoves(sys.argv[2])
    x1, y1 = find_start(asciiMap)
    asciiMap = multipleMove(asciiMap, moveList, x1, y1)
    print(calculateGPSScore(asciiMap))


if __name__ == "__main__":
    main()