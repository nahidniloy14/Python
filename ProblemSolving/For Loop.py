
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