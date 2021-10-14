import time
coins = [1, 2, 5, 10, 20, 50, 100, 200]

ways = 1

i = 0
while True:
    print("coin index " + str(i))
    startingcoin = coins[i]
    if i == 7:
        break

    index = 6
    total = startingcoin
    while True:
        total=startingcoin


        while index > (i - 1):

            if (total + coins[index]) > 200:
                index -= 1
                print(" INDEX " + str(index))
                if(index == (i-1)):
                    break
            elif (total + coins[index]) == 200:
                total += coins[index]
                ways+=1
                print("WAYS: " + str(ways))
                break
            elif (total + coins[index]) < 200:
                total += coins[index]

        if(index == i):

            index -= 1
            break

    i += 1

print(ways)