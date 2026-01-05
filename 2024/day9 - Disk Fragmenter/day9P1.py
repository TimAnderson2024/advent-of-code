import sys

def calculate_checksum(disk):
    cur_pos = 0
    checksum = 0
    while disk[cur_pos] != '.':
        # print(cur_pos * disk[cur_pos])
        checksum += cur_pos * disk[cur_pos]
        cur_pos += 1
        
    return checksum

def update_pointers(l, r, disk):
    while disk[l] != '.':
        l += 1
    while disk[r] == '.':
        r -= 1
    
    return l, r
    
def format_disk(disk):
    l = 0
    r = len(disk) - 1
    
    l, r = update_pointers(l, r, disk)
    
    while l < len(disk) and r >= 0 and l < r:
        disk[l] = disk[r]
        disk[r] = '.'
        l, r = update_pointers(l + 1, r - 1, disk)
        # print(disk)
    
    return disk

def generate_disk(map):
    disk = [0] * int(map[0])
    id = 1
    for i in range(1, len(map), 2):
        free_block = ['.'] * int(map[i])
        file = [id] * int(map[i+1])
        disk = disk + free_block + file
        id += 1
    return disk  

def read_input(input_file):
    with open(input_file, "r") as file:
        return file.read().strip()

def main():
    map = read_input(sys.argv[1])
    disk = generate_disk(map)
    disk = format_disk(disk)
    print(calculate_checksum(disk))
    
if __name__ == "__main__":
    main()