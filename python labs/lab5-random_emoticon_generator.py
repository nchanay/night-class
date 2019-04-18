import random

eyes_list = [";", ":", "!", "8", "|", "X", "B"]
nose_list = ["^", "*", "<", ">", "o"]
mouth_list = ["D", "E", "P", "C", "(", ")", "|", "\\", "/"]

for faces in range(5):
    eyes = random.choice(eyes_list)
    nose = random.choice(nose_list)
    mouth = random.choice(mouth_list)
    print(eyes + nose + mouth)
