# if statements do not need parenthesis or curly braces
n = 1
if n > 4:
    n +=10
elif n == 2:
    n *=4
else:
    n +=3
print(n)

# Parathesis are needed for multi-line conditions
# and = &&
# or = ||

x,y = 34, 57
if ((x > 23 and x != y) or x == y):
    z = x + y
print(z)