import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
           "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the alphanumeric password generator!")
no_of_letters = int(input("How many letters would you like in your password? "))
no_of_numbers = int(input("How many numbers would you like in your password? "))
no_of_symbols = int(input("How many symbols would you like in your password? "))
password_length = no_of_letters + no_of_numbers + no_of_symbols

random_letters = ""
for i in range(1, no_of_letters + 1):
    random_letters += random.choice(letters)

random_numbers = ""
for i in range(1, no_of_numbers + 1):
    random_letters += random.choice(numbers)

random_symbols = ""
for i in range(1, no_of_symbols + 1):
    random_letters += random.choice(symbols)

initial_string = random_letters + random_numbers + random_symbols

list_of_string = list(initial_string)

random.shuffle(list_of_string)

final_password = ""
for i in range(0, len(list_of_string)):
    final_password += list_of_string[i]

print(final_password)
