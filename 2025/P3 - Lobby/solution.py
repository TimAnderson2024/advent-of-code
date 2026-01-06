INPUT_FILEPATH = "P3 - Lobby/input.txt"

import heapq

def part_one(power_banks):
    total_power = 0

    for bank in power_banks:
        largest = int(bank[-2])
        second_largest = int(bank[-1])

        for val in reversed(bank[:-2]):
            if int(val) >= largest:                
                if second_largest < largest:
                    second_largest = largest
                
                largest = int(val)
        print(bank, int(f"{largest}{second_largest}"))
        total_power += int(f"{largest}{second_largest}")
    
    return total_power

def part_two(power_banks):
    total_power = 0

    for bank in power_banks:
        max_heap = []

        # Create initial heap with first n-12 elements
        for i, value in enumerate(bank[:-12]):
            heapq.heappush(max_heap, (-int(value), i))
        
        # Build solution while looping over last 12 elements
        solution = []
        left_bound = -1
        val, pos = heapq.heappop(max_heap)
        for i, new_val in enumerate(bank[-12:]):
            # Add new elem that couldn't be used before (because it was in last 12 positions)
            heapq.heappush(max_heap, (-int(new_val), len(bank) - 12 + i))

            # Pop until we get the greatest value that is to the right of our last chosen value
            while pos <= left_bound:
                val, pos = heapq.heappop(max_heap)
            solution.append(-val)
            left_bound = pos

        total_power += int("".join([str(x) for x in solution]))
    return total_power  

def read_input(input_file):
    power_banks = []
    with open(input_file, "r") as file:
        for line in file:
            power_banks.append(line.strip())
    
    return power_banks

def main():
    power_banks = read_input(INPUT_FILEPATH)
    print(part_one(power_banks))
    print(part_two(power_banks))


if __name__ == "__main__":
    main()