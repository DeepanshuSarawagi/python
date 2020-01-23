import tkinter
import os

mainWindow = tkinter.Tk()
mainWindow.title("Grid Demo")
mainWindow.geometry("640x480-8-200")

label = tkinter.Label(mainWindow, text='Tkinter Grid Demo')
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky="nsew", rowspan=2)
fileList.config(relief='sunken', borderwidth=2)

for zone in os.listdir('/usr/bin'):
    fileList.insert(tkinter.END, zone)  # inserting the directory list in the list box

# Add scroll bar in the list box
scrollList = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
scrollList.grid(row=1, column=1, rowspan=2, sticky='nsw')

# This allows to join the action of scroll bar to the list box whenever
# the scroll bar is moved using the keyboard or when an item is added

fileList['yscrollcommand'] = scrollList.set

# Frame for the radio buttons on the grid demo box

optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

# Adding the tkinter intVar() and assigning it to the variable. This is done for the radio buttons so that when
# one option is selected, other would automatically deselected

rbValue = tkinter.IntVar()
rbValue.set(3)

# Creating Radio buttons
radioButton1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
radioButton2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
radioButton3 = tkinter.Radiobutton(optionFrame, text='Time Stamp', value=3, variable=rbValue)

radioButton1.grid(row=0, column=0, sticky='w')
radioButton2.grid(row=1, column=0, sticky='w')
radioButton3.grid(row=2, column=0, sticky='w')

# Add result label
resultLabel = tkinter.Label(mainWindow, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')
# Add result box
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# Frame for the time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')
# Add the time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)

mainWindow.mainloop()
print(rbValue.get())