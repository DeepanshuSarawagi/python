# Opening a text file and reading the lines in it.
jabber = open("sample.txt", 'r')
for lines in jabber:
    print(lines)
jabber.close()

# There is a better way of performing file I/O operations using the "with" statement. Advantage of using with statement
# is that we need not explicitly specify a file to close.

with open("sample.txt", 'r') as f:
    for lines in f:
        if "JAB" in lines.upper():
            print(lines, end='')
