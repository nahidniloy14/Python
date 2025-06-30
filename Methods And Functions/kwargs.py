"""
kwargs
"""
"""
kwargs allows us to take as many input as we want
kwargs returns a dictioary and specified with two **
"""
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("My favourite food is {}".format(kwargs['fruit']))
    else:
        print("I did not find my food")
myfunc(fruit='apple',sour_fruit='grape',veg='carrot')
