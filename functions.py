# functions
def myFunc(n,m):
    return n * m

print(myFunc(3,4))

# Nested functions - have access to outer variables
def outerfunction (a,b):
    c = 'c'
    def innerfunction():
        return a + b + c
    return innerfunction()
print(outerfunction('a', 'b'))
    
# You can modify objects but not reassign unless using nonlocal keyword
def double(array, val):
    def helper():
        # Modifying array works
        for i, num in enumerate(array):
            array[i] *= 2

        # Modifying val works
        nonlocal val
        val *= 2

    # Call the helper function
    helper()
    print(array, val)

nums = [34, 23]
val = 78
double(nums, val)
