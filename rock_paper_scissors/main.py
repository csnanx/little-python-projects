import random

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

choices = [rock, paper, scissors]
computer_choice = random.choice(choices)

user_choice_index = int(input("0 for 'rock', 1 for 'paper' and 2 for 'scissors'\nEnter your choice: "))
user_choice = choices[user_choice_index]

print(f"Your Choice:\n{user_choice}")
print(f"Computer's Choice:\n{computer_choice}")

