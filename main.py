import random
import string

def generate_string():
    lettter_digits=string.ascii_letters+string.digits
    return ''.join(random.choice(lettter_digits) for i in range(8))

print(generate_string())
