def banner_text(text: str, width: int = 80) -> None:
    """Generate a banner with the given text centered within a specified width.

    Args:
        text (str): The text to be displayed in the banner.
        width (int, optional): The total width of the banner. Defaults to 80.

    Returns:
        str: A string representing the banner with the text centered.
    """
    if len(text) >= width - 4:
        print("EEK!!")
        print("The text is too long to fit in the specified width.")

    if text == "*":
        print("*" * width)
    else:
        output_string = "**{}**".format(text.center(width - 4))
        print(output_string)

banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("Don't panic!")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing!")
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")
