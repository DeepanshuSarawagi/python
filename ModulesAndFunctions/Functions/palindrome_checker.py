def is_palindrome(string: str) -> bool:
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

def palindrome_sentence(sentence: str) -> bool:
    """
    Check if the given sentence is a palindrome, ignoring spaces and punctuation.

    Args:
        sentence (str): The sentence to check.
    Returns:
        bool: True if the sentence is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():  # Consider only alphanumeric characters
            string += char.lower()
    return is_palindrome(string)

if __name__ == "__main__":
    word = input("Please enter a word to check: ")
    if is_palindrome(word):
        print(f'"{word}" is a palindrome.')
    else:
        print(f'"{word}" is not a palindrome.')
    sentence_to_check = input("Please enter a sentence to check: ")
    if palindrome_sentence(sentence_to_check):
        print(f'"{sentence_to_check}" is a palindrome.')
    else:
        print(f'"{sentence_to_check}" is not a palindrome.')
