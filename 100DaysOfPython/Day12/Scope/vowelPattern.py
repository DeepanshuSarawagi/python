alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

vowels = ["a", "e", "i", "o", "u"]

letter = input("Please enter a vowel of your choice: ").lower()

index_of_vowel = alphabets.index(letter)

s = ""

s += letter

count = 1

while count < 6:
    new_index = index_of_vowel + count
    next_char = ""
    if new_index > 25:
        next_char = alphabets[-25-1]
        print(next_char)
    else:
        next_char = alphabets[new_index]
        print(next_char)
    print(next_char in vowels)
    if next_char in vowels:
        print("Found a vowel")
        continue
    s += next_char
    count += 1

print(s)