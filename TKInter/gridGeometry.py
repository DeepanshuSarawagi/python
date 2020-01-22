import tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry("640x480-8-200")

label = tkinter.Label(mainWindow, text="Hello World")
label.grid(row=0, column=1)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=2)
canvas.grid(row=0, column=1)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky="n")

button1 = tkinter.Button(rightFrame, text="Button1")
button1.grid(row=0, column=0)
button2 = tkinter.Button(rightFrame, text="Button2")
button2.grid(row=1, column=0)
button3 = tkinter.Button(rightFrame, text="Button3")
button3.grid(row=2, column=0)

# configure the columns

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)

mainWindow.mainloop()
