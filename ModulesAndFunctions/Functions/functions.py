def center_text(text):
    if text == 'quit':
        print("You have decided to quit")
    else:
        text = str(text)
        left_margin = (80 - len(text)) // 2
        print(" " * left_margin, text)


text = input("Please enter a text: ")
center_text(text)


def centered_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    text = text.strip(":")
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


with open("centered.txt", mode='w') as centered_file:
    centered_text("spam", 1, 2, "eggs", "number", sep=":", file=centered_file)
    centered_text("spam and spam", file=centered_file)
    centered_text("spam, spam and spam", file=centered_file)
    centered_text("text without spam", file=centered_file)
