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
                will default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration


help(Song.__init__)  # This will display the document of __init__ method of class Song
