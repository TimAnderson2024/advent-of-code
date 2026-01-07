RANGE_FILEPATH = "P5 - Cafeteria/input-ranges.txt"
INGREDIENT_FILEPATH = "P5 - Cafeteria/input-ingredients.txt"

class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high
    
    def __repr__(self):
        return f"[{self.low}, {self.high}]"

class Node:
    def __init__(self, interval):
        self.interval = interval
        self.max_high = interval.high
        self.left = None
        self.right = None
        
def insert(root: Node, interval: Interval):
    if root is None:
        return Node(interval)
    if interval.low < root.interval.low:
        root.left = insert(root.left, interval)
    else:
        root.right = insert(root.right, interval)
    
    if root.max_high < interval.high:
        root.max_high = interval.high
    
    return root

def is_overlapping(root: Node, point: int):
    if root is None:
        return False
    
    if root.interval.low <= point <= root.interval.high:
        return True
    
    if root.left is not None and root.left.max_high >= point:
        return is_overlapping(root.left, point)
    
    return is_overlapping(root.right, point)

def print_interval_tree(node, indent="", position="root"):
    if node is not None:
        print(f"{indent}[{position}] Interval: [{node.interval.low}, {node.interval.high}], max_high: {node.max_high}")
        print_interval_tree(node.left, indent + "    ", "L")
        print_interval_tree(node.right, indent + "    ", "R")

def demo_print_tree():
    ranges = read_ranges(RANGE_FILEPATH)
    root = None
    for r in ranges:
        root = insert(root, r)
    print_interval_tree(root)

def part_one(ranges, ingredients):
    root = None
    for range in ranges:
        root = insert(root, range)

    num_fresh = 0
    for ingredient in ingredients:
        if is_overlapping(root, ingredient):
            num_fresh += 1
    
    return num_fresh

def part_two(ranges):
    root = None
    for r in ranges:
        root = insert(root, r)
    
    num_fresh = 0
    sorted_intervals = inorder_traversal(root)
    combined_intervals = combine_intervals(sorted_intervals)

    for interval in combined_intervals:
        num_fresh += interval.high - interval.low + 1

    return num_fresh   

def combine_intervals(intervals):
    combo_interval = intervals[0]
    combined_intervals = []

    for current_interval in intervals[1:]:
        # If cur high overlaps with next low, merge
        if combo_interval.high >= current_interval.low:
            combo_interval.high = max(combo_interval.high, current_interval.high)
        else:
            combined_intervals.append(combo_interval)
            combo_interval = current_interval
    combined_intervals.append(combo_interval)
    
    return combined_intervals

def inorder_traversal(current_node: Node):
    # Returns a sorted list of intervals (by low)
    if current_node is None:
        return []
    return (
        inorder_traversal(current_node.left)
        + [current_node.interval]
        + inorder_traversal(current_node.right)
    )


def read_ranges(range_file):
    ranges = []
    with open(range_file, "r") as file:
        for line in file:
            lower, upper = line.strip().split("-")
            interval = Interval(int(lower), int(upper))
            ranges.append(interval)

    return ranges

def read_ingredients(ingredient_file):
    ingredients = []
    with open(ingredient_file, "r") as file:
        for line in file:
            ingredients.append(int(line.strip()))
    
    return ingredients

def main():
    ranges = read_ranges(RANGE_FILEPATH)
    ingredients = read_ingredients(INGREDIENT_FILEPATH)
    print(part_one(ranges, ingredients))
    # demo_print_tree()
    print(part_two(ranges))




if __name__ == "__main__":
    main()