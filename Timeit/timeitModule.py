import timeit

setup = """\
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
"""

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}


def nested_loops():
    result = []
    for loc in sorted(locations):
        exits_to_destination_1 = []
        for xit in exits:
            if loc in exits[xit].values():
                exits_to_destination_1.append((xit, locations[xit]))
        result.append(exits_to_destination_1)
    return result


def list_comprehension():
    result = []
    for loc in sorted(locations):
        exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
        result.append(exits_to_destination_2)
    return result


def nested_comprehension():
    exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                              for loc in sorted(locations)]
    return exits_to_destination_3


def nested_generators():
    exits_to_destination_4 = ([(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                              for loc in sorted(locations))
    return exits_to_destination_4


print(nested_loops())
print(list_comprehension())
print(nested_comprehension())
result_1 = timeit.timeit(nested_loops, number=10000)
result_2 = timeit.timeit(list_comprehension, number=10000)
result_3 = timeit.timeit(nested_comprehension, number=10000)
result_4 = timeit.timeit(nested_generators, number=10000)
print(f"Nested loops take:'\t'{result_1} seconds to execute the code 1000 times.")
print(f"List comprehensions take:'\t'{result_2} seconds to execute the code 1000 times.")
print(f"Nested comprehensions take:'\t'{result_3} seconds to execute the code 1000 times.")
print(f"Nested generators take:'\t'{result_4} seconds to execute the code 1000 times.")
