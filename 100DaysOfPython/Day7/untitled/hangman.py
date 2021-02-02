import random

#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

word = random.choice(word_list)


list_of_blanks = []

for i in range(0, len(word)):
    list_of_blanks.append("_")

var = False

while var is False:
    print(list_of_blanks)

    guess = input("Please guess a letter of your choice: ").lower()

    for i in range(0, len(word)):
        if guess == word[i]:
            list_of_blanks[i] = guess
    if list(word) == list_of_blanks:
        var = True

print(list_of_blanks)
