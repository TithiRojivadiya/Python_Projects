import random

gameRunning = True
num = random.randint(0,100)
attempt = 0

def result(num,user_num):
    global gameRunning
    if num == user_num :
        print("Your choise is correct !!!")
        gameRunning = False
    elif num > user_num :
        print("Please Enter Higher no. !!!")
        gameRunning = True
    elif num < user_num :
        print("Please Enter Lower no. !!!")
        gameRunning = True

def score():
    global gameRunning
    global attempt
    if gameRunning == True :
        attempt = attempt + 1
    else:
        print(f"You have guessed in {attempt+1} attempts.")

while gameRunning :
    user_num = int(input("Enter a no. :"))
    result(num,user_num)
    score()