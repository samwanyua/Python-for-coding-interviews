# static arrays
a = [1,2,3,4,5]
print(a[3]) # O(1)
print(3 in a) # look for a given value, O(n)

# insertion -> O(n)
# deletion -> O(n)

# dynamic arrays : lists
# we don't have static arrays in python
def x_func(b):
    freq ={}
    for n in b:
        freq[n] = freq.get(n,0) + 1
    freq2 = {x: freq[x] for x in freq}
    freq3 = dict(sorted(freq.items(), key=lambda item : item[1]))
    return freq2, freq3
print(x_func([3,3,4,5,6,7,4,3,4,5,2,3,4,6,7,4,4,4,5,2,4,5]))

# sorting lists
# sorted() function returns a new list that is sorted, leaving original list unchanged
my_list = [4,2,9,1,5,6]
sorted_list = sorted(my_list)
sorted_list2 = sorted(my_list, reverse=True)
print(my_list)
print(sorted_list2)

# list.sort() -> sorts the list in place and modifies the original list, returns None
marks = [ 3,4,5,3,2,56,5,3,23,4,323,234]
marks.sort()
print(marks)

# sorting a tuple
my_tuple = (3,2,4,5,2)
# convert to list, sort and convert back to tuple
sorted_tuple = tuple(sorted(my_tuple))
print(sorted_tuple)

# sort a dictionary
my_dict = {'banana': 3, 'apple': 1, 'cherry': 2}
# sort by keys
sort_by_keys = {x: my_dict[x] for x in sorted(my_dict)}
print(sort_by_keys)

# sort by values
sort_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sort_by_values)
