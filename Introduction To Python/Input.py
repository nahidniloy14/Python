"""
Ask the user to enter a number. Then print whether it's:

Positive

Negative

Or Zero
"""

num=int(input("Enter a number: "))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
elif num==0:
    print("Zero")
else:
    print("Negative")


"""
Print Name & Favorite Color From user Input 
"""
name = input("What is your name: ")
color = input("What is your favourite color: ")
print(name  + 'likes' +  color)

