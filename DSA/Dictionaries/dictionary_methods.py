"""
In this lesson we are going to learn the different dictionary methods
"""

my_dict = {
    "name": "Deepanshu",
    "age": 27,
    "location": "India",
    "profession": "IT Engineer"
}

# Copy method return the shallow copy of a dictionary. It doesnt modify the original dictionary
new_dict = my_dict.copy()
print(my_dict)
print(new_dict)

"""
fromkeys() method returns the dictionary with the given sequence of elements as keys in the form of parameters
"""

dict_2 = {}.fromkeys([1, 2, 3], 0)  # Remember that all the keys will have the same value as 0
print(dict_2)
