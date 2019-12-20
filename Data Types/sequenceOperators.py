# String concatenation

string1 = "He's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords."

print(string1 + string2 + string3 + string4 + string5)

# We can also multiply a string.

print("Hello " * 5)  # This will print the string sequence 5 times.
# print("Hello" * 5 + 4)   This will not work because string once multiplied cannot be concatenated with int data type.
print("Hello " * (5 + 4))

# We can also find is string is a substring of another string.
today = "friday"
print("day" in today)   # This will evaluate to true
print("fri" in today)   # This will evaluate to true
print("thur" in today)  # This will evaluate to false
