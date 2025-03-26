import random

# Variables:
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
random_select = [rock, paper, scissors]
player_choice = input("Let's play a game of rock, paper, scissors! You go first.\n")
player_choice = player_choice.lower()
ai_choice = random.choice(random_select)

# Game Logic:
# A: Rock as choice:
if player_choice == "rock":
    if ai_choice == paper:
        print(paper + "\nI choose paper.\nOh no, you lost! Try again!")
    elif ai_choice == scissors:
        print(scissors + "\nI choose scissors.\nCongratulations, you won! Wanna play again?")
    elif ai_choice == rock:
        print(rock + "\nI choose rock.\nIt's a tie! Try again!")
    else:
        print("Error: Invalid choice. Please rerun the game.")
# B: Paper as choice:
elif player_choice == "paper":
    if ai_choice == scissors:
        print(scissors + "\nI choose scissors.\nOh no, you lost! Try again!")
    elif ai_choice == rock:
        print(rock + "\nI choose rock.\nCongratulations, you won! Wanna play again?")
    elif ai_choice == paper:
        print(paper + "\nI choose paper.\nIt's a tie! Try again!")
    else:
        print("Error: Invalid choice. Please rerun the game.")
# C: Scissors as choice:
elif player_choice == "scissors":
    if ai_choice == rock:
        print(rock + "\nI choose rock.\nOh no, you lost! Try again!")
    elif ai_choice == paper:
        print(paper + "\nI choose paper.\nCongratulations, you won! Wanna play again?")
    elif ai_choice == scissors:
        print(scissors + "\nI choose scissors.\nIt's a tie! Try again!")
    else:
        print("Error: Invalid choice. Please rerun the game.")
