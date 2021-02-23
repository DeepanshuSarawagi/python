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
        print("new index is now: {}".format(new_index))
        if new_index > 25:
            next_char = alphabets[(new_index - 26)]
            print("Next index is greater than 25. {}".format(next_char))
            if next_char not in vowels and length <= 6:
                s = append_char(next_char)
                print(s)
                length = len(s)
                print("length is now: {}".format(length))
            else:
                length = len(s)
                continue
        else:
            next_char = alphabets[new_index]
            print("Next index is lesser than 25. {}".format(next_char))
            if next_char not in vowels and length <= 6:
                s = append_char(next_char)
                print(s)
                length = len(s)
                print("length is now: {}".format(length))
            else:
                length = len(s)
                continue
        # if next_char not in vowels:
        #     s += next_char
        #     length = len(s)
        #     print("length is now: {}".format(length))
        # else:
        #     continue
else:
    print("It is not a vowel. Please try again.")

print(s)
