with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)

with open("my_file.txt", "w") as file:
    file.write("This is a new text")