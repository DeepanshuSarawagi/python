even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd
print(sorted(numbers))
empty_list = []

print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(len(numbers))

print()

print(len(even))
print(len(odd))

print()

print("mississippi".count("s"))
print("mississippi".count("iss"))

even.extend(odd)
print(even)
another_even = even
print(another_even)
print()
even.sort(reverse=True)
print(even)

"""Refer following to know more of different ways of creating list and their performance - 
https://stackoverflow.com/questions/2612802/how-do-i-clone-a-list-so-that-it-doesnt-change-unexpectedly-after-assignment/43220129#43220129"""
