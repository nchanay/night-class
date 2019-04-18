while True:
    user_grade = int(input("Enter your score:\n> "))
    ones_digit = user_grade % 10

    if user_grade >= 90:
        letter_grade = "A"
    if user_grade >= 80:
        letter_grade = "B"
    if user_grade >= 70:
        letter_grade = "C"
    if user_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    sign = ""
    if letter_grade != "F":
        if ones_digit <= 3:
            sign = "-"
        elif ones_digit >= 7:
            sign = "+"

    if user_grade >= 100:
        sign = "+"

    print(str(letter_grade) + sign)

    valid_inputs = ['yes', 'y', 'no', 'n']
    while True:
        play_again = input("Do you want to continue: ").strip().lower()
        if play_again in valid_inputs:
            break

    if play_again.startswith('n'):
        print("Goodbye!")
        break
