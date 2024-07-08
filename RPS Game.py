# `````` Welcome to the Rock, Paper, and Scissors game. ``````
print("Welcome to the Rock, Paper, and Scissors game.")
# `````````` just a demo, nothing special. ````````
print('''
      
█▀█ █▀█ █▀▀ █▄▀  
█▀▄ █▄█ █▄▄ █░█  ,

█▀█ ▄▀█ █▀█ █▀▀ █▀█  
█▀▀ █▀█ █▀▀ ██▄ █▀▄  , 

█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█ . 
     
       ''')
# Rock Paper Scissors ASCII Art
# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
import random
game_modes = [rock, paper, scissors]

player_choice = int(input('What do you choose? Type "0 for Rock", "1 for Paper" or "2 for Scissors" :\n'))
if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number, please check and try again!")
else :     
      print(game_modes[player_choice])
# `````` Where the computer has to chose its own game mode. ``````

      print("Computer chose :")
      computer_choice = random.randint(0, 2)
      print(game_modes[computer_choice])

      # `````` Now to the conditions. ``````
      if player_choice == 0 and computer_choice == 2 :
       print("You win!")   
      elif player_choice == computer_choice :
       print("It's a draw.")
      elif computer_choice == 0 and player_choice == 2 :
       print("You lose!")
      elif computer_choice > player_choice : 
       print("You lose!")
      elif player_choice > computer_choice :
       print("You win!")         


# ``````linuxmode``````