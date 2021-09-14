j = 0
flag = False

last_prime = 1

for i in range(1, 10002):
    print(i)
    j = last_prime
    while True:
        j += 1

        flag = False
        for k in range(2, j):
            if j%k == 0 and j != k:
                flag = True
                break
        if flag == False:
            last_prime = j
            break


print(str(last_prime))