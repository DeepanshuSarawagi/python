from nested_data import albums

while True:
    print("Please choose the album to play (invalid choice exists): ")
    for index, (title, artist, year, songs)  in enumerate(albums):
        print("{} - {}, {}, {}, {}".format(index + 1, title, artist, year, songs))
    break