#001
"""
Given an integer that can perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  2 to 5 , print Not Weird
If  is even and in the inclusive range of  6 to 20 , print Weird
If  is even and greater than , print Not Weird
"""
N = int(input().strip())

if N % 2 != 0:
    print ("Weird")
else:
    if N >= 2 and N <= 5:
        print ("Not Weird")
    elif N >= 6 and N <= 20:
        print ("Weird")
    elif N > 20:
        print ("Not Weird")
#002
"""
Take user input

weather : summer
Instruction : drink plenty of water
weather : winter
Instruction: wear warm clothes
"""
print("What type of weather is today?")
print("Choose Between 'cold' and 'hot ")
weather=input()

if weather=="cold":
    print("wear warm clothes")
elif weather=="hot":
    print("drink plenty of water")
else:
    print("It is a regular day")
#003
"""
No user input

weather : summer
Instruction : drink plenty of water
weather : winter
Instruction: wear warm clothes
"""
cold=True
hot=False
if cold:
    print("wear warm clothes")
elif hot:
    print("drink plenty of water")
else:
    print("It is a regular day")
#004
"""
Price of house is $10000
buyer has good credit: 10% discount
buyer has moderate credit: 20% discount

"""
credit_good = True
credit_moderate = False
house_price=10000
discountType1 = house_price- (500 * .1)
discountType2 = house_price- (500 * .2)
if credit_good:
    print(f'house price is {discountType1}')
elif credit_moderate:
    print(f'house price is {discountType2}')
else:
    print("Credit invalid")

"""
High Income + Good Credit : Eligble for Loan
Otherwise : Not eligble for Loan
"""

high_income=True
good_credit=True

if high_income and good_credit:
    print("Eligble for loadn")
else:
    print("Not eligble")

"""
tempartaure is higher than 30  :HOT
tempartaure is lower than 20  :Cold
tempartaure is between 20 and 30: moderate
"""

temp=int(input("Temparature in Celcius Today: "))
if temp>=30:
    print("Weather is hot")
elif temp<=20:
    print("Weateher is cold")
elif temp in range(20,30):
    print("Weather is moderate")
else:
    print("Invalid")

