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


if __name__ == "__main__":
    list1 = timeit.timeit("caps()", setup="from __main__ import caps", number=100000)
    print(list1)
    list2 = timeit.timeit("map_caps()", setup="from __main__ import map_caps", number=100000)
    print(list2)
    list3 = timeit.timeit("words_caps()", setup="from __main__ import words_caps", number=100000)
    print(list3)
    list4 = timeit.timeit("words_map()", setup="from __main__ import words_map", number=100000)
    print(list4)
