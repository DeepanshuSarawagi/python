import os


def list_directories(s):
    tab_stop = 0
    if os.path.exists(s):
        print(f"Directory listings of {s}")
        dir_list(s)
    else:
        print(f"The following path {s} doesn't exist")


listing = os.walk('/Users/deepanshusarawagi/Desktop/Learning/python')
for root, directories, files in listing:
    print(root)
    for d in directories:
        print(d)
    for file in files:
        print(file)
