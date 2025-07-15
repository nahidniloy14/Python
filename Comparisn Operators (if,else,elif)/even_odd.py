"""
Ask the user to enter a number. Then print whether it is even or odd.
"""
num=int(input("Enter a number: "))
if num%2==0:
    print(num,"is an even number.")
elif num%2==1:
    print(num,"is an odd number.")
else:
    print("Invalid input.")
