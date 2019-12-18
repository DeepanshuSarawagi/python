# In this lesson we are going to learn about the numeric operators in the Python.

a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# We will learn about the operator precedence in the following example.

print(a + b / 3 - 4 * 12)  # This should evaluate to -35.0 as per the BODMAS rule. If you have got it 12, you are wrong.
print(a + (b/3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)  # This will evaluate to 12.0.
print(a / (b * a) / b)
