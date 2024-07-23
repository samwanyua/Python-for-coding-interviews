s = 'Nebuchadnezzar'
# similar to arrays
print(s[2:7])

# strings are immutable (can't be changed)

# updating a string
s += 'adlksjafklj'
print(s) # creates a new string

# valid numeric strings can be converted
print(int('23423423') + int('234231435'))

# Converting numbers to strings
print(type(str(123)))

# converting strings to an array
# Using list() function
string_value = "Hello, World!"
array_result = list(string_value)
print(array_result)

# Getting ASCII value of a char
print(ord('a'))

# Combining a list of strings (with an empty string) delimitor
strings = ['ab', 'cd', 'ef']
print("".join(strings))

