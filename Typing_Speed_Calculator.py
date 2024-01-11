import random
from time import *

def mistake(test_par, user_par):
    error = 0
    for i in range(len(test_par)):
        try:
            if test_par[i] != user_par :
                error = error + 1
        except:
            error = error + 1
    return error

def speed_calculation(time_start, time_end, user_par):
    time_delay = time_end - time_start
    time_R = round(time_delay, 2)
    speed = (len(user_par)/time_R)*60
    return round(speed)

test = [ "This feedback graph will follow you from page to page for your typing session. You can see more details by mousing over the graph. The session is reset when the tab on your browser is closed.",
         "To find out how fast you type, just start typing in the blank textbox on the right of the test prompt. You will see your progress, including errors on the left side as you type.",
         "You can fix errors as you go, or correct them at the end with the help of the spell checker. If you need to restart the test, delete the text in the text box. Interactive feedback shows you your current wpm and accuracy.",
         "The algorithm to calculate difficulty depends on the average word length and how many special characters like capitals, numbers and symbols are included in the text. Most standard pre-employment typing tests will be in the normal range.",
         "The Guinness World Record for fastest typing is 216 WPM, set by Stella Pajunas in 1946. Competitive typists today reach around 170 WPM. The average person types at about 40 WPM, adequate for most jobs.",
         "Typing practice paragraphs are texts specifically designed to help improve your typing skills. These paragraphs come in various forms, such as PDFs and can be found online or in downloadable formats."]

test1 = random.choice(test)

print("Typing speed calculator")


while True :
    check = input("Do you want to check your typing speed ? y/n ::::")
    if check == 'y':
        print(test1)
        print()
        print()
        time_start = time()
        print("Enter :::::::::::::")
        user_paragraph = input()
        time_end = time()
        print()
        print("speed : " + str(speed_calculation(time_start, time_end, user_paragraph)) )
        print("Error : " + str(mistake(test1, user_paragraph)))
    elif check == 'n':
        print("Thank you!!!")
        break
    else:
        print("Invalid input!!!")

