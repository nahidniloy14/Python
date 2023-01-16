"""
Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
["Mike", "Emma", "Kelly", "Brad"]
"""

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)

