import sys

def try_operations(equation):
    target = equation[0]
    cur_results = {equation[1]}
    for num in equation[2:]:
        next_results = set()
        for cur_result in list(cur_results):
            next_results.add(cur_result * num)
            next_results.add(cur_result + num)
        cur_results = next_results
    
    if target in cur_results:
        return True
    
    return False

def calculate_calibration(equations):
    sum = 0
    for equation in equations:
        if try_operations(equation):
            print("Legal Equation")
            sum += equation[0]
        else:
            print("Illegal Equation")
    return(sum)

def read_input(input_file):
    equations = []
    with open(input_file, "r") as file:
        for line in file:
            total, components = line.split(":")
            equations.append([int(total)] + list(map(int, list(components.strip().split(" ")))))
    return equations
    
def main():
    equations = read_input(sys.argv[1])
    print(calculate_calibration(equations))
    
if __name__ == "__main__":
    main()