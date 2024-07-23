# Hashmaps(aka dict) - no duplicates
myMap = {}
myMap['Alice'] = 78
myMap['Bob']= 322
print(myMap)

# length
print(len(myMap))

# modifying hashmaps
myMap['Alice'] = 98789
print(myMap['Alice'])

# search for keys
print('Alice' in myMap)

# remove a key
myMap.pop('Alice')
print(myMap)

# Initializing a hashmap
myMap = { 'Kimani': 23422, 'Sarah': 234143343} # key values

# Dict comprehension
myMap = { i: 2 * i for i in range(5)} #i is key then 2*i is the value
print(myMap)

# Looping through a map
myMap = {'Jessica': 2342, 'Bob': 34453}
for key in myMap:
    print(key, myMap[key])

# looping through values
for val in myMap.values():
    print(val)

for key,val in myMap.items():
    print(key,val)