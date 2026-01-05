import sys
from collections import deque

class Block:
    # Constructor method
    def __init__(self, id, size, is_free):
        self.id = id
        self.size = int(size)
        self.is_free = is_free
    
    def __str__(self):
        status = "Free" if self.is_free else "Occupied"
        return f"Block(ID: {self.id}, Size: {self.size}, Status: {status})"

def print_disk(disk):
    formatted = ""
    for block in disk:
        for i in range(0, block.size):
            if block.id == -1:
                formatted += "."
            else:
                formatted += str(block.id)
    return formatted

def calculate_checksum(disk):
    cur_pos = 0
    checksum = 0
    
    for block in disk:
        for _ in range(0, block.size):
            if not block.is_free:
                checksum += block.id * cur_pos
            cur_pos += 1

    return checksum
    
def special_format_disk(file_blocks, disk):
    while len(file_blocks) > 0:
        cur_file = file_blocks.pop()
        
        for i, block in enumerate(disk):
            # Insert block 
            if block.is_free and block.size >= cur_file.size:
                block.size -= cur_file.size
                if block.size == 0:
                    del disk[i]
                disk.insert(i, cur_file)
                
                # Remove old file
                for j in range(len(disk) - 1, 0, -1):
                    # print(disk[j])
                    if disk[j].id == cur_file.id:
                        del disk[j]
                        new_free = Block(-1, cur_file.size, True)
                        disk.insert(j, new_free)
                        break
                                    
                break
    
    return disk
                

def generate_disk(map):
    file_blocks = []
    disk = []
    
    file_block = Block(0, map[0], False)
    file_blocks.append(file_block)
    disk.append(file_block)
    
    id = 1
    for i in range(1, len(map), 2):
        free_block = Block(-1, map[i], True)
        file_block = Block(id, map[i+1], False)
        
        disk.append(free_block)
        disk.append(file_block)
        file_blocks.append(file_block)

        id += 1
    
    return file_blocks, disk

def read_input(input_file):
    with open(input_file, "r") as file:
        return file.read().strip()

def main():
    map = read_input(sys.argv[1])
    file_blocks, disk = generate_disk(map)
    print_disk(disk)

    disk = special_format_disk(file_blocks, disk)
    print_disk(disk)
    
    checksum = calculate_checksum(disk)
    print(checksum)
    
if __name__ == "__main__":
    main()