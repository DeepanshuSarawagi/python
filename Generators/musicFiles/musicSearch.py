import os
import fnmatch

# args0 = input("Please enter the path you want to search the file: ")
args1 = input("Please enter the file extension you want to search: ")


def find_music(start: str, extension: str):
    for path, directories, files in os.walk(start):
        for song in fnmatch.filter(files, f"*.{extension}"):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, song)


for f in find_music("music", args1):
    print(f)
