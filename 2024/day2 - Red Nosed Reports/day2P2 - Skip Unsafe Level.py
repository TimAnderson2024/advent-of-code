import sys

def remove_levels(report):
    for i, _ in enumerate(report):
        if is_safe(report[:i] + report[i+1:]):
            return True, i
    
    return False, -1

def is_safe(report):
    increasing = report[-1] > report[1]
    
    for i, num in enumerate(report[1:], start=1):
        prev = report[i-1]
        diff = num - prev

        if (increasing and (diff <= 0 or diff > 3)) or (not increasing and (diff >= 0 or diff < -3)):
            # print(f"Num {prev} to num {num} is illegal")
            return False
    
    return True
        
def process_reports(reports):
    num_safe = 0
    for report in reports:
        if is_safe(report):
            print(f"{report} is safe")
            num_safe += 1
        else:
            can_remove, i =  remove_levels(report)
            if can_remove:
                print(f"{report} is safe if {report[i]} is removed")
                num_safe += 1
            else:
                print(f"{report} is illegal")

    return num_safe

def read_input(input_file):
    reports = []
    with open(input_file, 'r') as file:
        for line in file:
            reports.append(list(map(int, line.strip().split(" "))))

    return reports

def main():
    reports = read_input(sys.argv[1])
    num_safe = process_reports(reports)
    print(num_safe)
    
if __name__ == "__main__":
    main()