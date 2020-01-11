# We are going to practice some examples on Python on dictionary
# Exercise 1: Write a Python script to sort (ascending and descending) a dictionary by value.
vowels = {"a": "An apple a day keeps the doctor away",
          "e": "English is globally spoken.",
          "i": "India is a very beautiful country",
          "o": "Outstanding that you are practicing problems on Dictionary",
          "u": "Umbrella protects one from harsh weather"}
print(vowels)
print(vowels.keys())
print(vowels.items())
for f in sorted(vowels.keys()):
    print(f"{f} - {vowels[f]}")
print(sorted(vowels.values()))
reverse_vowels = sorted(vowels.values(), reverse=True)
print(reverse_vowels)


