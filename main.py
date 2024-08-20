import random
import sys

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
you_win = "You win!"
you_lose = "You lose"
draw = "It's a draw"
invalid_message = "You typed an invalid number, you lose!"
winner = ""

computer_choice = random.randint(0,2)
if computer_choice == 0:
    computer_choice = rock
elif computer_choice == 1:
    computer_choice = paper
else:
    computer_choice = scissors

    
try:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
    if user_choice > 2:
        print(invalid_message)
        sys.exit()
    elif user_choice == 0:
        user_choice = rock
        if user_choice == rock and computer_choice == rock:
            winner = "no one"
        elif user_choice == rock and computer_choice == paper:
            winner = "computer"
        else:
            winner = "user"
    elif user_choice == 1:
        user_choice = paper
        if user_choice == paper and computer_choice == rock:
            winner = "user"
        elif user_choice == paper and computer_choice == paper:
            winner = "no one"
        else:
            winner = "computer"
    else:
        user_choice = scissors
        if user_choice == scissors and computer_choice == rock:
            winner = "computer"
        elif user_choice == scissors and computer_choice == paper:
            winner = "user"
        else:
            winner = "no one"
except ValueError:
    print(f"undefined\nComputer chose:\n {computer_choice}")
    sys.exit()

#now print results of game
print(f"{user_choice} \n Computer chose:\n{computer_choice}")

if winner == "user":
    print(you_win)
elif winner == "no one":
    print(draw)
else:
    print(you_lose)