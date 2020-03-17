# def print_backwards(*args, **kwargs):
#
#     """Just similar to *args which unpacks the tuple of arguments passed as parameter in functions, **kwargs will
#     unpack the dictionary of named keywords which is passed. In the below program, we will define a simple function
#     without specifying the named parameter file= yet pass it as an argument while calling the method"""
#     print(kwargs.keys())
#     print(kwargs)
#     kwargs.pop('end', None)
#     print(kwargs)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)


def print_backwards(*args, **kwargs):

    # print(kwargs.keys())
    # print(kwargs)
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', None)
    # print(kwargs)
    for word in args[:0:-1]:
        print(word[::-1], end=sep_character, **kwargs)
    # print(end=end_character)
    print(args[0][::-1], end=end_character, **kwargs)


with open('backwards.txt', 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print('another string')

print()
print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
