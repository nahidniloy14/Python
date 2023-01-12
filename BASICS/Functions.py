"""
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
