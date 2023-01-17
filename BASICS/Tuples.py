"""
Tuples are very simmilar to list.Once an elemenet is assigned inside a touple,
it can not be reassigned.For example,fruits[5]='banana' will cause syntax error.
Touple is useulf when we don't want our program to change any values.
"""
numbers=(11,52,44,85,85)
print(numbers.count(85)) #2 repeatation
print(len(numbers)) #5
print(type(numbers)) #tuple
print(numbers.index(52)) #1 index

"""
Reverse a tuple
"""
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)

"""
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))>>
20
"""
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

"""
Write a program to unpack the following tuple into four variables and display each variable.
tuple1 = (10, 20, 30, 40)
"""
tuple1 = (10, 20, 30, 40)
(a,b,c,d) =tuple1
print(a)

"""
Swap values in python
"""
tuple1 = (11, 22)
tuple2 = (99, 88)

#tuple1[0],tuple1[1]=tuple2[0],tuple2[1]
tuple1,tuple2=tuple2,tuple1
print("tuple1:",tuple1)
print("tuple2:",tuple2)

"""
Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
"""
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2=(tuple1[3],tuple1[4])
print(tuple2)
"""
 Write a program to modify the first item (22) of a list inside a following tuple to 222
"""
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)