def center_text(text):
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)

text = input("Please enter a text: ")
center_text(text)
