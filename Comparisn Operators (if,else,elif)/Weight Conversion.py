weight=int(input("Weight: "))
convType=input("Press 'L' to convert to pound or Press 'K' to convert to Kg\n")
if convType == 'K':
    conv = weight / 0.454
    print(f"Converted Weight: {conv} Kg")
else:
    conv = weight * 0.454
