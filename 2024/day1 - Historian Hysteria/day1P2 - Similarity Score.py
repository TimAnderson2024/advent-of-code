import sys
from collections import Counter

def calculate_similarity(list1, list2):
    right_list = Counter(list2)
    
    similarity = 0
    for num in list1:
        similarity += num * right_list[num]
    
    return similarity
    

def read_input(input_file):
    list1, list2 = [], []
    with open(input_file, 'r') as file:
        for line in file:
            nums = line.strip().split("   ")
            list1.append(int(nums[0]))
            list2.append(int(nums[1]))
    return list1, list2

def main():
    list1, list2 = read_input(sys.argv[1])
    similarity = calculate_similarity(list1, list2)
    print(similarity)
    
if __name__ == "__main__":
    main()