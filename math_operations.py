# Division is decimal by default
print(5/2)

#  Double slash rounds down
print(9 // 2)

# most languages round towards 0 by default so negative numbers will round down
print(-3 // 2) # output is -2

# A workaround for rounding towards zero is to use decimal division the convert to int
print(int(-7/2)) # output is -3

# Modulus
print(10 % 3) # 1

# Ecept for negative values
print(-10 % 3) # 2

# To be consistent
import math
print(math.fmod(-10,3)) # -1.0

# Floor - round down
print(math.floor(7/2))
# round up
print(math.ceil(7/2))
# squareroot
print(math.sqrt(2))
# power
print(math.pow(7,2))


# max/min int
float('inf') #max
float('-inf') #min
# Example: Finding the maximum and minimum values in a list
numbers = [5, 8, 2, 10, 3, 15]

# Initialize max_value and min_value with infinity and negative infinity
max_value = float('-inf')
min_value = float('inf')

# Sample list of integers
numbers = [5, 8, 2, 10, 3, 15]

# Finding the maximum and minimum values
max_value = max(numbers)
min_value = min(numbers)

# python numbers are infinite so they never overflow
import math
print(math.pow(3,200))

# Checking if it is less than infinity
print(math.pow(3,300) < float('inf'))

# Convert int to array
integer_value = 12345
array_result = list(map(int, str(integer_value)))

print(array_result)

