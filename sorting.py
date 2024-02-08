# To sort an array in ascending order
sheep = [3, 4, 5456, 34, 2324, 5463, 6756, 2534, 143, 435, 456]
sheep.sort()
print(sheep)

# sorting in descending order
sheep.sort(reverse=True)
print(sheep)

names = ['Laney', 'Samuel', 'Brenda', 'Josephat']
names.sort()
print(names)

# Custom sort (length of a string)
# lamda is function without a name
names.sort(key=lambda  x: len(x))
print(names)


