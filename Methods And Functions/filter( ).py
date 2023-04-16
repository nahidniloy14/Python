"""
List
"""

"""
filter function filters out the moles and gives us our desired output
"""

def even_check(num):
    return num%2==0
num_list=[11,22,33,44,55,66]

print(list(filter(even_check,num_list)))