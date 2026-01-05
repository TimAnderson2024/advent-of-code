import sys

def sum_secret(secrets, x):
    sum = 0
    for secret in secrets:
        sum += calculate_secret(secret, x)
    return sum

def calculate_secret(secret, x):
    for _ in range(0, x):
        secret = calculate_next(secret)
    print(secret)
    return secret

def calculate_next(secret):
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, int(secret / 32)))
    return prune(mix(secret, secret * 2048))

def mix(secret, new):
    return new ^ secret

def prune(secret):
    return secret % 16777216

def read_input_file(file_name):
    with open(file_name, 'r') as file:
        input_numbers = list(int(line.strip()) for line in file)
    return input_numbers

def main():
    input_numbers = read_input_file(sys.argv[1])
    print(sum_secret(input_numbers, 2000))

if __name__ == "__main__":
    main()