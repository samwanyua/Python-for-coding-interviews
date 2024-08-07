# reverse string
name = "Joseph"
print(name[::-1])


# check if palindrome
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("amas"))

# slicing strings
s = "abcdefg"

# extract substring from index 1 to 4 (excluding 4)
sub1 = s[1:4] # "bcd"
# extract from beginning to index 3(excluding 3)
sub2 = s[:3] # "abc"
# extract from index 2 to the end
sub3 = s[2:] # "cdefg"
# extract entire string
sub4 = s[:] # "abcdefg"
# extract a string with a step of 2
sub5 = s[::2] # "aceg"
# extract the last 3 with negative index
sub6 = s[-3:] # "efg"
# reverse string
sub7 = s[::-1]

# find the first non-repeating character
def find_first_non_repeating_str(x):
    count = {} # hashmap
    for char in x:
        count[char] = count.get(char,0) + 1 # counting characters in a hashmap
    for char in x:
        if count[char] == 1:
            return char
    return None
