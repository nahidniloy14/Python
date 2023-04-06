"""
Difference between return and print
"""
"""
Use print when you want to show a value to a human. return is a keyword. 
When a return statement is reached, Python will stop the execution of the current function, sending a value out to where the function was called. 
Use return when you want to send a value from one point in your code to another.
"""
# Print
def print_func(num1, num2):
    print(num1 + num2)


print_func(20, 10)

# Return
"""
In return statement we can store the value separately so that we can use it for other purposes
"""


def return_func(num1, num2):
    return num1 + num2


# print(return_func(10, 20))
result = return_func(10, 20)
print(result)


# Print & Result at a time

def add_num(num1, num2):
    print(num1 + num2)
    return num1 + num2


print(add_num(20, 30))
add_num(10, 20)
