import math

flag = False

a1 = 0
b1 = 0
c1 = 0

for a in range(1, 500):
    for b in range(a, 500):
        c = math.sqrt(a ** 2 + b ** 2)
        if (c % 2 == 0 or c % 2 == 1) and a + b + c == 1000:
            flag = True
            a1 = a
            b1 = b
            c1 = c
            break

    if(flag == True):
        break


print("a = " + str(a1))
print("b = " + str(b1))
print("c = " + str(c1))
print("product = " + str(a*b*c))