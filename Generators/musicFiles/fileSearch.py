import os
import fnmatch


def find_albums(root: str, artist_name: str):
    for path, directories, files in os.walk(root, topdown=True):
        for artist in fnmatch.filter(directories, artist_name):
            sub_dir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(sub_dir):
                for album in albums:
                    yield os.path.join(album_path, album), album


album_list = find_albums("music", "Aerosmith")

for a in album_list:
    print(a)
