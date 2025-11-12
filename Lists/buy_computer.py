available_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]
current_choice = "-"
computer_parts = []
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
print(valid_choices)
while current_choice != "0":
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        computer_parts.append(available_parts[int(current_choice) - 1])

    else:
        print("Please add options from the list below:")
        """enumerate function adds a counter to an iterable and returns it"""
        # for part in available_parts:
        #     print("{0} - {1}".format(available_parts.index(part) + 1, part))
        for number, part in enumerate(available_parts):
            print("{0} - {1}".format(number + 1, part))
    current_choice = input("Please enter your choice based on menu: ")

print(computer_parts)
