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

"""Lets create some more tuples to understand more"""
metallica = ("Ride the lightning", "Metallica", 1984)
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# metallica[0] = "Master of Puppets"
"""Tuples are immutable which means once created, they cannot be changed. But thats not the case with lists.
Look at the below example to understand more."""

metallica2 = ["Ride the lightning, Metallica", 1984]
print(metallica2)
print()
metallica2[0] = "Master of Puppets"
print(metallica2)

"""As you can see from line 26 to 30, we created a list called metallica2 and changed the first item in the list and
it worked, however, changing the items in a tuple is not possible since they are immutable."""
