# Hashset - you can search them in constant time
# Has no duplicates
mySet = set()

mySet.add(1)
mySet.add(32)
print(mySet)

print(len(mySet)) # checking the length

print(1 in mySet) # if something exist

mySet.remove(1)
print(mySet)


# List to set
print(set([343,234,43,4323]))

# Set comprehension
mySet = { i for i in range(8)}
print(mySet)