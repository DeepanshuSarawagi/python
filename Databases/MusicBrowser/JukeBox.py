import sqlite3
import tkinter

conn = sqlite3.connect("music.sqlite")
mainWindow = tkinter.Tk()
mainWindow.title("Music Juke Box")
mainWindow.geometry("1024x768")

mainWindow.mainloop()
