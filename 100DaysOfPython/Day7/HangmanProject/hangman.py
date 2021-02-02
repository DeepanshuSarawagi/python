import random
import hangman_art
import hangman_words

print(hangman_art.logo)

word_list = hangman_words.word_list
word = random.choice(word_list)


list_of_blanks = []

for i in range(0, len(word)):
    list_of_blanks.append("_")

var = False
lives = 6

while var is False:
    print(list_of_blanks)

    guess = input("Please guess a letter of your choice: ").lower()

    for i in range(0, len(word)):
        if guess == word[i]:
            list_of_blanks[i] = guess

    if guess not in word:
        lives -= 1
        print(hangman_art.stages[lives])

    if lives == 0:
        print("You Lose!")
        var = True

    if list(word) == list_of_blanks:
        var = True
        print("You Win!")
