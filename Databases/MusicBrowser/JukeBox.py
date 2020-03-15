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

mainWindow.mainloop()
