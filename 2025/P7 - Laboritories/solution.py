INPUT_FILEPATH = "input.txt"

def part_one(input):
    beam_indexes = set()
    
    # Get starting beam pos
    for col, cell in enumerate(input[0]):
        if cell == "S":
            beam_indexes.add(col)
    
    # For each row, check the col that had beams in the prev row
    splits = 0
    for r, row in enumerate(input):
        new_beams = set()
        for col in beam_indexes:
            
            # Split beam vs continue beam
            if input[r][col] == "^":
                splits += 1
                new_beams.add(col - 1)
                new_beams.add(col + 1)
            else:
                new_beams.add(col)
        
        # Switch out old beams for new beams
        beam_indexes = set()
        for beam in new_beams:
            if beam < len(row) and beam >= 0:
                beam_indexes.add(beam)

    
    return splits

def part_two(input):
    # Recursively travel down the beam "tree"
    # At each splitter, recurse left, then recurse right, counting the number
    # of splits

    beam_index = -1
    # Get starting beam pos
    for col, cell in enumerate(input[0]):
        if cell == "S":
            beam_index = col
    
    # Start recursion
    return quantum_beam(input, 0, beam_index)

CACHE = dict()
def quantum_beam(input, cur_row, cur_col):
    if cur_row == len(input):
        return 1

    if cur_col >= len(input[0]) or cur_col < 0:
        return 0

    if CACHE.get((cur_row, cur_col)) is not None: 
        return CACHE[(cur_row, cur_col)]

    if input[cur_row][cur_col] == "^":
        result = quantum_beam(input, cur_row + 1, cur_col - 1) + quantum_beam(input, cur_row + 1, cur_col + 1)
    else:
        result = quantum_beam(input, cur_row + 1, cur_col)
    
    CACHE[(cur_row, cur_col)] = result
    return result

def read_input(input_file):
    input = []
    with open(input_file, "r") as file:
        for line in file:
            input.append(list(line.strip()))

    return input

def main():
    input = read_input(INPUT_FILEPATH)
    print(part_one(input))
    print(part_two(input))

if __name__ == "__main__":
    main()