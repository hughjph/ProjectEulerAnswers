longest_chain = 0
number = 0


for i in range(2, 1000000):
    chain = 1
    n = i
    while n!=1:
        chain+=1
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    print(i)
    print(chain)
    if chain > longest_chain:
        longest_chain = chain
        number = i

print(str(number) + "   " + str(longest_chain))