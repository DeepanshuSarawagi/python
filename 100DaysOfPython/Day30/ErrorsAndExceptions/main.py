"""
In this lesson we are going to learn how to catch exceptions when it is raised in Python.
Look out for below examples.
Remember that exceptions are raised chronologically in the code line by line. In the below case KeyError will not be
raised first time when we run the program. FileNotFoundException will be raised and the code in except clause block of
code will be executed.
However, when we run the program second time, since there wont be any FileNotFoundException since it has been handled
in the previous run, KeyError will be raised and it will be handled.
"""

try:
    file = open("a_file.txt")
    # file.read()
    a_dictionary = {
        "key": "value"
    }
    print(a_dictionary["abc"])  # Deliberately raising KeyError to demonstrate below except clause
except KeyError as key_error:
    print("The key {} does not exist.".format(key_error))
except FileNotFoundError:
    print("The file is not found. Creating one.")
    with open("a_file.txt", "w") as file:
        file.write("Writing some data\n")
