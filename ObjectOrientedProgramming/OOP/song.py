class Song:

    """Class to represent a song

    Attributes:
        title(str): Title of the song.
        artist(str): An artist of the song representing song creator.
        duration(int): Duration of the song in seconds. May be zero.
    """
    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title(str): Initialises the title attribute.
            artist(Artist): An object representing the song's creator.
            duration(Optional[int]): Initial value for the 'duration' attribute.
                Will default to zero if not specified
        """
        self.name = title
        self.artist = artist
        self.duration = duration


class Album:
    """ Class to represent an Album using it's track list.
    Attributes:
        name(str): The name of the album.
        year(int): The year album was released.
        artist: (Artist): The artist responsible for the album.
                If not specified, the artist will default to an artist with the name "various artists"
        tracks (list[song]): list of the songs in the album.

    Methods:
        addSong: Used to add a new song to the album's track list.
    """
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list
        Args:
            song (Song): The title of the song to add.
            position(optional[int]): If specified, song will be added to that position in the track list
            - inserting it between other songs if necessary.
            Otherwise, song will be added to the end of the list.
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """Basic class to store artist details.
    Attributes:
        name (str): The name of the artist.
        albums (List(Album]): A list of the album by this artist.
            The list includes only those albums in this collections,
            it is not an exhaustive list of all the albums by this artist.
    Methods:
         add_album: Used to add a new album to the artist`s list of albums.
    """
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Adds a new album to the list.
        Args:
             album(Album): An Album object to add to the list.
             If the album is already present, it will not be added to the list(although it is yet to be implemented)
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """"Add a new song to the collection of the albums.
            This method will add the song to the album in the collection.
            A new album will be created in the collection if it doesn't already exists.
            Args:
                name (str): The name of the album
                year (int): The year the album was produced
                title (str): The title of the song
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(f"{name} not found")
            album_found = Album(name, year, self)
            self.add_album(album_found)
        else:
            print(f"Found album: {name}")
        album_found.add_song(title)


def find_object(field, object_list):
    """Check object_list to see if the object with a 'name' attribute equal to the 'field' attribute, if so
    return it."""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []
    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(f"{artist_field}:{album_field}:{year_field}:{song_field}")

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(artist_field, year_field, song_field)

    return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file."""
    with open('checkfile.txt', 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.name}".format(new_artist, new_album, new_song), file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print(f"There are {len(artists)} artists.")
    create_checkfile(artists)


# help(Song.__init__)  # This will display the document of __init__ method of class Song
# print(Song.__doc__)  # Alternate method to print the documentation of class and it's objects if any.
