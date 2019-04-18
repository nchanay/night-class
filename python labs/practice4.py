# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.
#
# eveneven([5, 6, 2]) → True
# eveneven([5, 5, 2]) → False

import random

def eveneven(list):
    evens = [num for num in list if num % 2 == 0]
    # for num in list:
    #     if num % 2 == 0:
    #         evens += 1
    return len(evens) % 2 == 0

num_list = [random.randint(0,9) for digit in range(6)]
# for digit in range(6):
#     num_list.append(random.randint(0,9))

print(f"The list is {num_list}\nThere are an even number of evens in the list : {eveneven(num_list)}")

#comprehension practice 1
print([2**i for i in range (10)])
#comprehension practice 2
print([i*2 for i in range (1,11)])
