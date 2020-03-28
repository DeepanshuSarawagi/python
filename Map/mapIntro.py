string = "What have the romans ever done for us"

capitals = [word.upper() for word in string]
print(capitals)

words = [word.upper() for word in string.split(' ')]
print(words)

