# Program for Rock paper Scissor

import random
Rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
Paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
Scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
print("\n\nWelcome to the Rock paper Scissor Game!\n")
print("Winning rules of the game:\nRock vs paper-> paper wins\nRock vs scissor-> Rock wins\npaper vs scissor-> scissor wins.")
print("\n\nType: \n0 for Rock \n1 for Paper\n2 for Scissor.")
game_images=[Rock,Paper,Scissor]
user_choice=int(input("Enter user choice:"))
if (user_choice>=3 or user_choice<0):
    print("\n\nYou entered in valid number,You Lose!")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("Now it's Computer's Turn...\ncomputer_choice")
    print(game_images[computer_choice])
    print("\n\nResult is: ")
    if(computer_choice==user_choice):
        print("<==It is a draw! Please try again later ==>")
    elif(computer_choice>user_choice):
        print(" <==You Lose! ==>")
    elif(user_choice>computer_choice):
        print("<==You Win! ==>")
    elif(computer_choice==0 and user_choice==2):
        print("<==You Lose!==>")
    elif(user_choice==0 and computer_choice==2):
        print("<==You Win! ==>")

# else:
#     print("Invalid choice! Please try again")