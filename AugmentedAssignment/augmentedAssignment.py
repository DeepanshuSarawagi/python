number = "9,323,890,417,862,337,007"
cleanedNumber = ""
for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanedNumber += number[i]
newNumber = int(cleanedNumber)
print(f"The number is {newNumber}")

# simple examples of Augmented Assignments

x = 23
x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x /= 4
print(x)

x **=2
print(x)

x %= 60
print(x)

greeting = "Good "
greeting += "morning "
print(greeting)

greeting *= 5
print(greeting)

# Coding exercise

number = 5
multiplier = 8
answer = 0

# add your loop after this comment
for i in range(answer, multiplier):
    answer += number

print(answer)
