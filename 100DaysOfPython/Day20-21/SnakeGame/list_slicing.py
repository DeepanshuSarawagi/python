"""In this simple python program we are going to see how to slice a list"""

list_of_vowels = ["a", "e", "i", "o", "u"]

print(list_of_vowels[2:5])  # This will print from i till u. We need to be careful here that u is the fifth element
# and we need to include it in order for it be printed

print(list_of_vowels[::-1])  # This will print the list of vowels in reverse order

print(list_of_vowels[::2])  # This will print every consecutive item in the list



