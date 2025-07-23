"""
Understanding Data Structures and Functions

Problem: 01

Write a function that takes two numbers as input and returns their average. Call the function with different values.

Problem: 02

Write a function that sorts a list of strings alphabetically.

["apple", "banana", "cherry", "kiwi", "grape"]

Problem: 03

Write a Python program that creates a new list containing only the duplicate elements from the given list: [1, 5, 6, 5, 1, 2, 3].

"""
#Problem 1
def average(num1, num2):
    return (num1 + num2) / 2

# Calling the function with different values
print("Average of 4 and 8:", average(4, 8))
print("Average of 10 and 20:", average(10, 20))
print("Average of -5 and 5:", average(-5, 5))


#Problem 2
def sort_strings(strings):
    return sorted(strings)

# Example list
fruits = ["apple", "banana", "cherry", "kiwi", "grape"]

# Sorting the list
sorted_fruits = sort_strings(fruits)
print("Sorted fruits:", sorted_fruits)

#Problem 3

def find_duplicates(input_list):
    seen = set()
    duplicates = set()
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# Given list
numbers = [1, 5, 6, 5, 1, 2, 3]

# Finding duplicates
duplicate_elements = find_duplicates(numbers)
print("Duplicate elements:", duplicate_elements)
