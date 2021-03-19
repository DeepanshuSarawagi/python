with open("Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()  # This will give us the list of names

with open("Input/Letters/starting_letter.txt", mode="r") as file:
    lines = file.read()
    for name in names:
        name = name.strip("\n")
        new_letter = lines.replace("[name],", name + ",")
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
            file.write(new_letter)
