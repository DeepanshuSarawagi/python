parrot = "Norwegian Blue"

for char in parrot:
    print(char)

numbers = "9,223,289;865 965:437.116"
separator = ""

for char in numbers:
    if not char.isnumeric():
        separator = separator + char

print(separator)

values = "".join(char if char not in separator else " " for char in numbers).split()

int_values = [int(val) for val in values]
print(int_values)