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

