import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for index, row in nato_data.iterrows()}

user_name = input("Enter your name: ")
list_letters = [letter.upper() for letter in user_name]

mnemonics = []
for letter in list_letters:
    # mnemonics.append([value for key, value in nato_dict.items() if key == letter]
    for key, value in nato_dict.items():
        if key == letter:
            mnemonics.append(value)

print(mnemonics)
