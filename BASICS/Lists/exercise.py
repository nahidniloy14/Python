

"""
Maximum number from a list
"""
numbers=[5,10,20,30]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number
print(max)

"""
Sort 14,25,8,59,2,45 ascending and descending order
"""

num=[14,25,8,59,2,45]
num.sort()
print("ascending: ",num)
num.reverse()
print("descending:", num)

"""
Identify unique values in  a list
"""
num=[2,2,4,6,3,4,6,1]
unique=[]
for value in num :
    if value not in unique:
        unique.append(value)
print(unique)
