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
