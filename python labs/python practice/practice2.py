import random

def double_letters(x):
    double = ''
    for char in x:
        double += char * 2
    return double

    # return ''.join([char*2 for char in x])

print(double_letters('hello'))

def random_element(a):
    index = random.randint(0, len(a) - 1)
    return a[index]

fruits = ['pear', 'orange', 'grapefruit', 'kiwi']
print(random_element(fruits))
