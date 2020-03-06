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
        self.title = title
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
            song (Song): A song to add.
            position(optional[int]): If specified, song will be added to that position in the track list
            - inserting it between other songs if necessary.
            Otherwise, song will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


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


def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(f"{artist_field}:{album_field}:{year_field}:{song_field}")

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # We have just read details for new_artist
                # store the current album in the current artist's collection and then create new Artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None
            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # We have just read a new album for the current artist
                # store the current album in the new artist collection and then create the new album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After having read the last line of the text file, we will have an artist and album that haven't stored,
        # process them now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file."""
    with open('checkfile.txt', 'rw') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print(f"There are {len(artists)} artists.")
    create_checkfile(artists)


# help(Song.__init__)  # This will display the document of __init__ method of class Song
# print(Song.__doc__)  # Alternate method to print the documentation of class and it's objects if any.
