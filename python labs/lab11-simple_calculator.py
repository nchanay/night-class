# simple calculator

def mathematical(x, y, operator):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    else:
        return x / y

do_another = True
while do_another:
    while True:
        operator= input("What is the operator you would like to perform? (+), (-), (*), or (/) : ").lower().strip()
        if operator in ['+', '-', '*', '/']:
            break
        print("input not valid")
    while True:
            first_num = input("what is your first number? : ")
            if first_num.isdigit():
                first_num = int(first_num)
                break
            else:
                print("Please enter a number")
    while True:
            second_num = input("what is your second number? : ")
            if second_num.isdigit():
                second_num = int(second_num)
                break
            else:
                print("Please enter a number")
    print(f"{first_num} {operator} {second_num} = {mathematical(first_num, second_num, operator)}")

    while True: # do_another == yes/no
        do_another = input("Do you want to do another? (yes) or (no) : ").strip().lower()
        if do_another not in ["yes", "no"]:
            print("That wasn't the answer I was looking for")
            continue
        else:
            break
    if do_another == "no":
        print("See ya later Alligator!")
        do_another = False
