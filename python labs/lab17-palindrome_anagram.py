# Lab 17: Palindrome and Anagram

from string import punctuation


def check_palindrome(input):
    for symbols in punctuation:
        input = input.replace(symbols, '').lower().replace(' ', '')
    return input == input[::-1]


def check_anagram(input1, input2):
    for symbols in punctuation:
        input1 = input1.replace(symbols, '').lower().replace(' ', '')
    list1 = list(input1)
    list1.sort()

    for symbols in punctuation:
        input2 = input2.replace(symbols, '').lower().replace(' ', '')
    list2 = list(input2)
    list2.sort()
    return list1 == list2


while True:
    function = input("Would you like to check for a (palindrome) or (anagram)?\n> ").strip().lower()
    if function in ['p', 'palindrome', 'a', 'anagram']:
        break
    else:
        print("Please select one of the choices!")
if function.startswith('p'):
    input1 = input("What would you like to check to see if it is a palindrome?\n> ").strip()
    print(f"Is {input1} a palindrome? : {check_palindrome(input1)}")
else:
    input1 = input("What is our first word for the anagram checker?\n> ").strip()
    input2 = input("What is our second word for the anagram checker?\n> ").strip()
    print(f"Is {input1} an anagram of {input2}? : {check_anagram(input1, input2)}")
