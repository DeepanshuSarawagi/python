import hangman_words

word_list = hangman_words.word_list
vowels = ["a", "e", "i", "o", "u"]
# vowels = "aeiou"

count = 0

for words in word_list:
    if "a" in words or "e" in words or "i" in words or "o" in words or "u" in words:
        count += 1
    else:
        print(words)

print("No of word with vowels: " + str(count))
print(len(word_list))
