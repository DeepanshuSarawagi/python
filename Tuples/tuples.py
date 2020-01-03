# In this chapter we are learning about typles in Python.

"""Usually tuples consists of number of values separated by comma. It is a best practice to enclose a tuple in
parenthesis. Refer to below example to understand about tuples."""

data = "Deepanshu", "Sarawagi", 27, "Male"
print(data)
"""Here data variable is tuple with sequence of values separated by comma. """
print("Deepanshu", "Sarawagi", 27, "Male")    # This is not a tuple.
print(("Deepasnhu", "Sarawagi", 27, "Male"))  # This is a tuple, since data is enclosed in parenthesis inside the print
                                              # function.
print(data[1])
print(data[2])
