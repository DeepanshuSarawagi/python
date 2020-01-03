"""In this chapter we are going to learn about ranges in Python."""

myList = list(range(10))
print(myList)

"""This will create a list of elements ranging between 0 and 9"""
even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)

"""We can also define the start and end value of ranges. In the above example we have used step of 2 which means 
it will skip every consecutive element in the defined range between 0 and 10 for even and 1 to 10 for odd."""

myString = "abcdefghijklmnopqrstuvwxyz"
print(myString.index('i'))
print(myString[4])

largeNumber = range(1, 10000000, 3)
print(largeNumber)
print(largeNumber[5550])

print()

fives = range(5, 100000, 5)
print(fives[2455])
print()

x = int(input("Please enter a number less than 100000: "))
if x in fives:
    print(f"{x} is divisible by fives")
    print(f"Index of {x} is {fives.index(x)}")
else:
    print(f"{x} is not found in the range")

print()

decimals = range(0, 100)
print(decimals)

print()
myRange = decimals[3:40:3]
print(myRange)
print()
for i in myRange:
    print(i)
print()
for i in range(3, 40, 3):
    print(i)

print()
print(myRange == range(3, 40, 3))
