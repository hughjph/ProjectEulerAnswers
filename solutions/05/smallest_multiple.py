from __future__ import division

x = 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20

temp_x = 0
flag = False

print(x)

for i in range(20):
    i+=1
    print(i)
    if(i != 0):
        flag = False
        temp_x = x/i
        for j in range(20):
            j+=1
            if not (float(temp_x)%float(j) == 0):
                flag = True
                break

        if(flag == False):
            x = temp_x

print("Answer is " + str(x))