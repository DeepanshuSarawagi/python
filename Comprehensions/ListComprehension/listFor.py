print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Please enter a number and i'll tell you its square: "))


squares = []
for number in numbers:
    print(squares.append(number ** 2))

index_pos = numbers.index(number)
print(index_pos)
print()
print(squares[index_pos])

