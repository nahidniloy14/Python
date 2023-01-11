#TOSS
from random import randint

result=randint(1,2)
result
team1=input("Enter the name of home team:  ")
team2=input("Enter the name of away team:  ")
pick=input("Choose between head and tail: ")
if result==1 and pick=='head'or pick=='tail':
    print(f'{team1} won the toss')
else:
    print(f'{team2} won the toss')
    