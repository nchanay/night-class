# Credit Card Validation


def ccv(card_num):
    """
    >>> ccv("4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5")
    "Valid"
    """
    num = card_num.replace(' ', '')  # taking out the spaces
    num_list = [int(i) for i in list(num)]  # building a list of ints out of the remaining string
    check_digit = num_list.pop()  # taking the last digit out of the list, and setting it as our check digit
    num_list.reverse()  # reversing the remaining list
    for i in range(len(num_list)):  # doubling every other element
        if i % 2 == 0:
            num_list[i] = num_list[i]*2
    for i in range(len(num_list)):  # subtracting 9 from any element over 9
        if num_list[i] > 9:
            num_list[i] = num_list[i]-9
    num_list = sum(num_list) % 10  # summing ints in list, and taking the one's digit
    if num_list == check_digit:  # checking to see if our summed one's digit is the same as our check digit
        return "Valid"
    else:
        return "Invalid"


card_num = "4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5"
print(ccv(card_num))

card_num2 = "4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 4"
print(ccv(card_num2))
