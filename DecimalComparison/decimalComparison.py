input1 = str(input("Enter a decimal number of your choice: "))
input2 = str(input("Enter a second decimal number of your choice: "))

# input1 = str(3.1567)
# input2 = str(3.156)

print(input1)
print(input2)

print(input1[0] == input2[0])

extractedDecimal = []
for char in input1:
    if char == ".":
        extractedDecimal = input1.split(".")
print(extractedDecimal)

extractedDecimal2 = []
for char in input2:
    if char == ".":
        extractedDecimal2 = input2.split(".")
print(extractedDecimal2)

print(extractedDecimal[1][0:3] == extractedDecimal2[1][0:3])

if extractedDecimal[1][0:3] == extractedDecimal2[1][0:3]:
    print("first three decimals are same")
else:
    print("First three decimals are not same")
