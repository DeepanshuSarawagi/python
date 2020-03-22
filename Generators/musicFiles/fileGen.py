import os

root = "music"

# for f in os.walk(root, topdown=True):
#     print(f)
# as we can learn from os.walk it prints tuples of three values which is
# path, directory, files. We are going to unpack the tuple and print them

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            song_details = f[:-5].split(' - ')
            print(song_details)
        print("*" * 40)
    # print(directories)
    # print(files)
    # input()
    # for f in files:
    #     print(f"\t{f}")

