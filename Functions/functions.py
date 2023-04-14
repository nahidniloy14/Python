"""
FUNCTION
"""
"""
Functions allows us to create blocks of code that can be easily executed many times without needing to rewrite the block of code
def name_of_function():
def is the keyword to identify this as a function
We use snake casing to write a function.
Snake casing is all small letters with underscore between this to call a function we must use the paranthesis 
"""


#NON PARAMETERIZED
"""
def greet():
    print("Hello,Good Morning")
    print("Welcome To Dhaka")    
greet()

"""

#PARAMETERIZED
"""
def greet(name):
    print("Hello,Good Morning !!!")
    print(f"Welcome To Dhaka {name}")
greet("Niloy")
greet("John")
"""


#Using default value as a parameter
def greet(name):
    print(f'Hello!! good morning {name}')

greet('Abbas')

def greet(name='abcxyz'):
    print(f'Hello!! good morning {name}')

greet()

# Positional Argument
"""
def greet(f_name,l_name):
    print("Hello,Good Morning !!!")
    print(f"Welcome To Dhaka {f_name} {l_name}")
greet("Nahid Hassan","Niloy")

"""

# Keyword Argumet
def greet(f_name,l_name):
    print("Hello,Good Morning !!!")
    print(f"Welcome To Dhaka {f_name} {l_name}")

greet(f_name="Nahid Hassan",l_name="Niloy")


#return statement
def square(num):
    return num*num

print(square(2))


