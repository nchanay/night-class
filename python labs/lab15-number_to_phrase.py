# number to phrase

ones_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens_dict = {0: None, 1: None, 2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

# romans_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD', 400, 'D': 500, 'CM': 900, 'M': 1000}


def translate(user_num, type):
    if type.startswith('e'):
        hundreds = user_num // 100
        tens = user_num // 10 % 10
        ones = user_num % 10
        if user_num <= 19:
            return ones_dict[user_num]
        elif user_num >= 20 and user_num <= 99:
            if ones == 0:
                return tens_dict[tens]
            else:
                return '-'.join([tens_dict[tens], ones_dict[ones]])
        elif user_num >= 100 and tens_dict[tens] == None:
            if ones == 0:
                return '-'.join([ones_dict[hundreds], "hundred"])
            else:
                return '-'.join([ones_dict[hundreds], "hundred", ones_dict[user_num % 100]])
        elif user_num >= 100 and ones == 0:
            return '-'.join([ones_dict[hundreds], "hundred", tens_dict[tens]])
        else:
            return '-'.join([ones_dict[hundreds], "hundred", tens_dict[tens], ones_dict[ones]])

    else:
        # m_roman = user_num // 1000
        # cm_roman = user_num % 1000 // 900
        # d_roman = user_num % 1000 // 500
        # cd_roman1 = user_num % 1000 % 500
        # if cd_roman1 < 500:
        #     cd_roman = cd_roman1 // 400
        # c_roman = user_num % 500 // 100
        # xc_roman = user_num % 100 // 90
        # l_roman = user_num % 100 // 50
        # x_roman = user_num % 50 // 10
        # v_roman = user_num % 10 // 5
        # i_roman = user_num % 5
        # cite = https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html
        nums = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        roman = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        roman_version = []
        for i in range(len(nums)):
            count = int(user_num / nums[i])
            roman_version.append(roman[i] * count)
            user_num -= nums[i] * count
        return ''.join(roman_version)


print("We're going to translate your number")

while True:
    translate_method = input("Would you like to translate to (english) or (roman numerals) : ").lower().strip()
    if translate_method in ['e', 'english', 'r', 'roman', 'roman numerals']:
        break
    else:
        print("Invalid input")

while True:
    user_num = input("Please pick a positive number between 0-999 for english, 1-3999 for roman.\n> ")
    if user_num.isdigit():
        user_num = int(user_num)
        if user_num in range(0, 1000) and translate_method.startswith('e'):
            break
        elif user_num in range(1, 3999) and translate_method.startswith('r'):
            break
    else:
        print("Invalid input")


print(f"Your number {user_num} and want to translate to {translate_method} : {translate(user_num, translate_method)}.")
