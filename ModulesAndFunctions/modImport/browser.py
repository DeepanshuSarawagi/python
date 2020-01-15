import webbrowser

webbrowser.get(using=None)

webbrowser.open("https://www.python.org")

"""Functions with names arguments. sep= and end= are the named arguments defined in the print function"""

for i in range(10):
    print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='; ', end='\t')
