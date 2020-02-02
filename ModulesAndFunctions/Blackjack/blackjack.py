import tkinter
import random

mainWindow = tkinter.Tk()

# setup the screen and frames for dealer and player

mainWindow.title('Black Jack')
mainWindow.geometry('640x480-8-200')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=2, background='green')
card_frame.grid(row=1, column=0, columnspan=3, rowspan=2, sticky='ew')

mainWindow.mainloop()