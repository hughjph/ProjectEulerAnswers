import math

sum = 0

flag = False
last_i = 2

for i in range(2, 2000000):

    if(i%2 != 0):
        flag = False
        j = 3
        while j <= int(math.sqrt(i) + 1):
            if (i % j == 0) and j != i:
                flag = True
                break
            j += 2


        if flag == False:
            sum += i
            print("PRIME " + str(i))
            print("SUM " + str(sum))




print("SUM: " + str(sum + 2))