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
print("*" * 50)
# More ways of reading lines from a file.
with open("sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()
print("*" * 50)

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)  # This will return the lines of file as a list
print("*" * 50)
for line in lines:
    print(line, end='')

