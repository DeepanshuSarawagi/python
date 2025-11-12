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
