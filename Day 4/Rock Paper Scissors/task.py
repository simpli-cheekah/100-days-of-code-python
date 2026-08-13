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
import random
choices = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:"))
computer_choice = [random.choice(choices)]

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

print("Computer choose:\n" + random.choice(computer_choice))

if choice == computer_choice:
    print("it's a tie!")
elif choice == 0 and computer_choice == [scissors]:
    print("You win! Rock beats Scissors!")
elif choice == 1 and computer_choice == [rock]:
    print("You win! Paper beats Rock!")
elif choice == 2 and computer_choice == [paper]:
    print("You win! Scissors beats Paper!")
else:
    print("You lose! Computer Wins.")