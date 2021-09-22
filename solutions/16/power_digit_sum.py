x = 2**1000
y = str(x)

sum = 0

for i in range(len(y)):
    sum += int(y[i])
    print(sum)