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
