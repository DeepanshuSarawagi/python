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
