'''
if (computer == -1 and you == 1): # -1-1 = -2     
        print("You Win!")

elif(computer == -1 and you == 0): # -1-0 = -1
    print("You Lose!")
        
elif(computer == 1 and you == -1): # 1 - (-1) = 2
    print("You Lose!")
        
elif(computer == 1 and you == 0): # 1 - 0 = 1
    print("You win!")
        
elif(computer == 0 and you == -1): # 0 -(-1) = 1
    print("You Lose!")
        
elif(computer == 0 and you == 1): # 0  -1 = -1 
    print("You Lose!")
else:
    print("Something went wrong!")

# In above game we notice the pattern that if you get  -1 and 2 you loose the game and if you get 1 and -2 you win the game 
# we can build code according to this logic to make the lines of code shorter
if((computer - you) == -1 or (computer - you) == 2):
    print("You Lose!")
else:
    print("You Win!")
'''    
