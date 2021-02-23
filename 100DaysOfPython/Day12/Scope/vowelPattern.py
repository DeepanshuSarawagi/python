alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

vowels = ["a", "e", "i", "o", "u"]

letter = input("Please enter a vowel of your choice: ").lower()

index_of_vowel = alphabets.index(letter)

s = ""

s += letter

length = len(s)
print(length)
count = 0

if letter in vowels:
    while length < 7:
        count += 1
        new_index = index_of_vowel + count
        print(new_index)
        if new_index > 25:
            next_char = alphabets[-25-1]
            print("Next index is greater than 25. {}".format(next_char))
        else:
            next_char = alphabets[new_index]
            print("Next index is lesser than 25. {}".format(next_char))
        if next_char not in vowels:
            s += next_char
            length = len(s)
        else:
            continue
else:
    print("It is not a vowel. Please try again.")

print(s)
