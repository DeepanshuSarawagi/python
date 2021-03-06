import tkinter
import os

mainWindow = tkinter.Tk()
mainWindow.title("Grid Demo")
mainWindow.geometry("640x480-8-200")
mainWindow['padx'] = 8
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

# Add padding in the timeFrame widget to move the spinners and make it look more presentable
timeFrame['padx'] = 36

# Add date frame
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')

# Add the date Labels
dayLabel = tkinter.Label(dateFrame, text='Day')
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel = tkinter.Label(dateFrame, text='Month')
monthLabel.grid(row=0, column=1, sticky='w')
YearLabel = tkinter.Label(dateFrame, text='Year')
YearLabel.grid(row=0, column=2, sticky='w')

# Add date spinners
daySpinner = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
daySpinner.grid(row=1, column=0)
monthSpinner = tkinter.Spinbox(dateFrame, width=5, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July',
                                                           'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
monthSpinner.grid(row=1, column=1)
YearSpinner = tkinter.Spinbox(dateFrame, width=5, from_=1930, to=2099)
YearSpinner.grid(row=1, column=2)

# Add OK and Cancel buttons
okButton = tkinter.Button(mainWindow, text='OK')
okButton.grid(row=4, column=2, sticky='e')
okButton['padx'] = 8
cancelButton = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.quit)
cancelButton.grid(row=4, column=3, sticky='w')
cancelButton['padx'] = 8

mainWindow.mainloop()
print(rbValue.get())
