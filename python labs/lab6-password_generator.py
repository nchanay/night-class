import random
import string

password_upper_letters = int(input("How many upper case letters should our password have?\n> "))
password_lower_letters = int(input("How many lower case letters should our password have?\n> "))
password_numbers = int(input("How many numbers should our password have?\n> "))
password_special_characters = int(input("How many special characters should our password have?\n> "))

pw_up_letters = ''
for num in range(password_upper_letters):
    pw_up_letters += random.choice(string.ascii_uppercase)

pw_low_letters = ''
for num in range(password_lower_letters):
    pw_low_letters += random.choice(string.ascii_lowercase)

pw_numbers = ''
for num in range(password_numbers):
    pw_numbers += random.choice(string.digits)

pw_puncuations = ''
for num in range(password_special_characters):
    pw_puncuations += random.choice(string.punctuation)

random_password = pw_up_letters + pw_low_letters + pw_numbers + pw_puncuations
rp_list = list(random_password)
random.shuffle(rp_list)
random_password = ''.join(rp_list)

print(f"Your random password is: {random_password}")
