for i in range(1,20):
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
# to skip the number in sequence. Lets run the code below to understand more.

for a in range(0, 100, 5):
    print(f"a is now {a}")

# As you can see, after executing the code, python has skipped every 5th number in the range from 0 to 100.
