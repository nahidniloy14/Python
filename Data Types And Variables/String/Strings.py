#use of single quotes
module='pyton'
print(module)


#use of double quotes
course="python's course for beginners"
print(course)#python's course for beginners
print(course[:])
print(course[-3]) #e
print(course[0:6]) #python
print(course[8:]) #course for beginners
print(course[:6]) #python

#use of 3 single quotes
email= '''  
Dear Sir,
Thank you for the oppurtunity

Regards,
Nahid Hassan Niloy
'''
print(email)

#String Methods
tutorial="Python String Methods"
print(len(tutorial))
print(tutorial.upper()) #PYTHON STRING METHODS
print(tutorial.lower()) #python string methods
# gives the index
print(tutorial.find('t'))
#replace string
print(tutorial.replace('String','Class'))
print('Python' in tutorial) #True
