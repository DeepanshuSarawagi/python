"""
In this lesson we are going to learn how to catch exceptions when it is raised in Python.
Look out for below examples.
"""

try:
    with open("a_file.txt") as file:
        file.read()
except FileNotFoundError:
    print("There was an error. The file is not found.")
