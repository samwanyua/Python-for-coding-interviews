# Arrays (lists in python)

arr = [1,3,4,5]
print(arr)

# Dynamic arrays can be used as stack
arr.append(7)
print(arr)
arr.pop()
print(arr)

arr.insert(1, 34) # at index 1 you can insert a value
print(arr)

# read and reassign the value
arr[3] = 342
print(arr)

# intialize array of size n with default value of 1
n = 5
array = [1] * n
print(array) # [1, 1, 1, 1, 1]
print(len(array))
print(array[-1]) #reads the last value

# sublist (slicing an array)
numbers = [323,234,233,231,34,232,323]
print(numbers[1:3]) # [234, 233]

# non-inclusive
print(numbers[0:4]) # [323, 234, 233, 231]

# unpacking
d,f,g = [23,34,56]
print(d,f,g)

# looping through arrays
marks = [98,48,75,49]

# using index 
for i in range(len(marks)):
    print(marks[i])

# without index
for n in marks:
    print(n)

# with index and value
for j, k in enumerate(marks):
    print(j,k)

# looping through multiple arrays simultaneously with unpacking

age1 = [23,34,45,56,57,67,78,79]
age2 = [98,97,65,64,54,53,34,43]

for a1, a2 in zip (age1,age2):
    print(a1,a2)

# reversing an array
goats = [23,1,3,4,3,5,3,23,34]
goats.reverse()
print(goats)

