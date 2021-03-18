with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)

with open("my_file.txt", "w") as file:
    file.write("This is a new text")

with open("new_file.txt", "w") as file:
    file.write("Hello, this is a new file. \nI`m writing a new line here."
               "\nThis is a third line in the text file.")

with open("new_file.txt", "a") as file:
    file.write("\nI have appended a line")

with open("new_file.txt", "r") as file:
    content = file.read()
    print(content)