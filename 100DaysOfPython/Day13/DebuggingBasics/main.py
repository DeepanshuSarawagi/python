############DEBUGGING#####################

# Describe Problem
def my_function():
    # for i in range(1, 20):
    for i in range(1, 21):  # This is the bug. We had to change the range from 20 to 21 since the upper bound in range
        # fn is not inclusive
        if i == 20:
            print("You got it")


my_function()

# Reproduce the Bug
from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)  # this is the bug. We have to change the upper bound limit to 5 since upper bound in
# randint() fn is inclusive and while accessing the list, the index always starts from 0. And the 6th element will be
# accessed as list[5]
dice_num = randint(1, 5)
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:  # This is the bug. We need to include the operand = in this line of code.
# Whenever the user enters the year 1994 there was no way computer can evaluate to if statements
if 1980 < year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# Fix the Errors
# age = input("How old are you?")  # This is the bug here. When we get the user input, it is always in STRING datatype.
# We need to cast the input to int datatype.
age = int(input("How old are you?"))
if age > 18:
    # print("You can drive at age {age}.")  # Second error is the poor indentation and then the print statement was not
    # a f"string"
    print(f"You can drive at age {age}.")

# Print is Your Friend
# pages = 0
# word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))  # This is again a bug since we did a equivalent
# assignment rather than assigning the user input to a variable
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


# Use a Debugger


def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    # b_list.append(new_item)  # This is the bug here. This line of code was outside of for loop hence all the
    # items in the list were not appended.
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
