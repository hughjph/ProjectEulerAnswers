import time

x = 600851475143

new_num = 0

base_val = 2
last_prime = 2
flag = False
falg = False

while True:

    while True:
        flag = False
        falg = False
        if (x % base_val != 0):

            print(x / base_val)
            last_prime = base_val
            while falg == False:
                flag = False

                base_val += 1

                print(base_val)

                for i in range(last_prime, base_val):

                    print(i)

                    if (base_val % i == 0) and base_val != i:
                        flag = True
                        break

                if (flag == False):
                    break

            print(base_val)
        else:
            print("a prime factor is " + str(base_val))
            time.sleep(3)
            break

    x = x / base_val

    if(x < 10):
        break

# answer is 6857