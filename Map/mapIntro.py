import timeit

string = "What have the Romans ever done for us"


def caps():
    capitals = [word.upper() for word in string]
    return capitals


# Use map to get the same results.

def map_caps():
    map_capitals = list(map(str.upper, string))
    return map_capitals


print()


def words_caps():
    words = [word.upper() for word in string.split(' ')]
    return words


# Use map to print the capital words
def words_map():
    map_words = list(map(str.upper, string.split(' ')))
    return map_words


def map_iter():
    for x in map(str.upper, string.split(' ')):
        return x


result1 = timeit.timeit(caps, globals=globals(), number=10000)
result2 = timeit.timeit(map_caps, globals=globals(), number=10000)
result3 = timeit.timeit(words_caps, globals=globals(), number=10000)
result4 = timeit.timeit(words_map, globals=globals(), number=10000)
result5 = timeit.timeit(map_iter, globals=globals(), number=10000)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)


