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
print(find_first_non_repeating_str("swiss"))

# count the number of vowels
def count_vowels(x):
    vowels = "aeiouAEIOU"
    return sum(1 for char in x if char in vowels) # 1 for each character
print(count_vowels("samuel wanyua "))

# check if two strings are anagrams
def are_anagrams(s1,s2):
    # solution 1
    # return sorted(s1) == sorted(s2)

    # solution 2
    # check if strings have the same length
    if len(s1) != len(s2):
        return False
    # initialize dictionaries
    count1,count2 = {},{}
    for char in s1:
        count1[char] = count1.get(char, 0) + 1
    for char in s2:
        count2[char] = count2.get(char,0) + 1
    return count1 == count2
print(are_anagrams("amss", "mass"))

# replace all spaces with %20
def replace_spaces(y):
    return y.replace(" ", "%20")
print(replace_spaces("samus kinutiha  jsdk ds s"))

# find the longest common prefix
def longest_common_prefix(strs):
    if not strs: # if the strs is empty
        return ""
    prefix = strs[0] # prefix is set to the first string in the list
    for s in strs[1:]: # iterate over remaining strings
        while s[:len(prefix)] != prefix and prefix: # s[:len(prefix)] != prefix checks if the extracted substring from s (s[:len(prefix)]) is not equal to the current prefix
            # and prefix - checks if 'prefix' is not an empty string
            prefix = prefix[:-1] # removing the last character
    return prefix

print(longest_common_prefix(["samm","sammanthing", "sammand"]))

# if a string contains digits
def is_digits_only(s):
    # solution 1
    # return s.isdigit()

    # solution 2
    return all(char.isdigit() for char in s) # The all() function returns True if all elements of the iterable are True. Otherwise, it returns False

    # solutin 3
    return s.isnumeric()
print(is_digits_only("dsj3dfkl"))

#  find all permutation of a string
from itertools import permutations
def strs_permutations(str):
    [''.join(p) for p in permutations(str)]

print(strs_permutations("samuel"))
