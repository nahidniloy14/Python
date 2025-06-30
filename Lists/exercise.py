

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

"""
Reverse a String
"""
list1 = [100, 200, 300, 400, 500]
#method 1
list1.reverse()
print(list1)
#method 2
list1=list1[::-1]
print(list1)

"""
Concatenate Two lists
"""
#zip()
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

# For loop
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print(res)

"""
Square of list 
"""
numbers = [1, 2, 3, 4, 5, 6, 7]
square=[]
for i in numbers:
    square.append(i*i)
print(square)

"""
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

10 100
20 200
30 300
40 400
"""
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2 = list2[::-1]
print(list2)
for x, y in zip(list1, list2):
    print(x, y)
# for x, y in zip(list1, list2[::-1]):
#     print(x, y)

"""
Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
["Mike", "Emma", "Kelly", "Brad"]
"""

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)

"""
remove empty string
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"] >>
["Mike", "Emma", "Kelly", "Brad"]

"""
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)

"""
Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]>>
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
"""
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

"""
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
add sublist to existing list
"""
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

# understand indexing
# list1[2] = ['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
# list1[2][1] = ['d', 'e', ['f', 'g'], 'k']
# list1[2][1][2] = ['f', 'g']

# solution
list1[2][1][2].extend(sub_list)
print(list1)

"""
Write a program to find value 20 in the list, 
and if it is present, replace it with 200. Only update the first occurrence of an item.
list1 = [5, 10, 15, 20, 25, 50, 20]
"""

list1 = [5, 10, 15, 20, 25, 50, 20]
# get the first occurrence index
index = list1.index(20)
# update item present at location
list1[index] = 200
print(list1)


"""
remove 20 from the list 
list1 = [5, 20, 15, 20, 25, 50, 20]

"""
list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)
