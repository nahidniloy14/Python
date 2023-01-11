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
