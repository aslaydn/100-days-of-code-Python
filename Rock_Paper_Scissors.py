rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Rock wins against scissors.
#Scissors win against paper.
#Paper wins against rock.

import random

game_images = [rock,paper,scissors]
user_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_move == 1 or user_move ==2 or user_move ==0:
    choice1 = game_images[user_move]
computer_move = random.randint(0,2)
choice2 = game_images[computer_move]

if user_move == computer_move:
    print(f"{choice1}\ncomputer chose:\n{choice2}\nIt's a draw.")
elif user_move == 0 and computer_move == 2:
    print(f"{rock}\ncomputer chose:\n{scissors}\nYou win!")    
elif user_move == 2 and computer_move == 1:
    print(f"{scissors}\ncomputer chose:\n{paper}\nYou win!")
elif user_move == 1 and computer_move == 0:
    print(f"{paper}\ncomputer chose:\n{rock}\nYou win!") 
elif user_move != 1 and user_move !=2 and user_move !=0:
    print("You typed an invalid number. You lose.")      
else:
    print(f"{choice1}\ncomputer chose:\n{choice2}\nYou lose.")    