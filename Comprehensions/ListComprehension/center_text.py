def center_text(*args):

    text = "-".join([str(arg) for arg in args])
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


center_text("spam and eggs")
center_text("spam, eggs and spam")
center_text("spam, spam and more spam")
center_text(12)
center_text("spam", "eggs", 5, 12, "spam")
