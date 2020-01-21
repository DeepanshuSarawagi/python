import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry("640x480")

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side="top")

canvas = tkinter.Canvas(mainWindow, relief="raised", borderwidth=2)
canvas.pack(side="left")
# canvas.pack(side="left", fill=tkinter.BOTH, expand=True)

button1 = tkinter.Button(mainWindow, text="button1")
button2 = tkinter.Button(mainWindow, text="button2")
button3 = tkinter.Button(mainWindow, text="button3")

button1.pack(side="left", anchor="n")
button2.pack(side="left", anchor="e")
button3.pack(side="left", anchor="s")
mainWindow.mainloop()
