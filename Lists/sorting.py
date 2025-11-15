pangram = "The Quick Brown Fox jumps over the lazy dog"
print(pangram)
letters = sorted(pangram.lower())
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

# another_sorted_numbers = numbers.sort()
numbers.sort()
print(numbers)
# print(another_sorted_numbers)

"""The difference between list.sort() and sorted() methods is that in the former, the list is sorted in-place without having
a variable assigned to it since it doesn't return anything, whereas, the sorted function returns a list and hence a 
variable needs to be assigned to it."""

missing_letter = sorted("The quick brown fox jumps over the lazy dog")
print(missing_letter)

