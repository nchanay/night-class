def is_even(a):
    # if a % 2 == 0:
    #     return True
    # else:
    #     return False
    return a % 2 == 0
def opposite(a, b):
    # return not ((a >= 0 and b>= 0) or (a < 0 and b < 0))
    return (a >= 0 and b < 0) or (a <0 and b >=0)
    # if a >= 0 and b>= 0:
    #     return False
    # elif a < 0 and b < 0:
    #     return False
    # else:
    #     return True


print("is this number even?", is_even(-10))
print("is this number even?",is_even(17))
print("is this number even?",is_even(4235))

print(opposite(1, 2))
