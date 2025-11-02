parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])

# Negative indexing
print(parrot[-1])  # Will print the last character of the string
print(parrot[-14]) # Will print the first character of the string
print(parrot[:9:2]) # Stepper, it will skip every 1 character until index 9
print(parrot[::2]) # Skip every consecutive char from the string

# Nice example using list comprehension and stepper

numbers = "9,223,289;865 965:437.116"
separators = numbers[1::4]
print(separators)
values = "".join(char if char not in separators else " " for char in numbers).split()
print(values)
numbers_list = [int(val) for val in values]
print(numbers_list)