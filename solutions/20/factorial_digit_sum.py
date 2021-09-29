import math

x = math.factorial(100)

y = str(x)

sum = 0
for i in range(len(y)):
    sum += int(y[i])

print(x)
print(sum)