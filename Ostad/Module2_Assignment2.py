"""
Advanced-Data Structures and Comparison

Write a Python program that takes two sets from the user and computes their union, intersection, and difference.

A = {1, 2, 3, 4, 5}

B = {4, 5, 6, 7, 8}

"""

# Given sets (you can replace these or input your own)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)

# Union
union_set = A.union(B)
print("Union:", union_set)

# Intersection
intersection_set = A.intersection(B)
print("Intersection:", intersection_set)

# Difference (A - B)
difference_set = A.difference(B)
print("Difference (A - B):", difference_set)

# Difference (B - A)
difference_set_BA = B.difference(A)
print("Difference (B - A):", difference_set_BA)
