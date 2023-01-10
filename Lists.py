values=[1,4,"Niloy",29]
print(values[2] )#Niloy
fruits=['banana','grape','orange','apple','pineapple','watermelon']
len(fruits)
print(fruits[2:5]) #['orange', 'apple', 'pineapple']
price=['10','20','30','40','50','60']
print(fruits+price)
"""
['banana',
 'grape',
 'orange',
 'apple',
 'pineapple',
 'watermelon',
 '10',
 '20',
 '30',
 '40',
 '50',
 '60']
"""

#Update element
fruits=['banana','grape','orange','apple','pineapple','watermelon']
fruits[4]='date'
print(fruits)
#['banana', 'grape', 'orange', 'apple', 'date', 'watermelon']

#insert element to a particular index
info=["Nahid Hassan",26,2.98]
info.insert(1,"Niloy")
print(info)
# ['Nahid Hassan', 'Niloy', 26, 2.98]

#insert element to last
#append function
fruits=['banana','grape','orange','apple','pineapple','watermelon']
fruits.append('date')
print(fruits)
#['banana', 'grape', 'orange', 'apple', 'pineapple', 'watermelon', 'date']

#pop element from last
#pop function
fruits=['banana','grape','orange','apple','pineapple','watermelon']
fruits.pop()
print(fruits)
#['banana', 'grape', 'orange', 'apple', 'pineapple']

#pop element from index
fruits=['banana','grape','orange','apple','pineapple','watermelon']
fruits.pop(2)
print(fruits)
#['banana', 'grape', 'apple', 'pineapple', 'watermelon']

#delete element from index
fruits=['banana','grape','orange','apple','pineapple','watermelon']
del fruits[2]
print(fruits)
#['banana', 'grape', 'apple', 'pineapple', 'watermelon']

#sort in alphabetical order
fruits=['banana','grape','orange','apple','pineapple','watermelon']
fruits.sort()
print(fruits)
#['apple', 'banana', 'grape', 'orange', 'pineapple', 'watermelon']

#reverse elements
fruits=['banana','grape','orange','apple','pineapple','watermelon']
fruits.reverse()
print(fruits)
#['watermelon', 'pineapple', 'apple', 'orange', 'grape', 'banana']