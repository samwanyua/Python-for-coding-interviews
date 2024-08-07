# reverse string
name = "Joseph"
print(name[::-1])


# check if palindrome
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("amas"))
