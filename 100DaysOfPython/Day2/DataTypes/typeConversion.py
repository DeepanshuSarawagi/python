# In this lesson we are going to convert the int data type to string data type

num_char = len(input("What is your name?\n"))
print("Your name has " + str(num_char) + " characters")  # Type conversion happens here. Where we convert
                                                         # the type integer to string
# Or we can use the fStrings
print("Your name has {} characters".format(num_char))

print(70 + float("170.5"))

# Day 2 - Exercise 1 - Print the sum of digits of a number
two_digit_number = input("Type a two digit number of your choice: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Better solution

sum_of_numbers = 0
for i in range(0, len(str(two_digit_number))):
    sum_of_numbers += int(two_digit_number[i])
print(sum_of_numbers)

# Remembering the PEMDASLR rule
print(3 * 3 + 3 / 3 - 3 ** 2)
