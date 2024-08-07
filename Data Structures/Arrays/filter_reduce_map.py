from functools import reduce

numbers = [1,3,4,5,6,3,2,4,5,6,3,4,6,7,4,3,3,46,6]
def add(x,y):
    return x + y
# reduce method
result = reduce(add, numbers)
print(result)

# filter method
def is_even(n):
    return n % 2 == 0
even_numbers = list(filter(is_even, numbers))
print(even_numbers)