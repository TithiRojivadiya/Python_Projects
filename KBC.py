import os

def robo_speaker(text):
    os.system(f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"')



print("\n")
robo_speaker("Welcome to KBC")
print("\n\nRules :")
print("(1)There are 16 questions of General Knowledge. The prize money increases with question no. You have to answer in 1,2,3,4.")
print("\n")
print("(2)If you give correct answer, You get prize money according to question no.")
print("\n")
print("(3)If you quit the game you get prize money of previous question. If you want to quit the game enter 5.")
print("\n")
print("(4)If you give wrong answer, \nIf you between question no. 1 to 5 , You will get Rs. 0.\nIf you between question no. 6 to 10  , You will get Rs. 10,000\nIf you between question no. 11 to 16 , You will get Rs. 3,20,000.")
print("\n")
print("(5)There are three LifeLines : (A)50:50,(B)Expert's Advice,(C)Switch the Question. You can choose only one lifeline at a time. ")
print("\n")
print("(A)50:50 ::: Will remove two wrong answer.")
print("\n")
print("(B)Expert's Advice ::: Guide you.")
print("\n")
print("(C)Switch the Question ::: will give you 6 options of subject. Choose one subject and you will be asked other question according to chozen subject instead of main question.")
print("\n\n\n")
print("Are you ready ? Let's go...")
print("\n\n\n")

questions = [
    [" Which river is the longest in the world?","The Nile River","The Amazon River","The Ganga River","The Yamuna River",1],

    ["Name of the first university of India?","Nalanda University","Taxshila University","Valabhi University","Bharatiya University",1],

    ["Who was the first President of India?","Mahatma Gandhi"," Dr. Rajendra Prasad","Jawaharlal Nehru","Saradar Patel",2],

    ["Stanley Cup is related to which sport?","Cricket","Football","Hockey","Tennis",3],

    ["The base of Binary no. is-","10","2","16","8",2],

    ["What is the national animal of India ?","Linon","Deer","Cow","Tiger",4],

    ["When was the Battle of Plassey fought?","1749","1801","1757","1758",3],

    ["What is the only even prime number?","1","3","2","4",3],

    [" What is the largest continent in the world by land area?","Asia","Europe","Africa","South America",1],

    ["At which age Gautham Buddha got Nirvana?","25","35","32","40",2],

    #Change the questions

    ["The ratio of width of our National flag to its length is ?","3:5","2:3","2:4","2:5",2],

    ["Dandia is a popular dance of","Gujarat","Panjab","Rajsthan","Delhi",1],

    ["Mohiniattam dance from developed originally in which state?","Tamil Nadu","Orissa","Kerala","Karnataka",3],

    ["The number of moles of solute present in 1 kg of a solvent is called its","molality","molarity","normality","formality",1],

    ["Plants synthesis protein from","starch","sugar","amino acids","fatty acids",3],

    ["Nuclear sizes are expressed in a unit named ","newton","tesla","angstrom","Fermi",4]

    #change the questions
]#end of questions

money = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,"1 Crore","7 Crore"]

LifeLine = ["(A)50:50","(B)Expert's Advice","(C)Switch the Question"]
switch_question = [

    #Indian politics
    ["The members of the Rajya Sabha are elected by","the people","Lok Sabha","elected members of the legislative assembly","elected members of the legislative council",3],

    #Books&Authors
    ["The book 'To Live or Not Live' was written by","V.S. Naipaul","Alexandra Dumas","George Elliot","Nirad C. Chaudhuri",4],

    #Indian Economy
    ["ICICI is the name of a","chemical industry","bureau","corporation","financial institution",4],

    #Indian Geography
    ["The percentage of irrigated land in India is about","45","65","35","25",3],

    #Indian Mythologi
    ["Which one is the first avatar of Lord Vishnu from his Dashavatar?","Matsya","Kurma","Varah","Narasimbha",1],

    #Inventions
    ["Which scientist discovered the radioactive element radium?","Isaac Newton","Albert Einstein","Benjamin Franklin","Marie Curie",4]

]#end of switch_question

