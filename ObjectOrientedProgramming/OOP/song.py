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
        album_name(str): The name of the album.
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


help(Song.__init__)  # This will display the document of __init__ method of class Song
print(Song.__doc__)  # Alternate method to print the documentation of class and it's objects if any.
