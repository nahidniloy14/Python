def square(num):
    result=num**2
"""
lamda function is used to convert the function in a easy manner

def square will be replaced by lamda keyword
return will be replaced by :

"""
square_num=lambda num: num**2
print(square_num(5))

#map( ) to lamda expression
"""
def num_square(num):
    return num**2
num=[1,2,3,4,5,6,7,8]
print(map(num_square,num))

lamda function>>
lamda num:num**2
map the functon>>
map(lambda num:num**2,num)
list the map>>
list(map(lambda num:num**2,num))
print the list>>
list(map(lambda num:num**2,num))
"""

num=[1,2,3,4,5,6,7,8]
print(list(map(lambda num:num**2,num)))

#filter( ) to lambda
"""
def even_check(num):
    return num%2==0
num_list=[11,22,33,44,55,66]

print(list(filter(even_check,num_list)))
"""
num=[1,2,3,4,5,6,7,8]
print(list(filter(lambda num:num**2==0,num)))