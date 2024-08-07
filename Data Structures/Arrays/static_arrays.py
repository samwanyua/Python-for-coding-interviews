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
    return freq
print(x_func([3,3,4,5,6,7,4,3,4,5,2,3,4,6,7,4,4,4,5,2,4,5]))



