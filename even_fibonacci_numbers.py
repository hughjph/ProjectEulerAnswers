x = 0
y = 1

total = 0

while (x <= 4000000) and (y <= 4000000):
    z = x + y
    print(z)

    if (z % 2 == 0):
        total += z

    x = z

    if (x <= 4000000) and (y <= 4000000):
        z = x + y
        print(z)

        if (z % 2 == 0):
            total += z
        y = z

print("TOTAL: " + str(total))
