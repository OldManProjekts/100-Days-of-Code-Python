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

#Write your code below this line 👇
import random

print("Would you like to play a Game?")
choice = input ("Choose your weapon. 0 for Rock, 1 for Paper, or 2 for Scissors\n")
choice_int = int(choice)

if choice_int == 0:
  print(rock + "Rock")
elif choice_int == 1:
  print(paper + "Paper")
elif choice_int == 2:
  print(scissors + "Scissors")

print("Computer chose:\n")

computer = random.randint(0, 2)

if computer == 0:
  print(rock + "Rock")
elif computer == 1:
  print(paper + "Paper")
elif computer == 2:
  print(scissors + "Scissors")

if choice_int >= 3 or choice_int < 0:
  print("You typed an invalid number, you lose")
elif choice_int == 0 and computer == 2:
  print("You win")
elif computer == 0 and choice_int == 2:
  print("You lose")
elif computer > choice_int:
  print("You lose")
elif computer < choice_int:
  print("You win")
elif computer == choice_int:
  print("It is a draw")
