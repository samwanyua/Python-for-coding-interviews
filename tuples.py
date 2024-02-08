# tupples are like lists but immutable
tup = (56,54,34,32)
print(tup)
print(tup[0])
print(tup[-1])

# tuples are used as keys for hashmaps or hashsets
myMap = {(2,23): 3}
print(myMap[(2,23)])
print(myMap)

mySet = set()
mySet.add((1,3))
print((1,3) in mySet)

# lists can't be keys for hashmaps or hashsets

