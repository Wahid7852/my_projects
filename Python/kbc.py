# A program which is a simple version of the game "Kaun Banega Crorepati"

import os
os.system('cls')

name = input("Enter your name: ")
print("\nWelcome to Kaun Banega Crorepati,", name, "We hope you enjoy the game!\nLets start with your first question:\n")

questions = [ "What is the capital of India?\nOptions are:\n Delhi\n Mumbai\n Kolkata\n Chennai\nYour Answer: ",
              "What is the financial capital of India?\nOptions are:\n Delhi\n Mumbai\n Kolkata\n Chennai\nYour Answer: ",
              "How many planers are there in the solar system?\nOptions are:\n 8\n 9\n 10\n 11\nYour Answer: ",
              "What is the value of the gravity constant 'g' ? \nOptions are\n: 9.8\n 9.9\n 10\n 10.2\nYour Answer: "]

answers = ["delhi" , "mumbai" , "8" , "9.8"]

a,b,c,d = "1000 Rs", "2000 Rs", "3000 Rs", "5000 Rs"

answers1 = input(questions[0])
if(answers1.lower() == answers[0]):
    print("Correct answer!")
    print("You have won", a)

else:
    print("Wrong answer!")
    print("You have lost the game!")
    exit()

print("\nYour second question is:\n")
answers2 = input(questions[1])
if(answers2.lower() == answers[1]):
    print("Correct answer!")
    print("You have won", b)

else:
    print("Wrong answer!")
    print("You have lost the game!")
    exit()

print("\nYour third question is:\n")
answers3 = input(questions[2])
if(answers3.lower() == answers[2]):
    print("Correct answer!")
    print("You have won", c)

else:
    print("Wrong answer!")
    print("You have lost the game!")
    exit()

print("\nYour fourth question is:\n")
answers4 = input(questions[3])
if(answers4.lower() == answers[3]):
    print("Correct answer!")
    print("You have won", d)

else:
    print("Wrong answer!")
    print("You have lost the game!")
    exit()

print("\nCongratulations", name, "you have won the game!\n")
