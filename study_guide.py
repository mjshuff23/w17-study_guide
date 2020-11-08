# WEEK 17 Study Guide - Run lines of code by highlighting then running in code runner extension

# The None Value
# None is the same as null in JS.  It represents the lack of existence of a value
# Must be used with a capital letter, funcs that don't have an explicit return return None


def say_hi(name):
    """<---- Multi-Line Comments and Docstrings
    This is where you put your content for help() to inform the user
    about what your function does and how to use it
    """
    print(f"Hello {name}!")


print(say_hi("Michael"))  # Should get the print inside the function, then None

# Boolean Values
# Work the same as in JS, except they are title case: True and False
a = True
b = False

# Logical Operators
# ! = not, || = or, && = and
print(True and True)
print(True and not True)
print(True or True)

# Truthiness - Everything is True except...
# False - None, False, '', [], (), set(), range(0)

# Number Values
# Integers are numbers without a floating decimal point
print(type(3))  # type returns the type of whatever argument you pass in
# Floating Point values are numbers with a floating decimal point
print(type(3.5))

# Type Casting
# You can convert between ints and floats (along with other types...)
print(float(3))  # If you convert a float to an int, it will truncate the decimal
print(int(4.5))
print(type(str(3)))
# Python does not automatically convert types like JS
# print(17.0 + ' heyooo ' + 17)  # TypeError

# Arithmetic Operators
# ** - exponent (comparable to Math.pow(num, pow))
# // - integer division
# There is no ++ or -- in Python

# String Values
# We can use single quotes, double quotes, or f'' for string formats
# We can use triple single quotes for multiline strings
print(
    """This here's a story
All about how
My life got twist
Turned upside down
"""
)

# Three double quotes can also be used, but we typically reserve these for
# multi-line comments and function docstrings (refer to lines 6-9)(Nice :D)
# We use len() to get the length of something
print(len("Michael"))  # 7 characters
print(len(["hey", "ho", "hey", "hey", "ho"]))  # 5 list items
print(len({1, 2, 3, 4, 5, 6, 7, 9}))  # 8 set items

# We can index into strings, list, etc..self.
name = "Michael"
for i in range(len(name)):
    print(name[i])  # M, i, c, h, a, e, l

# We can index starting from the end as well, with negatives
occupation = "Full Stack Software Engineer"
print(occupation[-3])  # e

# We can also get ranges in the index with the [start:stop:step] syntax
print(occupation[0:4:1])  # step and stop are optional, stop is exclusive
print(occupation[::4])  # beginning to end, every 4th letter
print(occupation[4:14:2])  # Let's get weird with it!
# NOTE: Indexing out of range will give you an IndexError

# We can also get the index og things with the .index() method, similar to indexOf()
print(occupation.index("Stack"))
print(["Mike", "Barry", "Cole", "James", "Mark"].index("Cole"))

# We can count how many times a substring/item appears in something as well
print(occupation.count("S"))
print(
    """Now this here's a story all about how
My life got twist turned upside down
I forget the rest but the the the potato
smells like the potato""".count(
        "the"
    )
)

# We concatenate the same as Javascript, but we can also multiply strings
print("dog " + "show")
print("ha" * 10)

# We can use format for a multitude of things, from spaces to decimal places
first_name = "Michael"
last_name = "Shuff"
print("Your name is {0} {1}".format(first_name, last_name))

# Useful String Methods
print("Hello".upper())  # HELLO
print("Hello".lower())  # hello
print("HELLO".islower())  # False
print("HELLO".isupper())  # True
print("Hello".startswith("he"))  # False
print("Hello".endswith("lo"))  # True
print("Hello There".split())  # [Hello, There]
print("hello1".isalpha())  # False,  must consist only of letters
print("hello1".isalnum())  # True, must consist of only letters and numbers
print("3215235123".isdecimal())  # True, must be all numbers
# True, must consist of only spaces/tabs/newlines
print("       \n     ".isspace())
# False, index 0 must be upper case and the rest lower
print("MichaeL".istitle())
print("Michael Lee".istitle())  # True!

# Duck Typing - If it walks like a duck, and talks like a duck, it must be a duck
# Assignment - All like JS, but there are no special keywords like let or const
a = 3
b = a
c = "heyoo"
b = ["reassignment", "is", "fine", "G!"]

# Comparison Operators - Python uses the same equality operators as JS, but no ===
# < - Less than
# > - Greater than
# <= - Less than or Equal
# >= - Greater than or Equal
# == - Equal to
# != - Not equal to
# is - Refers to exact same memory location
# not - !
# Precedence - Negative Signs(not) are applied first(part of each number)
#            - Multiplication and Division(and) happen next
#            - Addition and Subtraction(or) are the last step
#  NOTE: Be careful when using not along with ==
print(not a == b)  # True
# print(a == not b) # Syntax Error
print(a == (not b))  # This fixes it. Answer: False
# Python does short-circuit evaluation

# Assignment Operators - Mostly the same as JS except Python has **= and //= (int division)

# Flow Control Statements - if, while, for
# Note: Python smushes 'else if' into 'elif'!
if 10 < 1:
    print("We don't get here")
elif 10 < 5:
    print("Nor here...")
