last_number = 100
range_number = range(1, last_number + 1)
sum_of_squares = sum(list(i**2 for i in range_number))
square_of_sum = sum(range_number)**2
print(square_of_sum - sum_of_squares)
