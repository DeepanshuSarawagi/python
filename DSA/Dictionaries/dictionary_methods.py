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

print(my_dict.get("gender", "Male"))  # This method returns the value of key if exists in the dictionary else it will
# return the value we specified as parameter in get() method. If we do not pass the value paramter and if the key
# doesn't exist then it returns None. refer to below example
print(my_dict.get("city"))

print(my_dict.items())  # This will return the list of key-value pairs as tuples

print(my_dict.keys())  # This will return the list of keys in the dictionary

print(my_dict.values())  # This will return the list of values in the dictionary
