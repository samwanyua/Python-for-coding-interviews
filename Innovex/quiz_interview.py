"""
Given a string word and a character ch, write a function transformWord that transforms the string in the following way:

Find the first occurrence of the character ch in the string word.
If ch is not found in the string, return the original string word.
If ch is found, reverse the substring from the start of word to the first occurrence of ch (inclusive), and concatenate this reversed substring with the remainder of the string.
Return the resulting transformed string.
Example:

Input: word = "abcdefga", ch = "d"
Output: "dcbafga"
Input: word = "advb", ch = "z"
Output: "advb"
Constraints:

The function should handle both lowercase and uppercase letters.
The length of word can be up to 1000 characters.
"""


def solution(word, ch):
    index = -1
    for i in range(len(word)):
        if word[i] == ch:
            index = i
            break
    #     if ch is not found
    if index == -1:
        return word
    else:
        first_part = word[:index + 1]
        first_part = first_part[::-1]
        second_part = word[index + 1:]
        return first_part + second_part


print(solution("abcdef", "c"))

s = "abcdefg"

# Extract substring from index 1 to 4 (excluding 4)
sub1 = s[1:4]  # "bcd"

# Extract substring from the beginning to index 3 (excluding 3)
sub2 = s[:3]  # "abc"

# Extract substring from index 2 to the end
sub3 = s[2:]  # "cdefg"

# Extract the entire string
sub4 = s[:]  # "abcdefg"

# Extract substring with a step of 2
sub5 = s[::2]  # "aceg"

# Extract substring with negative indices
sub6 = s[-3:]  # "efg"

# Reverse the string
sub7 = s[::-1]  # "gfedcba"

