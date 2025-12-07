albums = [("Welcome to my Nightmare!", "Alice Cooper", 1975),
          ("Bad Company", "bad Company", 1974),
          ("NightFlight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the lighting", "Metallica", 1984)]

for album in albums:
    alb, artist, year = album
    print("Album: {}, Artist: {}, Year: {}".format(*album))
    """Notice the * in-front of the album variable which is unpacking the tuple
        This is just a shorthand to unpack the tuple efficiently
    """
