import sys

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.append(int(str(stone)[:(len(str(stone)) // 2)]))
            new_stones.append(int(str(stone)[(len(str(stone)) // 2):]))
        else:
            new_stones.append(stone * 2024)
    return new_stones

def process_stones(stones, num_blinks):
    for _ in range(1, num_blinks + 1):
        stones = blink(stones)

    return stones

def read_input(input_file):
    with open(input_file, "r") as file:
        stones = list(map(int, file.read().strip().split(" ")))
    return stones

def main():
    stones = read_input(sys.argv[1])
    stones = process_stones(stones, int(sys.argv[2]))
    print(f"Total stones: {len(stones)}")
    
if __name__ == "__main__":
    main()