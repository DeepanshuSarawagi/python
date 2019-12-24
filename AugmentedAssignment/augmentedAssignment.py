number = "9,323,890,417,862,337,007"
cleanedNumber = ""
for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanedNumber += number[i]
newNumber = int(cleanedNumber)
print(f"The number is {newNumber}")
