import tkinter

mainWindow = tkinter.Tk()
mainWindow.title('Calculator')
mainWindow.geometry('320x240')
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.columnconfigure(4, weight=1)
mainWindow.columnconfigure(5, weight=1)
mainWindow.columnconfigure(6, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)
mainWindow.rowconfigure(6, weight=1)
mainWindow.rowconfigure(7, weight=1)
mainWindow['padx'] = 8
mainWindow['pady'] = 8
resultFrame = tkinter.Entry(mainWindow, width=2)
resultFrame.grid(row=0, column=0, columnspan=3, sticky='new')

buttonFrame = tkinter.Frame(mainWindow, width=5)
buttonFrame.grid(row=1, column=0, rowspan=5, columnspan=6, sticky='nsew')

# Add buttons of calculator
cButton = tkinter.Button(buttonFrame, text='C')
cButton.grid(row=0, column=0, sticky='w')

ceButton = tkinter.Button(buttonFrame, text='CE')
ceButton.grid(row=0, column=1, sticky='w')

sevenButton = tkinter.Button(buttonFrame, text='7')
sevenButton.grid(row=1, column=0, sticky='w')
eightButton = tkinter.Button(buttonFrame, text='8')
eightButton.grid(row=1, column=1, sticky='w')
nineButton = tkinter.Button(buttonFrame, text='9')
nineButton.grid(row=1, column=2, sticky='w')
plusButton = tkinter.Button(buttonFrame, text='+')
plusButton.grid(row=1, column=3, sticky='w')

fourButton = tkinter.Button(buttonFrame, text='4')
fourButton.grid(row=2, column=0, sticky='w')
fiveButton = tkinter.Button(buttonFrame, text='5')
fiveButton.grid(row=2, column=1, sticky='w')
sixButton = tkinter.Button(buttonFrame, text='6')
sixButton.grid(row=2, column=2, sticky='w')
minusButton = tkinter.Button(buttonFrame, text='-')
minusButton.grid(row=2, column=3, sticky='w')

oneButton = tkinter.Button(buttonFrame, text='1')
oneButton.grid(row=3, column=0, sticky='w')
twoButton = tkinter.Button(buttonFrame, text='2')
twoButton.grid(row=3, column=1, sticky='w')
threeButton = tkinter.Button(buttonFrame, text='3')
threeButton.grid(row=3, column=2, sticky='w')
multiplyButton = tkinter.Button(buttonFrame, text='*')
multiplyButton.grid(row=3, column=3, sticky='w')

zeroButton = tkinter.Button(buttonFrame, text='0')
zeroButton.grid(row=4, column=0, sticky='w')

equalButton = tkinter.Button(buttonFrame, text='=')
equalButton.grid(row=4, column=1, columnspan=2, sticky='w')

slashButton = tkinter.Button(buttonFrame, text='/')
slashButton.grid(row=4, column=3, sticky='w')

mainWindow.mainloop()
