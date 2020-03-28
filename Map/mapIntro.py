string = "What have the Romans ever done for us"

capitals = [word.upper() for word in string]
print(capitals)

# Use map to get the same results.
map_capitals = list(map(str.upper, string))
print(map_capitals)
print()


words = [word.upper() for word in string.split(' ')]
print(words)

# Use map to print the capital words
map_words = list(map(str.upper, string.split(' ')))
print(map_words)

for x in map(str.upper, string.split(' ')):
    print(x)
