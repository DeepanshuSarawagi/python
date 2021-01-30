# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Type a two digit number. Digits should be between 1 and 3."
                 "Eg: 23, 31, 11, 12, 32, 13 ")
column_position = int(position[0]) - 1
row_position = int(position[1]) - 1
map[row_position][column_position] = "X"
print(f"{map[0]}\n{map[1]}\n{map[2]}")
