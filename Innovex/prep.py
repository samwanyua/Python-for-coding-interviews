#  Lambda function - used for creating quick, one-off functions
#  syntax ->  lamba arguments: expression
add = lambda x,y: x + y

# filtering
numbers = [1,2,3,4,5,6]
even_numbers = list(filter(lambda x: x % 2 ==0, numbers))
print(even_numbers)

# reduce
from functools import reduce

result = reduce(lambda x,y: x + y, numbers)
print(result)

# map
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Sorting
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
sortedPairs = sorted(pairs, key = lambda pair : pair[1])
print(sortedPairs)

# exceptional handling
try:
    ans = 10 /0
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful")
finally:
    print("Execution completed")

# swapcase - converts uppercase characters to lowercase and vice versa
name = "Wanyua"
newName = name.swapcase()
print(newName)


for i in numbers:
    print(i)

y = 0
while i < 5:
    print(i)
    i+=1

#  list - ordered and mutable collection of items
myList = [1,3,4,5]

#  list comprehension - concise way of creating lists in python
#  syntax: [expression for item in iterable if condition]
squares = [x**2 for x in range(10)]
print(squares)

even_squares = [x**2 for x in range(100) if x % 2 == 0]
# print(even_squares)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
flattened = [element for row in matrix for element in row]
print(flattened)


words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
print(upper_words)

#  Tuple - ordered, immutable collection of items, contain duplicates
my_tuple = (3,2,4,5,3)
print(my_tuple)

# set - unordered collection of unique items
age = {3,4,5}
marks = set([2,3,4])

# dictionary - unordered, mutable, key-value pairs with unique keys
#  used for associating keys with values and fast lookups
my_dict={
    'name': 'sam',
    'role': 'Backend Developer',
    'company': 'Google'
}

employee = dict(name='Goshua', salary=45000)
print(employee.get('name'))
print(employee.get('age')) # None
print(employee.keys())
print(employee.values())
print(employee.items())
print(employee.update({'salary': '45000', 'salary': '60000'}))
print(employee.items())
print(employee.pop('salary'))
print(employee.items())
print(employee.popitem()) # removes and return the last key-value pair as a tuple

# passing function as arguments
def greet(name):
    return f"Hello, {name}"

def printMessage(messageFunction, name):
    message = messageFunction(name)
    print(message)

printMessage(greet, 'Innovex')

# *args - allows a function to accept any number of positional arguments
# arguments are passed as a tuple to the function

def print_nums(*args):
    for num in args:
        print(num)

print_nums(1,2,3,4,5,6,7)

# **kwargs - allows a function to accept any number of keyword arguments
# arguments are passed as dictionary where keys are argument names, values are argument values
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Wanyua", role="Backend Developer", company="Innovex")

# local scope -scope inside a function
def func():
    local_var =10
    print(local_var) # local variable, accessed only here
func()

# Enclosing scope - scope of any enclosing function, used in nested functions
def outer_function():
    outer_var = 'outer'
    def inner_function():
        inner_var = 'inner'
        print(outer_var) # accessible here

    inner_function()
outer_function()


#  Global scope - accessible throughout the module
global_var = 'global'
def my_function():
    print(global_var)
my_function()

# modifying global variables
cout = 0
def increment():
    global cout
    cout +=1
increment()
print(cout)

# Built in scope - example; functions, exceptions
print(len([1,2,3,4,5,6,67,8,8,5,4,3,4,5]))

# Scope resolution(LEGB rule)
'''
Python resolves names using LEGB RULE:
    - Local
    - Enclosing
    - Global
    - Built-in
'''

# Docstring 
'''
- is a string literal used to document modules, functions, classes and methods
- enclosed in "..." or '...'
- provide convenient way of associating documentation with python code
'''

# single line docstrings
def addTwoNumbers(a,b):
    """Add two numbers."""
    return a + b
print(addTwoNumbers.__doc__)

addThreeNumbers = lambda x,y,z: x + y + z
print(addThreeNumbers(45,45,45))

# dict comprehension - concise way of creating dictionaries
nums = [1,2,3,4,5]
square = {num : num **2 for num in nums}
print(square.items())

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Nairobi']
person_details = {key : value for key, value in zip(keys,values)}
print(person_details)

# shallow copy
# Copies the outer container but not the contents inside. 
# Changes to inner elements affect both the original and the copy.

import copy
original_list = [1,[2,3],4]
shallow_copy = copy.copy(original_list)
shallow_copy[1][0] = 'changed'
print(original_list)
print(shallow_copy)

# deep copy
# Copies everything, including contents inside the outer container. 
# Changes to the copy do not affect the original.
original = [1,[3,4],7]
deep_copy = copy.deepcopy(original)
deep_copy[1] [0] = 'changed'
print(original)
print(deep_copy)

# sort() function - sorts list in place
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
nums.sort()
print(nums)

# sorted() - returns new sorted list
sorted_nums = sorted(nums)
print(sorted_nums)


# decorators - powerful and flexible way to modify the behavior of functions or methods
# how they work - takes another function as an argument and returns a new function that typically extends the behavior of the original function.
'''
syntax

@decorator
def function_to_decorate():
    pass
    

it's a shortform of
function_to_decorate() = decorator(function_to_decorate)
'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening before the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("hello")
say_hello()


# iterators - allow you to traverse through all the elements of a collection (such as a list or tuple) one element at a time.
my_list = [1,2,3,4,5,6,7]

my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

'''
Encapsulation - hides internal details of a class from external access

public class Person{
    private String name;
    private int age;

    // public method to get name
    public String getName(){
        return name;
    }

    // public method to set name
    public void setName(String name){
        this.name = name;
    }

    // public method to get age
    public int getAge(){
        return age;
    }

    // public method to set age
    public void setAge(int age){
        if(age > 0){
            this.age = age;
        }
        else{
            this.age = age;
        }
    }
}

Abstraction - hiding the complex details and showing only the necessary parts

abstract class Shape{
    abstract double area;
    abstract double perimeter;
}

class Rectangle extends Shape{
    private double width;
    private double length;

    public Rectangle(double width, double length){
        this.width = width;
        this.length = length;
    }

    @override
    double area(){
        return width * length;
    }

    @override
    double perimeter(){
        return 2 * (width + length);
    }
}

public class Main{
    public static void main(String[] args){
        Shape rectangle = new Rectangle(4,5);
        System.out.println(rectangle.area());
    }
}





'''