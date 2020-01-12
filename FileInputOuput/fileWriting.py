# Writing something to a file.
cities = ["Chennai", "Bengaluru", "Delhi", "Mumbai", "Pune", "Jaipur"]
with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file, end='\n', flush=True)

# Since we are using the with statement, we need not explicity close the file.
# whenever you write some data to a file/enternal device, processor first writes the data in the buffer and from there
# buffer then writes to other devices. Since this is a small file, we may not slow down the process of writing the day.
# Consider the scenario when you want huge amount of data to be printed on the screen for the user and keep that kind
# of data in the buffer memory is not a good idea. Here comes the importance of flush=True parameter while writing
# something to a file.

# Now the we have written the data, let's try to read from the file.

cities_read = []
with open("cities.txt", 'r') as city_file_read:
    for city in city_file_read:
        cities_read.append(city.strip('\n'))
print(cities_read)
for city in cities_read:
    print(city)

imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"),
                                             (3, "Mayhem"), (4, "Kentish Town Waltz"))
with open("imelda.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file, flush=True)

with open("imelda.txt", 'r') as imelda_file_read:
    contents = imelda_file_read.readline()
imelda_read = eval(contents)  # This is done to evaluate the contents from a value if its tuple.
print(imelda_read)
title, artist, year, tracks = imelda_read
print(title)
print(artist)
print(year)
print(tracks)
for track in tracks:
    trackNo, trackName = track
    print(f"Song {trackNo} is {trackName}")
