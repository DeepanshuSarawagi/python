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

mainWindow.mainloop()
