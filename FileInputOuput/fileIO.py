# Opening a text file and reading the lines in it.
jabber = open("sample.txt", 'r')
for lines in jabber:
    print(lines)
jabber.close()
