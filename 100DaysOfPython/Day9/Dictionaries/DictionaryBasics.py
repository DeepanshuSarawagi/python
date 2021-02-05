# In this lesson we are going to learn about the dictionaries in Python

programming_dictionary = {"bug": "A piece of code which prevents the program from running as expected",
                          "function": "A program which can be called again and again"}

for keys in programming_dictionary.keys():
    print("{}: {}".format(keys, programming_dictionary[keys]))
