import sys

def blink(stones : dict):
    new_stones = {}
    for stone in stones.keys():
        if stone == 0:
            new_stones[1] = new_stones.get(1, 0) + stones[stone]
        elif len(str(stone)) % 2 == 0:
            stone_l = int(str(stone)[:(len(str(stone)) // 2)])
            stone_r = int(str(stone)[(len(str(stone)) // 2):])
            new_stones[stone_l] = new_stones.get(stone_l, 0) + stones[stone] 
            new_stones[stone_r] = new_stones.get(stone_r, 0) + stones[stone] 
        else:
            new_stones[stone * 2024] = new_stones.get(stone * 2024, 0) + stones[stone]
            
    return new_stones

def process_stones(stones, num_blinks):
    for _ in range(1, num_blinks + 1):
        stones = blink(stones)
    
    num_stones = 0
    for stone in stones.values():
        num_stones += stone
        
    return num_stones

# { stone_num : num_appearences}
def make_dict(stone_list):
    stones = {}
    for stone in stone_list:
        stones[stone] = stones.get(stone, 0) + 1
    return stones

def read_input(input_file):
    with open(input_file, "r") as file:
        stones = list(map(int, file.read().strip().split(" ")))
    return stones

def main():
    stone_list = read_input(sys.argv[1])
    stones = make_dict(stone_list)
    num_stones = process_stones(stones, int(sys.argv[2]))
    print(f"Total stones: {num_stones}")
    
if __name__ == "__main__":
    main()