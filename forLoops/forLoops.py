for i in range(1, 20):
    print(f"i is now {i}.")

number = "9,223,456,865,207,590,007"
cleanedNumber = ''
for i in range(0, len(number)):
    if number[i] in "0123456789":
        print(number[i], end='')
print()

for char in number:
    if char in "0123456789":
        cleanedNumber = cleanedNumber + char
newNumber = int(cleanedNumber)
print(newNumber)
print()
for state in ["not pinin", "no more", "bereft of life", "a stiff"]:
    print("This parrot is " + state)

# introducing steps in for loops. In the below example, the third number in range is step; which means python is going
# to skip to the number in sequence. Lets run the code below to understand more.

for a in range(0, 100, 5):
    print(f"a is now {a}")

# As you can see, after executing the code, python has skipped to every 5th number in the range from 0 to 100.

# nesting for loops inside a for loop.
print()
for i in range(1, 16):
    for j in range(1, 11):
        print("{0:2} times {1:2} is {2:3}".format(i, j, i * j))
    print(50 * "=")

# A simple program to extract capitals

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for i in range(0, len(quote)):
    if quote[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(quote[i], end="\t")
print()

# Coding challenge on Udemy. Write a program so that it calculates the no. of segments and each segment length of
# Ip address

# ipAddress = input("Please enter a IP address: ")
# segment = 1
# segment_len = 0
#
# for char in ipAddress:
#     if char == ".":
#         print("Segment {} has {} characters".format(segment, segment_len))
#         segment += 1
#         segment_len = 0
#     else:
#         segment_len += 1
# if char != ".":
#     print("Segment {} has {} characters".format(segment, segment_len))
# There is a better way of doing this. We can add a period; "." at the end of the Ip address this way we dont have to
# check for the last if condition.

ipAddress = input("Enter an IP address: ")
if ipAddress[-1] != ".":
    ipAddress += "."

segment = 1
segment_len = 0

for char in ipAddress:
    if char == ".":
        print("Segment {} has {} characters".format(segment, segment_len))
        segment += 1
        segment_len = 0
    else:
        segment_len += 1
