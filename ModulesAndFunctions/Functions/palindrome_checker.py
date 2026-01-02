def is_palindrome(string):
    """
    Check if the given string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards,
    ignoring case, spaces, and punctuation.

    Args:
        string (str): The string to check.
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    backwards = string[::-1]
    return string.lower() == backwards.lower()

if __name__ == "__main__":
    print(is_palindrome("malayalam"))
