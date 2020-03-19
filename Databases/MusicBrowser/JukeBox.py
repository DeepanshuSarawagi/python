import sqlite3
import tkinter

conn = sqlite3.connect("music.sqlite")


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):

        super().__init__(window, **kwargs)
        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ",".join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def requery(self):
        print(self.sql_select + self.sql_sort)  # TODO remove this line once testing is complete
        self.cursor.execute(self.sql_select + self.sql_sort)

        # clear the list box contents before re-laoding
        self.clear()

        # reload the data
        for value in self.cursor:
            self.insert(tkinter.END, value[0])


def get_albums(event):
    lb = event.widget
    if lb.curselection():  # fix the IndexError: tuple out of range
        index = lb.curselection()[0]
        artist_name = lb.get(index),
        # get the artist id from the database
        artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name=?", artist_name).fetchone()
        alist = []
        for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist = ? ORDER BY albums.name", artist_id):
            alist.append(row[0])
        albumLV.set(tuple(alist))
        songLV.set(("Choose an albums",))


def get_songs(event):
        lb = event.widget
        if lb.curselection():
            index = int(lb.curselection()[0])
            album_name = lb.get(index),

            # get the album is from the database
            album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name = ?", album_name).fetchone()
            alist = []
            for x in conn.execute("SELECT songs.title FROM songs WHERE songs.album = ? ORDER BY songs.track", album_id):
                alist.append(x[0])
            songLV.set(tuple(alist))


mainWindow = tkinter.Tk()
mainWindow.title("Music Juke Box")
mainWindow.geometry("1024x768")

# configure columns
mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)  # Add spacer column in the end

# configure rows
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# Create Labels

tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# Create Artists list box
artistsList = DataListBox(mainWindow, conn, "artists", "name")
artistsList.grid(row=1, column=0, rowspan=2, sticky='nsew', padx=(30, 0))
artistsList.config(relief='sunken', border=2)

# insert the artist list data in the artist listbox from database
# for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
#     # print(artist)
#     artistsList.insert(tkinter.END, artist[0])

artistsList.requery()
artistsList.bind('<<ListboxSelect>>', get_albums)

# # artist scrollbar
# artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistsList.yview)
# artistScroll.grid(row=1, column=0, rowspan=2, sticky='nse')
# artistsList['yscrollcommand'] = artistScroll.set

# Create Albums list box
albumLV = tkinter.Variable(mainWindow)
albumLV.set(('Choose an artists',))
albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))
albumList.requery()
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(relief='sunken', border=2)

albumList.bind('<<ListboxSelect>>', get_songs)

# albumScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumList.yview)
# albumScroll.grid(row=1, column=1, sticky='nse')
# albumList['yscrollcommand'] = albumScroll.set

# Songs list box
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))
songList = DataListBox(mainWindow, conn, "songs", "title", sort_order=("track", "title"))
songList.requery()
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(relief='sunken', border=2)

testList = range(1, 100)
albumLV.set(tuple(testList))
mainWindow.mainloop()
conn.close()
