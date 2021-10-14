import math

a = -999
b = -1000
max_length = 0
aa = 0
bb = 0

while b <= 1000:
    print ("b " + str(b))
    while a < 1000:
        print("a " + str(a))
        nonPrimeFound = False
        n = 0
        length = 0
        while not nonPrimeFound:
            val = n**2 + a*n + b
            print(val)
            if (abs(val) % 2 != 0):
                j = 3
                print(math.sqrt(abs(val)))
                while j <= int(math.sqrt(abs(val)) + 1):

                    if (abs(val) % j == 0) and j != val:

                        nonPrimeFound = True
                        break
                    j += 2
                if(j >= int(math.sqrt(abs(val))+1)):
                    break

            else:
                nonPrimeFound = True
            length += 1
        n+=1
        if(length > max_length):
            max_length = length
            aa = a
            bb = b

        a += 1
    b+=1
    a = -999

print (aa*bb)
print(aa)
print(bb)
print(length)

