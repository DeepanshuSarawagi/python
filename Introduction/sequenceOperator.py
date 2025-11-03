# Sequence operators, below example will demonstrate how we can concatenate strings

string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords "
print(string1 + string2 + string3 + string4 + string5)

# String multiplier range
print("Hello " * 5)
# print("Hello " * 5 + 4)  # This will not work since we can't concatenate string with int
print("Hello " * (5+4))
print("Hello " * 5 + "4")