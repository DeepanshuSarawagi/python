import os


def list_directories(s):

    def dir_list(d):
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print(f"Directory listings of {s}")
        dir_list(s)
    else:
        print(f"The following path {s} doesn't exist")


list_directories('/Users/deepanshusarawagi/Desktop/Learning/python')

# listing = os.walk('/Users/deepanshusarawagi/Desktop/Learning/python')
# for root, directories, files in listing:
#     print(root)
#     for d in directories:
#         print(d)
#     for file in files:
#         print(file)
