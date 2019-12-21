# In this lesson we are going to learn more about the string formatting using replacement fields.

for i in range(1,13):
    print("No: {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# number after the color in the replacement field sets the width. Which means, :2 will reserve 2 spaces on the screen,
# :4 will reserve 4 spaces on the screen.

# Learn how to left align the value

print()

for i in range(1,13):
    print("No: {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

# The less than symbol left aligns the characters in the output.
print()

# Learn how to center align the characters using the caret symbol

for i in range(1,13):
    print("No: {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()
# we are going to learn about the precision fields in python. Let's try to understand this by running the below code.
# We will be calculating the value of pi and get the output in floating point value. The maximum precision fields python
# can support is between 51 and 53.

print("The value of pi is approximately {0:12}".format(22 / 7))
print("The value of pi is approximately {0:12f}".format(22 / 7))
print("The value of pi is approximately {0:12.50f}".format(22 / 7))
print("The value of pi is approximately {0:52.50f}".format(22 / 7))
print("The value of pi is approximately {0:62.50f}".format(22 / 7))
print("The value of pi is approximately {0:<72.50f}".format(22 / 7))
print("The value of pi is approximately {0:<72.54f}".format(22 / 7))

print()
# As you can compare the output after executing the code in line 34 and 35, python is able to get the value of pi upto
# 51 places after the decimal point (precision value)

# We are going to learn about f-strings.
# we can also calculate the value of Pi and then using print function display the result. This time we wont use
# .format() method in the print function.

Pi = (22 / 7)
print(f"The value of Pi is approximately {Pi:12.50f}")

# Remember that f-strings will not work for python 3.6 and earlier.
