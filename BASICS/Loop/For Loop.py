
#For Loop
price=[10,25,65]
for i in price:
    i=i+1
    print(i)

#Nested For Loop
for x in range(3):
    for y in range(3):
        print(f'{x},{y}')
"""
Draw F alphabet using pattern
"""
num=[5,2,5,2,2]
# for count in num:
#     pattern=''
#     for count in range(count):
#         pattern=pattern+'x'
#     print(pattern)
for count in num:
    print('x'*count)

"""
Draw L alphabet using pattern
"""
num=[2,2,2,2,6]
for count in num:
    print('x'*count)

"""
Draw Pyraid Pattern Type 1
"""
num=int(input("Enter pyramid size: "))
for row in range(num): #row
    for column in range(num-row-1):
        print(" ",end="") #keeps the control in the same line
    for column in range(row+1):
        print('*',end=" ")
    print("\n")

"""
Draw Pyraid Pattern Type 2
"""
num=int(input("Enter pyramid size: "))
for row in range(num): #row
    for column in range(num-row-1):
        print(" ",end="") #keeps the control in the same line
    for column in range(row*2+1):
        print('*',end=" ")
    print("\n")

"""
Draw Reverse Pyraid Pattern 
"""
num=int(input("Enter pyramid size: "))
for row in range(num): #row
    for column in range(row+1):
        print(" ",end="") #keeps the control in the same line
    for column in range(num-row-1):
        print('*',end=" ")
    print("\n")

"""
Draw Pattern:
xxxx

xxxx

xxxx

xxxx
 
"""
for row in range(4):
    for column in range(4):
        print('x',end="")
    print("\n")
"""
Draw Pattern:
x

xx

xxx

xxxx

xxxxx

"""
for row  in range(5):
    for column in range(row+1):
        print('x',end="")
    print('\n')
"""
Draw Pattern:
xxxx

xxx

xx

x

"""
for row  in range(4):
    for column in range(4-row):
        print('x',end="")
    print('\n')

"""
 * 

      * * * 

    * * * * * 

  * * * * * * * 

* * * * * * * * * 

  * * * * * * *   

    * * * * *     

      * * *       

        *         

"""

for row_1 in range(5):
    for column in range(5-row_1-1):
        print(' ',end=" ")
    for column in range(row_1*2+1):
        print('*',end=" ")
    print('\n')
for row_2 in range(5):
    for column in range(row_2 + 1):
        print(' ', end=" ")
    for column in range(5- row_2*2+2):
        print('*',end=" ")
    for column in range(row_2 + 1):
        print(' ',end=" ")
    print('\n')

"""
Print first 10 numbers
"""
for num in range(5):
    print(num)

"""
Sum of all odd numbers from 10 to 20
"""
for num in range(11,20,2):
    print(num)

"""
user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
"""
num=int(input("Enter a Number: "))
sum=0
for i in range(0,num):
    #print(i)
    sum=sum+i
print(sum)

"""
Time Table
"""
num=int(input("Enter a number"))
for i in range(0,10):
    i+=1
    mul=i*2
    print(mul)
"""
Retrive value and reversed value from a list
"""
list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
list1.reverse()
print(list1)
# iterate reversed list
for item in new_list:
    print(item)
print("----------------")
for val in list1:
    print(val)

"""
print -10 to -1
"""
for i in range(-10,0):
    print(i)

"""
Prime numbers between 25,50
"""
for num in range(25, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

"""
Factorial of a number
"""
num = 5
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # run loop 5 times
    for i in range(1, num + 1):
        # multiply factorial by current number
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
