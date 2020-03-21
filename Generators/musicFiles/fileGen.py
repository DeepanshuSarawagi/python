import os

root = "music"

# for f in os.walk(root, topdown=True):
#     print(f)
# as we can learn from os.walk it prints tuples of three values which is
# path, directory, files. We are going to unpack the tuple and print them

for path, directories, files in os.walk(root, topdown=True):
    print(path)
    print(directories)
    print(files)
    input()
    # for f in files:
    #     print(f"\t{f}")

