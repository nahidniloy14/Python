"""
Problem: 01

Write a Python program that takes a number as input and checks whether it is even or odd.



Problem: 02

 Write a program that takes two numbers and an operator (+, -, *, /) and performs the calculation.



Problem: 03

Write a program using a for loop that calculates the sum of even numbers between 1 and 100.

"""

# Problem 01
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
# Problem 02
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")
# Problem 03
total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total += i

print("Sum of even numbers from 1 to 100 is:", total)
