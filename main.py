temp=int(input("Temparature in Celcius Today: "))
if temp>=30:
    print("Weather is hot")
elif temp<=20:
    print("Weateher is cold")
elif temp in range(20,30):
    print("Weather is moderate")
else:
    print("Invalid")

