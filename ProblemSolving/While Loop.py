

"""
 Print 1 to 100
 """
i=1
while i<=100:
    print(i)
    i=i+1


"""
Number Guess
"""
secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("Guess: "))
    guess_count +=1
    if guess==secret_number:
        print("You Win")
        break
else:
    print("Sorry You Failed")

"""
Average Of 5 Numbers
"""
number_count=0
number_limit=3
total=0
while number_count<number_limit:
    number=int(input("Enter  a Number: "))
    number_count+=1
    total=total+number
print("Average: ",+total/number_limit)

"""
Printing the square of numbers
"""
count=0
limit=3
while limit>count:
    count=count+1
    number=int(input("Enter a Number: "))
    square=number*number
    print("Square:",+square)

