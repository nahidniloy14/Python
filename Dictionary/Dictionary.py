customer={

    "Name":"Nahid Hassan Niloy",
     "Age":"26",
     "Email":"nahidniloy894@gmail.com"

}
print(customer)
#update
customer["DOB"]=["Jan 21,1996"]
print(customer)
customer["Name"]=["Jamil Ali"]
print(customer)

fruits={'banana':10,'grape':40,'orange':30,'apple':20,20:'apple','pineapple':50,'watermelon':60}
print(fruits['apple'])
print(fruits[20])

#insert
#add new dictionary
fruits={'banana':10,'grape':40,'orange':30,'apple':20,'pineapple':50,'watermelon':60}
fruits['date']='80'
print(fruits)
#keys and values
print(fruits.keys())
print(fruits.values())
#create dictionary at runtime
my_dic={}
my_dic["first name"]= "Nahid Hassan"
my_dic["last name"]= "Niloy"
print(my_dic)

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

"""
Convert two lists into a dictionary
"""
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1=dict(zip(keys,values))
print(dict1)

"""
Merge two dictionaries into one 
"""
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

"""
Retrive value from a dictionary
"""
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
value=sampleDict['class']['student']['marks']['physics']
print(value)

"""
Initialize dictionary with default values
"""
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["Kelly"])

"""
extract only mentioned keys
"""
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york" }
#
# keys = ["name", "salary"]
#
# newDict = {k: sampleDict[k] for k in keys}
# print(newDict)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# keys to extract
keys = ["name", "salary"]

# new dict
res = dict()

for k in keys:
    # add current key with its value from sample_dict
    res.update({k: sample_dict[k]})
print(res)

"""
Delete keys from dictionaries
"""
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]
for k in keys:
    sample_dict.pop(k)
print(sample_dict)

"""
check if a value is present in a list
"""
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in a dict')

"""
rename a key
"""
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

"""
Get the key of minimum value
"""
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(sample_dict, key=sample_dict.get))

"""
Change Value of keys
"""
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
sample_dict['emp3']['salary'] = 8500
print(sample_dict)