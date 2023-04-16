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

