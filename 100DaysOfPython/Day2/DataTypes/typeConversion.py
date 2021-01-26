# In this lesson we are going to convert the int data type to string data type

num_char = len(input("What is your name?\n"))
print("Your name has " + str(num_char) + " characters")  # Type conversion happens here. Where we convert
                                                         # the type integer to string
# Or we can use the fStrings
print("Your name has {} characters".format(num_char))
