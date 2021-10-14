x = 0
y = 1
index = 1


oneKdigits = False

while oneKdigits == False:
    z = x + y
    index+=1
    print(z)

    x = z

    if(len(str(x)) == 1000):
        oneKdigits = True

    if not oneKdigits:
        z = x + y
        index += 1
        print(z)
        y = z
        if(len(str(y)) == 1000):
            oneKdigits = True



print(index)
print(x)
print(y)
