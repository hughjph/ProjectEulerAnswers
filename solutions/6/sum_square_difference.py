sum_of_squares = 0
square_of_sum = 0


for i in range(1, 101):
     square_of_sum += i
     sum_of_squares += i ** 2

print(square_of_sum)
square_of_sum = square_of_sum ** 2

difference = square_of_sum - sum_of_squares

print(str(square_of_sum))
print(str(sum_of_squares))


print("the difference is " + str(difference))