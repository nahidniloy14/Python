"""

"""
"""
#1 Generate a string of random 8 numbers
"""
import random
import string

def generate_string():
    lettter_digits=string.ascii_letters+string.digits
    return ''.join(random.choice(lettter_digits) for i in range(8))

print(generate_string())

"""
#2 Sum of series
"""
def sum_series(n,a,r):
    s=0
    for i in range(1,n+1):
        s+=a*(r**(i-1))

    return s
first_term=a=2
ratio=r=3
series=n=5

print(sum_series(n,a,r))

"""
Check a number if it is even or not
"""
#Method 1
def even_check(number):
    result=number%2==0
    return result
print(even_check(22))

# Method 2
def even_check(number):
    result=number%2==0
    return result
print(even_check(22))


"""
Write a function that will return true if it finds an even number in a list
"""
def even_number(number_list):
    for i in number_list:
        if i%2==0:
            return True
        else:
            pass
print(even_number([2,6,3]))


"""
Write a function that will return true if it finds an even number in a list and return the list
"""
def even_number(number_list):
    number=[]
    for i in number_list:
        if i%2==0:
           number.append(i)
        else:
            pass
    return number
print(even_number([12,16,77]))