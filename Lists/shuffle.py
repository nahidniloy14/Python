my_list = [14, 6, 7, 9, 12]
from random import shuffle

# Method 1
shuffle(my_list)

print(my_list)


# Method 2
def shuffle_func(shuffle_list):
    shuffle(shuffle_list)
    return shuffle_list


print(shuffle_func(my_list))
