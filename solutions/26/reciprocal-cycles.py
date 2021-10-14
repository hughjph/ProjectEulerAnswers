max_p = 0
max = 0

for d in range (1, 1000):
    print(d)
    a = 1
    x = 0
    y = False
    while a!=1:
        a = a * 10 % d
        x += 1
        print(a)
        if a == 1:
            y = True
    if(max < x):
        max_p = d
        max = x
        print(max)
        print(max_p)

print(max_p)
print(max)
