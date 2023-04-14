



def check_even_list(number_list):
    even_number=[]
    for number in number_list:
        if number%2==0:
           even_number.append(number)
        else:
            pass
    return even_number
print(check_even_list([12,11,33]))
