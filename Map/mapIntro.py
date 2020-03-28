string = "What have the Romans ever done for us"

capitals = [word.upper() for word in string]
print(capitals)

words = [word.upper() for word in string.split(' ')]
print(words)
