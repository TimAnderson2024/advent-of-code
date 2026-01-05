import heapq
import sys

def calculate_diff(list1, list2):
    heapq.heapify(list1)
    heapq.heapify(list2)
    
    diff = 0
    while len(list1) > 0:
        diff += abs(heapq.heappop(list1) - heapq.heappop(list2))
    
    return diff
    

def read_input(input_file):
    list1, list2 = [], []
    with open(input_file, 'r') as file:
        for line in file:
            nums = line.strip().split("   ")
            print(nums)
            list1.append(int(nums[0]))
            list2.append(int(nums[1]))
    return list1, list2

def main():
    list1, list2 = read_input(sys.argv[1])
    diff = calculate_diff(list1, list2)
    print(diff)
    
if __name__ == "__main__":
    main()