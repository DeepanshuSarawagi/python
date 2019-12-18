# In this lesson we are going to learn about the escape characters in the strings.
splitString = "This string has been\nsplit over \nseveral \ntimes."
print(splitString)
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# Below example shows how to escape single quotes or double quotes in a string using the backslash.
print("The pet shop owner said, \"No, No 'e 's... uh, He's resting\". ")

# Or we can print the above line like this.

print('The pet shop owner said, "No, No \'e \'s... uh, He\'s resting." ')
# We can also use the triple quotes like this which will not require us to use the backslash.
print("""The pet shop owner said, "No, No 'e 's... uh, He's resting". """)

# Another way of splitting strings is using the triple quotes. Python recognizes that string has not ended until it
# finds the closing triple quotes.

anotherSplitString = """This string has been 
split over
several 
lines."""
print(anotherSplitString)
# Below example shows how to escape the backslash character. In this example, consider we need a backslash character in
# the output then we need to tell python to escape it. We can get that done in two ways.
print("C:\\Users\deepanshusarawagi\\notes.txt")
# We can create a raw string by adding the letter "r" in front of the string.
print(r"C:\Users\deepanshusarawagi\notes.txt")

