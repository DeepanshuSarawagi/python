alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

vowels = ["a", "e", "i", "o", "u"]

letter = input("Please enter a vowel of your choice: ").lower()

index_of_vowel = alphabets.index(letter)

s = ""

s += letter

count = 0
length = len(s)


def append_char(char):
    global s
    s += char
    return s


if letter in vowels:
    while not length >= 6:
        count += 1
        new_index = index_of_vowel + count
        if new_index > 25:
            next_char = alphabets[(new_index - 26)]
            if next_char not in vowels:
                s = append_char(next_char)
                length = len(s)
            else:
                continue
        else:
            next_char = alphabets[new_index]
            if next_char not in vowels:
                s = append_char(next_char)
                length = len(s)
            else:
                continue
else:
    print("It is not a vowel. Please try again.")

print(s)
