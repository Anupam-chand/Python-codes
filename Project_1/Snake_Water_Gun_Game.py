# code without trick
'''
1 for snake 
-1 for water
0 for gun
'''
import random

# We use random module to generate random values out of -1 n 1 and 0  for computer
computer = random.choice([-1, 0, 1])

youStr = input("Enter your choice:- ")
youDict = {"s": 1, "w" : -1, "g" : 0}
reverseDict = {1: "Snake", -1:"Water", 0: "Gun"}

you = youDict[youStr]

# By now rwe have 2 numbers (variables), you and computer

print(f"You Chose  {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Nested if-else method
if(computer == you):
    print("It's a draw!")
else:
    if (computer == -1 and you == 1):        
        print("You Win!")

    elif(computer == -1 and you == 0):
        print("You Lose!")
        
    elif(computer == 1 and you == -1):
        print("You Lose!")
        
    elif(computer == 1 and you == 0):
        print("You win!")
        
    elif(computer == 0 and you == -1):
        print("You Lose!")
        
    elif(computer == 0 and you == 1):
        print("You Lose!")
    else:
        print("Something went wrong!")

