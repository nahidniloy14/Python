"""
Digit To Text
"""
phone=input("Enter Phone: ")
digit={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five"

}
output=""
for i in phone:
    output=output+digit.get(i) + " "
print(output)