for i in range(0,len(questions),1) :

    print("\n")
    print(f"Rs. {money[i]}")

    print(questions[i][0])
    print(f"1){questions[i][1]}\t2){questions[i][2]}")
    print(f"3){questions[i][3]}\t4){questions[i][4]}")

    print("You Can use LifeLine ::::::")
    print("If you want to take LifeLine, Enter 5")

    print("Enter 0 for quit....")
    

    ans = int(input("Enter your answer :"))
    if ans == questions[i][5] :
            robo_speaker("Correct Answer")
            print("\n################## Correct Answer ##################")
            print(f"Congratulations You have won Rs. {money[i]}")

    elif ans == 0 :
            if i==0 :
                print("Try Next time ...")
            else :
                print(f"\nYou have won {money[i-1]}")
                print("Congratulations!!!!")
                print(f"Correct Answer is {questions[i][5]})")
            break

    elif ans==5 :

            #LifeLine Display
            if "(A)50:50" not in LifeLine and "(B)Expert's Advice" not in LifeLine and "(C)Switch the Question" not in LifeLine :
                    print("You have no Life-line...")
                    #If no life line It will display
                    
            else :
                for j in range(len(LifeLine)) :
                    print(LifeLine[j])


                #No life Line....
            if "(A)50:50" not in LifeLine and "(B)Expert's Advice" not in LifeLine and "(C)Switch the Question" not in LifeLine :
                ans_of_no_lifeline = int(input("Enter your answer :"))


                if ans_of_no_lifeline == questions[i][5] :
                    print("\n################## Correct Answer ##################")
                    print(f"Congratulations You have won Rs. {money[i]}")

                elif ans_of_no_lifeline == 0 :
                    if i==0 :
                        print("Try Next time ...")
                    else :
                        print(f"\nYou have won {money[i-1]}")
                        print("Congratulations!!!!")
                        print(f"Correct Answer is {questions[i][5]})")
                    break

                else : #wrong answer
                    print("\n################## Wrong Answer ##################")
                    print(f"Correct Answer is {questions[i][5]})")
                    if i>4 and i<=9 :
                        print(f"Congratulations You have won Rs. {money[4]}")
                    if i>9 and i<=15 :
                        print(f"Congratulations You have won Rs. {money[9]}")
                    break

            else : #you can use lifeline...
                lifeline=input("Which LifeLine do you want to take ?")
                

                if lifeline=='0':
                    if i==0 :
                        print("Try Next time ...")
                        break
                    else :
                        print(f"\nYou have won {money[i-1]}")
                        print("Congratulations!!!!")
                        print(f"Correct Answer is {questions[i][5]})")
                        break
                    
                #50:50
                if lifeline=='A' or lifeline=='a':

                    if(questions[i][5]==1):
                        print(f"(1){questions[i][1]}")
                        print(f"(2){questions[i][2]}")

                    elif(questions[i][5]==2):
                        print(f"(2){questions[i][2]}")
                        print(f"(3){questions[i][3]}")

                    elif(questions[i][5]==3):
                        print(f"(2){questions[i][2]}")
                        print(f"(3){questions[i][3]}")

                    elif(questions[i][5]==4):
                        print(f"(1){questions[i][1]}")
                        print(f"(4){questions[i][4]}")

                    ans2 = int(input("Enter your answer :"))

                    if ans2==questions[i][5]:
                        robo_speaker("Correct Answer")
                        print("\n################## Correct Answer ##################")
                        print(f"Congratulations You have won Rs. {money[i]}")
                        LifeLine.remove("(A)50:50")

                    elif ans2 == 0 :
                        if i==0 :
                            print("Try Next time ...")
                        else :
                            print(f"\nYou have won {money[i-1]}")
                            print("Congratulations!!!!")
                            print(f"Correct Answer is {questions[i][5]})")
                        break

                    else : #wrong answer
                        print("\n################## Wrong Answer ##################")
                        print(f"Correct Answer is {questions[i][5]})")
                        if i>4 and i<=9 :
                            print(f"Congratulations You have won Rs. {money[4]}")
                        if i>9 and i<=15 :
                            print(f"Congratulations You have won Rs. {money[9]}")
                        break

                  #expert's advice  
                elif lifeline=='B' or lifeline=='b':

                    print(f"May be should choose {questions[i][5]}.....")

                    ans3 = int(input("Enter Your Answer :"))

                    if ans3 == questions[i][5]:
                        robo_speaker("Correct Answer")
                        print("\n################## Correct Answer ##################")
                        print(f"Congratulations You have won Rs. {money[i]}")
                        LifeLine.remove("(B)Expert's Advice")

                    elif ans3==0:
                        if i==0 :
                            print("Try Next time ...")
                            break
                        else :
                            print(f"\nYou have won {money[i-1]}")
                            print("Congratulations!!!!")
                            print(f"Correct Answer is {questions[i][5]})")
                            break

                    else :
                        print("\n################## Wrong Answer ##################")
                        print(f"Correct Answer is {questions[i][5]})")
                        if i>4 and i<=9 :
                            print(f"Congratulations You have won Rs. {money[4]}")
                        if i>9 and i<=15 :
                            print(f"Congratulations You have won Rs. {money[9]}")
                        break

                elif lifeline=='C' or lifeline=='c':
                    print(f"Correct Answer is {questions[i][5]})")
                    print("(1)Indian politics")
                    print("(2)Books & Authors")
                    print("(3)Indian Economy")
                    print("(4)Indian Geography")
                    print("(5)Indian Mythology")
                    print("(6)Inventions")

                    ans4 = int(input("Enter your choice :"))

                    if ans4==1 :#indian politics
                        print(switch_question[0][0])
                        print(f"1){switch_question[0][1]}\t2){switch_question[0][2]}")
                        print(f"3){switch_question[0][3]}\t4){switch_question[0][4]}")

                        a=int(input("Enter Your Answer :"))

                        if a==switch_question[0][5] :
                            robo_speaker("Correct Answer")
                            print("\n################## Correct Answer ##################")
                            print(f"Congratulations You have won Rs. {money[i]}")
                            LifeLine.remove("(C)Switch the Question")

                        elif a==0:
                            if i==0 :
                                print("Try Next time ...")
                            else :
                                print(f"\nYou have won {money[i-1]}")
                                print("Congratulations!!!!")
                                print(f"Correct Answer is {switch_question[0][5]})")
                            break

                        else :
                            print("\n################## Wrong Answer ##################")
                            print(f"Correct Answer is {switch_question[0][5]})")
                            if i>4 and i<=9 :
                                print(f"Congratulations You have won Rs. {money[4]}")
                            if i>9 and i<=15 :
                                print(f"Congratulations You have won Rs. {money[9]}")
                            break
                    
                    elif ans4==2 :#Books & Authors
                        print(switch_question[1][0])
                        print(f"1){switch_question[1][1]}\t2){switch_question[1][2]}")
                        print(f"3){switch_question[1][3]}\t4){switch_question[1][4]}")

                        b=int(input("Enter Your Answer :"))

                        if b==switch_question[1][5] :
                            robo_speaker("Correct Answer")
                            print("\n################## Correct Answer ##################")
                            print(f"Congratulations You have won Rs. {money[i]}")
                            LifeLine.remove("(C)Switch the Question")


                        elif b==0:
                            if i==0 :
                                print("Try Next time ...")
                            else :
                                print(f"\nYou have won {money[i-1]}")
                                print("Congratulations!!!!")
                                print(f"Correct Answer is {switch_question[1][5]})")
                            break

                        else :
                            print("\n################## Wrong Answer ##################")
                            print(f"Correct Answer is {switch_question[1][5]})")
                            if i>4 and i<=9 :
                                print(f"Congratulations You have won Rs. {money[4]}")
                            if i>9 and i<=15 :
                                print(f"Congratulations You have won Rs. {money[9]}")
                            break

                    elif ans4==3 :#Indian Economy
                        print(switch_question[2][0])
                        print(f"1){switch_question[2][1]}\t2){switch_question[2][2]}")
                        print(f"3){switch_question[2][3]}\t4){switch_question[2][4]}")

                        c=int(input("Enter Your Answer :"))

                        if c==switch_question[2][5] :
                            robo_speaker("Correct Answer")
                            print("\n################## Correct Answer ##################")
                            print(f"Congratulations You have won Rs. {money[i]}")
                            LifeLine.remove("(C)Switch the Question")

                        elif c==0:
                            if i==0 :
                                print("Try Next time ...")
                            else :
                                print(f"\nYou have won {money[i-1]}")
                                print("Congratulations!!!!")
                                print(f"Correct Answer is {switch_question[2][5]})")
                            break

                        else :
                            print("\n################## Wrong Answer ##################")
                            print(f"Correct Answer is {switch_question[1][5]})")
                            if i>4 and i<=9 :
                                print(f"Congratulations You have won Rs. {money[4]}")
                            if i>9 and i<=15 :
                                print(f"Congratulations You have won Rs. {money[9]}")
                            break

                    elif ans4==4 :#Indian Geography
                        print(switch_question[3][0])
                        print(f"1){switch_question[3][1]}\t2){switch_question[3][2]}")
                        print(f"3){switch_question[3][3]}\t4){switch_question[3][4]}")

                        d=int(input("Enter Your Answer :"))

                        if d==switch_question[3][5] :
                            robo_speaker("Correct Answer")
                            print("\n################## Correct Answer ##################")
                            print(f"Congratulations You have won Rs. {money[i]}")
                            LifeLine.remove("(C)Switch the Question")

                        elif d==0:
                            if i==0 :
                                print("Try Next time ...")
                            else :
                                print(f"\nYou have won {money[i-1]}")
                                print("Congratulations!!!!")
                                print(f"Correct Answer is {switch_question[3][5]})")
                            break

                        else :
                            robo_speaker("Wrong Answer")
                            print(f"Correct Answer is {switch_question[3][5]})")
                            if i>4 and i<=9 :
                                print(f"Congratulations You have won Rs. {money[4]}")
                            if i>9 and i<=15 :
                                print(f"Congratulations You have won Rs. {money[9]}")
                            break

                    elif ans4==5 :#Indian Mythology
                        print(switch_question[4][0])
                        print(f"1){switch_question[4][1]}\t2){switch_question[4][2]}")
                        print(f"3){switch_question[4][3]}\t4){switch_question[4][4]}")

                        e=int(input("Enter Your Answer :"))

                        if e==switch_question[4][5] :
                            robo_speaker("Correct Answer")
                            print("\n################## Correct Answer ##################")
                            print(f"Congratulations You have won Rs. {money[i]}")
                            LifeLine.remove("(C)Switch the Question")

                        elif e==0:
                            if i==0 :
                                robo_speaker("Try Next time ...")
                            else :
                                print(f"\nYou have won {money[i-1]}")
                                print("Congratulations!!!!")
                                print(f"Correct Answer is {switch_question[4][5]})")
                            break

                        else :
                            
                            robo_speaker("Wrong Answer")
                            print(f"Correct Answer is {switch_question[4][5]})")
                            if i>4 and i<=9 :
                                print(f"Congratulations You have won Rs. {money[4]}")
                            if i>9 and i<=15 :
                                print(f"Congratulations You have won Rs. {money[9]}")
                            break

                    elif ans4==6 : #Inventions
                        print(switch_question[5][0])
                        print(f"1){switch_question[5][1]}\t2){switch_question[5][2]}")
                        print(f"3){switch_question[5][3]}\t4){switch_question[5][4]}")

                        f=int(input("Enter Your Answer :"))

                        if f==switch_question[5][5] :
                            robo_speaker("Correct Answer")
                            print("\n################## Correct Answer ##################")
                            print(f"Congratulations You have won Rs. {money[i]}")
                            LifeLine.remove("(C)Switch the Question")

                        elif f==0:
                            if i==0 :
                                robo_speaker("Try Next time ...")
                            else :
                                robo_speaker(f"You have won {money[i-1]}")
                                print(f"You have won {money[i-1]}")
                                robo_speaker("Congratulations!!!!")
                                robo_speaker(f"Correct Answer is {switch_question[5][5]})")
                            break

                        else :
                            robo_speaker("Wrong Answer")
                            robo_speaker(f"Correct Answer is {switch_question[5][5]})")
                            if i>4 and i<=9 :
                                print(f"Congratulations You have won Rs. {money[4]}")
                                robo_speaker(f"Congratulations You have won Rs. {money[4]}")
                            if i>9 and i<=15 :
                                print(f"Congratulations You have won Rs. {money[9]}")
                                robo_speaker(f"Congratulations You have won Rs. {money[9]}")
                            break

    else : #wrong answer
        robo_speaker("Wrong Answer")
        robo_speaker(f"Correct Answer is {questions[i][5]})")
        if i>4 and i<=9 :
            robo_speaker(f"Congratulations You have won Rs. {money[4]}")
            print(f"Congratulations You have won Rs. {money[4]}")
        if i>9 and i<=15 :
            robo_speaker(f"Congratulations You have won Rs. {money[9]}")
            print(f"Congratulations You have won Rs. {money[9]}")
        break
