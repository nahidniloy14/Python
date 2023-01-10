a="3.58"
print(type(a)) #<class 'str'>
b=3.58
print(type(b))#<class 'float'>
print("my cgpa is ",a)
#print("my cgpa is " +b) #can only concatenate str (not "float") to str
#if both the data types are different we have to concatenate
print("{}{}".format("My cgpa is ",b))
