import sys

# Dict (Key : Numbers that can't appear before it)
# Iterate backwards through the update
# For each one, check if 0-cur contains an illegal value in dict

def check_update(update, rules):
    update = list(reversed(update))
    checked = [update[0]]
    for i, num in enumerate(update[1:]):
        print(num)
        for num2 in checked:
            if num in rules.get(num2, {}):
                print("Invalid Update")
                return False
        checked.append(num)
    print("Valid Update")
    return True


def run_update_list(update_list, rules):
    mid_sum = 0
    for update in update_list:
        print(update)
        if check_update(update, rules):
            print(update[int(len(update) / 2)])
            mid_sum += int(update[int(len(update) / 2)])
    return mid_sum
            

def read_input(input_file):
    with open(input_file, "r") as file:
        ordering_rules = {}
        update_list = []
        ordering, updates = file.read().strip().split("\n\n") 

        for line in ordering.split("\n"):
            num1, num2 = line.split("|")
            illegal = ordering_rules.get(num1, set())
            illegal.add(num2)
            ordering_rules[num1] = illegal
        
        for line in updates.split("\n"):
            update_list.append( list(line.split(",")))
            
    return ordering_rules, update_list

def main():
    rules, updates = read_input(sys.argv[1])
    print(rules)
    print("Total Score: ", run_update_list(updates, rules))
    
    
if __name__ == "__main__":
    main()