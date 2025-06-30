
"""
args
"""

"""
args allows us to take as many input as we want
It returns back a tuple to us
It is specified with *args
"""
def num(*args):
    return sum(args) * 0.5


print(num(1, 2, 3, 4, 5))


def tuple_num(*args):
    for item in args:
        print(item)

tuple_num(1, 2, 3, 4, 5)

