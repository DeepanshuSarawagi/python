# In this chapter we are learning about tuples in Python.

"""Usually tuples consists of number of values separated by comma. It is a best practice to enclose a tuple in
parenthesis. Refer to below example to understand about tuples."""

data = "Deepanshu", "Sarawagi", 27, "Male"
print(data)
"""Here data variable is tuple with sequence of values separated by comma. """
print("Deepanshu", "Sarawagi", 27, "Male")    # This is not a tuple.
print(("Deepasnhu", "Sarawagi", 27, "Male"))  # This is a tuple, since data is enclosed in parenthesis inside the print
                                              # function.
print(data[1])
print(data[2])

"""Lets create some more tuples to understand more"""
metallica = ("Ride the lightning", "Metallica", 1984)
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# metallica[0] = "Master of Puppets"
"""Tuples are immutable which means once created, they cannot be changed. But thats not the case with lists.
Look at the below example to understand more."""

metallica2 = ["Ride the lightning, Metallica", 1984]
print(metallica2)
print()
metallica2[0] = "Master of Puppets"
print(metallica2)

"""As you can see from line 26 to 30, we created a list called metallica2 and changed the first item in the list and
it worked, however, changing the items in a tuple is not possible since they are immutable."""

"""However, there is a work around if we want to change the contents of the tuple. Lets try to understand the below 
code."""

imelda = "More Mayhem", "Emilda May", 2011
print(imelda)
"""Good thing about tuples is that they support indexing hence we can something like to change the imelda[1] from 
"Emilda May" to "Imelda May"""
print()
imelda = imelda[0], "Imelda May", imelda[2]
print(imelda)

"""There are two important concepts here to understand that tuples are immutable but that doesn`t mean that your 
variable can't be assigned new objects of that type. We have assigned new object to the variable imelda to correct the 
typo from "Emilda" to "Imelda". We just assigned new objects to that variable."""

"""We can also unpack tuples like this."""

# # song, artist, year = imelda
# print(song)
# print(artist)
# print(year)
imelda = imelda[0], imelda[1], imelda[2], ((1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town "
                                                                                                     "Waltz"))
# print(imelda)
# title, artist, year, track1, track2, track3, track4 = imelda
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track1)
# print(track3)
# print(track4)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for track in tracks:
    print(track, end="\t")

print()

for track in tracks:
    title, song = track
    print(f"Title No. {title}, Track Name: {song}")

"""Although tuples are immutable but what happens when we create a tuple which contains a mutable objects such as lists.
Lets get to below code and see."""

coldplay = ("Everyday Life", "Chris Martin", 2019, ([(1, "Sunrise"), (2, "Church"), (3, "Trouble in Town"), (4, "Orpahns")]))

album, artist, year, tracks = coldplay
print(coldplay)
coldplay[3].append((5, "Everyday Life"))
print()
print(coldplay)

"""As you can we have a created a tuple object called coldplay which contains a mutable object called tracks.
The list tracks has several songs of the album. On line 88, we appended a new song in the album thereby changing the 
track list. Hence, a mutable object list can be changed inside immutable object tuple."""

print(album)
print(artist)
print(year)
tracks.append((6, "Old Friends"))
for song in tracks:
    trackNo, trackName = song
    print("\t" "Track No. {} and Track name is {}".format(trackNo, trackName))
"""We also unpacked the tuple in line 86 and then again in line 99, we appended one more item in the list tracks"""
