import sys
import queue

def find_best_sequence(secret_list):
    sequences = {}
    
    for secret in secret_list:
        secret_prices = find_prices(secret)
        for sequence in secret_prices.keys():
            sequences[sequence] = sequences.get(sequence, 0) + secret_prices[sequence]
      
    print(sequences)
    max_key, max_value = max(sequences.items(), key=lambda item: item[1])

    print(max_key)  
    print(max_value) 
    return 0

def find_prices(secret):
    prev_price = secret % 10
    price_changes = queue.Queue()
    previous_sequences = set()
    sequence_bannanas = {}
    
    for i in range(0, 4):
        secret = calculate_next(secret)
        new_price = secret % 10
        price_changes.put(new_price - prev_price)
        prev_price = new_price


    for i in range(4, 2000):    
        price_seq = tuple(price_changes.queue)
        if price_seq not in previous_sequences:
            previous_sequences.add(price_seq)
            sequence_bannanas[price_seq] = new_price
            
        secret = calculate_next(secret)
        new_price = secret % 10
        price_changes.put(new_price - prev_price)
        price_changes.get()
        prev_price = new_price

    return sequence_bannanas

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
    find_best_sequence(input_numbers)
    
if __name__ == "__main__":
    main()