else:
    print("Hey there!")

# Looping over a string
for c in "abcdefgh":
    print(c)

# Looping over a range
for i in range(5):
    print(i + 1)

# Looping over a list
lst = [1, 2, 3, 4]
for i in lst:
    print(i)

# Looping over a dictionary
spam = {"color": "red", "age": 42, "items": [(1, "hey"), (2, "hooo!")]}
for v in spam.values():
    print(v)

# Loop over a list of tuples and destructuring the values
# Assuming spam.items returns a list of tuples each containing two items (k, v)
for k, v in spam.items():
    print(f"{k}: {v}")

# While loops as long as the condition is True
#  - Exit loop early with break
#  - Exit iteration early with continue
spam = 0
while True:
    print("Heyy girrllll")
    spam += 1
    if spam < 5:
        continue
    break


# Functions - use def keyword to define a function in Python
def printCopyright():
    print("Copyright 2020, ya boi, Mike Shuff")


# Lambdas are one liners! (Should be at least, you can use parenthesis to disobey)
avg = lambda num1, num2: print(num1 + num2)

avg(1, 2)
# Calling it with keyword arguments, order does not matter
avg(num2=20, num1=1252)
printCopyright()

# We can give parameters default arguments like JS
def greeting(name, saying="Hello"):
    print(saying, name)


greeting("Mike")  # Hello Mike
greeting("Michael", saying="Hello there...")

# A common gotcha is using a mutable object for a default parameter
# All invocations of the function reference the same mutable object
def append_item(item_name, item_list=[]):  # Will it obey and give us a new list?
    item_list.append(item_name)
    return item_list


# Uses same item list unless otherwise stated which is counterintuitive
print(append_item("notebook"))
print(append_item("notebook"))
print(append_item("notebook", []))

# Errors - Unlike JS, if we pass the incorrect amount of arguments to a function,
#          it will throw an error
# avg(1)  # TypeError
# avg(1, 2, 2) # TypeError

# ----------------------------------- DAY 2 ----------------------------------------
# Functions - * to get rest of position arguments as tuple
#           - ** to get rest of keyword arguments as a dictionary
# Variable Length positional arguments
def add(a, b, *args):
    # args is a tuple of the rest of the arguments
    total = a + b
    for n in args:
        total += n
    return total


print(add(1, 2))  # args is None, returns 3
print(add(1, 2, 3, 4, 5, 6))  # args is (3, 4, 5, 6), returns 21

# Variable Length Keyword Arguments
def print_names_and_countries(greeting, **kwargs):
    # kwargs is a dictionary of the rest of the keyword arguments
    for k, v in kwargs.items():
        print(greeting, k, "from", v)


print_names_and_countries(
    "Hey there", Monica="Sweden", Mike="The United States", Mark="China"
)

# We can combine all of these together
def example2(arg1, arg2, *args, kw_1="cheese", kw_2="horse", **kwargs):
    pass


# Lists are mutable arrays
empty_list = []
roomates = ["Beau", "Delynn"]
# List built-in function makes a list too
specials = list()
# We can use 'in' to test if something is in the list, like 'includes' in JS
print(1 in [1, 2, 4])  # True
print(2 in [1, 3, 5])  # False

# Dictionaries - Similar to JS POJO's or Map, containing key value pairs
a = {"one": 1, "two": 2, "three": 3}
b = dict(one=1, two=2, three=3)
# Can use 'in' on dictionaries too (for keys)
print("one" in a)  # True
print(3 in b)  # False

# Sets - Just like JS, unordered collection of distinct objects
bedroom = {"bed", "tv", "computer", "clothes", "playstation 4"}
# bedroom = set("bed", "tv", "computer", "clothes", "playstation 5")
school_bag = set(
    ["book", "paper", "pencil", "pencil", "book", "book", "book", "eraser"]
)
print(school_bag)
print(bedroom)
# We can use 'in' on sets as wel
print(1 in {1, 2, 3})  # True
print(4 in {1, 3, 5})  # False

# Tuples are immutable lists of items
time_blocks = ("AM", "PM")
colors = "red", "green", "blue"  # Parenthesis not needed but encouraged
# The tuple built-in function can be used to convert things to tuples
print(tuple("abc"))
print(tuple([1, 2, 3]))
# 'in' may be used on tuples as well
print(1 in (1, 2, 3))  # True
print(5 in (1, 4, 3))  # False

# Ranges are immutable lists of numbers, often used with for loops
#   - start - default: 0, first number in sequence
#   - stop - required, next number past last number in sequence
#   - step - default: 1, difference between each number in sequence
range1 = range(5)  # [0,1,2,3,4]
range2 = range(1, 5)  # [1,2,3,4]
range3 = range(0, 25, 5)  # [0,5,10,15,20]
range4 = range(0)  # []
for i in range1:
    print(i)

# Built-in functions:
# Filter
isOdd = lambda num: num % 2 == 1


filtered = filter(isOdd, [1, 2, 3, 4])
for num in filtered:
    print(f"first way: {num}")
print("--" * 20)
[print(f"list comprehension: {i}") for i in [1, 2, 3, 4, 5, 6, 7, 8] if i % 2 == 1]
