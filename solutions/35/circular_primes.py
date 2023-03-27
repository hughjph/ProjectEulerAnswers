import math

primes = [2]
circular_primes = [2]

def get_circle(num):
    rotations = []
    number_array = [int(x) for x in str(num)]
    rotations.append(num)
    for i in range(len(number_array) - 1):
        x = number_array[0]
        for j in range(len(number_array) - 1):
            number_array[j] = number_array[j+1]
        number_array[len(number_array) - 1] = x
        
        rotations.append(int(''.join(map(str,number_array))))
    return rotations

def check_if_all_prime(number_array):
    for number in number_array:
        if not is_prime(number):
            return False
    return True    

def is_prime(number):
    
    if number % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False

    if not primes.__contains__(number):
        primes.append(number)

    return True    

def start():
    for i in range(3, 1_000_001):
        if circular_primes.__contains__(i):
            continue
        number_array = get_circle(i)
        if check_if_all_prime(number_array):
            for number in number_array:
                if not circular_primes.__contains__(number):
                    circular_primes.append(number)


start()
print(circular_primes)
print(len(circular_primes))