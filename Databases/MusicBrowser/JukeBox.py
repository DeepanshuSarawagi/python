import sqlite3
import tkinter

conn = sqlite3.connect("music.sqlite")
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
artistsList = tkinter.Listbox(mainWindow)
artistsList.grid(row=1, column=0, rowspan=2, sticky='nsew', padx=(30, 0))
artistsList.config(relief='sunken', border=2)

# Create Albums list box
albumLV = tkinter.Variable(mainWindow)
albumLV.set(('Choose an artists',))
albumList = tkinter.Listbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(relief='sunken', border=2)

# Songs list box
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))
songList = tkinter.Listbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(relief='sunken', border=2)

mainWindow.mainloop()
