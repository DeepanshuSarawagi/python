import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for index, row in nato_data.iterrows()}


def nato_project():
    try:
        user_name = input("Enter your name: ")
        list_letters = [letter.upper() for letter in user_name]
        phonetics = [nato_dict[letter] for letter in list_letters]
        print(phonetics)
    except KeyError:
        print("Sorry!! Only alphabets are accepted for the NATO Phonetics. Please try again.")
        nato_project()


nato_project()
