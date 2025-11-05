parrot = "Norwegian Blue"
letter = input("Enter a letter: ")
if letter in parrot.lower():
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter!")