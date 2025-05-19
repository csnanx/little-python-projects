import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator!")
letters_number = int(input("How many letters would you like in your password?\n"))
symbols_number = int(input("How many symbols would you like?\n"))
numbers_number = int(input("How many numbers would you like?\n"))

password_list = []

for i in range(letters_number):
    random_letter = random.choice(letters)
    password_list.append(random_letter)

for i in range(symbols_number):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)

for i in range(numbers_number):
    random_number = random.choice(numbers)
    password_list.append(random_number)

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your random password is: {password}")
