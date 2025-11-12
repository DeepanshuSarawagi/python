shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
print()
shopping_list += ['cookies']

"""
Since list is mutable, the id's are same for both lists unlike boolean and string as we saw in immutable.py
"""
print(shopping_list)
print(id(shopping_list))
print(id(another_list))

"""One thing to note here is that there is just one list in this python program. This is because both `shopping_list and `another_list` are pointing to the same object. 
Any change made to the object will be reflected in both lists.
"""

print(another_list is shopping_list)
print(another_list)

"""To confirm the theory, we can use the following code:
Plus we can see that the id's are same which means they are pointing to the same object.
"""
a = b = c = d = e = f = another_list
print(a is another_list)
print(b is another_list)
print(c is another_list)
print(d is another_list)
print(e is another_list)
print(f is another_list)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))
