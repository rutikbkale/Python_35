# WAP using lambda function to add number.

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(map(lambda x: x ** 2, numbers))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print("Original Numbers:", numbers)
print("Squared Numbers:", squared_numbers)
print("Even Numbers:", even_numbers)
print("Sum of Numbers:", sum_of_numbers)