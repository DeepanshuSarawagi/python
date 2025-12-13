from nested_data import albums

while True:
    print("Please choose the album to play (invalid choice exists): ")
    for index, (title, artist, year, songs)  in enumerate(albums):
        print("{}: {}".format(index + 1, title))
    choice = int(input("Enter a choice: "))
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][3]
    else:
        break
    print(albums[choice - 1])
    print(songs_list)
    print()