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

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25::-1]
print(backwards)
print(letters[16:13:-1])
print(letters[4::-1])
print(letters[-1:-9:-1])

# Common python slicing idioms
print(letters[-4:])
print(letters[-1])

age = 25
# print("My age is " + age + "years.") # This wont works since we cannot concatenate string with int.
# To overcome this issue, we will use f-strings.
print(f"My age is {age} years old.")
# We can also print the float value like this
print(f"Value of Pi is approximately {22 / 7:12.51f}")
# We can also use precision along with variablized value.
pi = 22 / 7
print(f"Value of Pi is approximately {pi:12.51f}")