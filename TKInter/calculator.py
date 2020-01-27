import tkinter

# mainWindow = tkinter.Tk()
# mainWindow.title('Calculator')
# mainWindow.geometry('320x240')
# mainWindow.columnconfigure(0, weight=1)
# mainWindow.columnconfigure(1, weight=1)
# mainWindow.columnconfigure(2, weight=1)
# mainWindow.columnconfigure(3, weight=1)
# mainWindow.columnconfigure(4, weight=1)
# mainWindow.columnconfigure(5, weight=1)
# mainWindow.columnconfigure(6, weight=1)
# mainWindow.rowconfigure(0, weight=1)
# mainWindow.rowconfigure(1, weight=1)
# mainWindow.rowconfigure(2, weight=1)
# mainWindow.rowconfigure(3, weight=1)
# mainWindow.rowconfigure(4, weight=1)
# mainWindow.rowconfigure(5, weight=1)
# mainWindow.rowconfigure(6, weight=1)
# mainWindow.rowconfigure(7, weight=1)
# mainWindow['padx'] = 8
# mainWindow['pady'] = 8
# resultFrame = tkinter.Entry(mainWindow, width=2)
# resultFrame.grid(row=0, column=0, columnspan=3, sticky='nsew')
#
#
# buttonFrame = tkinter.Frame(mainWindow, width=5)
# buttonFrame.grid(row=1, column=0, rowspan=5, columnspan=6, sticky='nsew')
#
#
# # Add buttons of calculator
# cButton = tkinter.Button(buttonFrame, text='C', background='grey')
# cButton.grid(row=0, column=0, sticky='ew')
#
#
# ceButton = tkinter.Button(buttonFrame, text='CE')
# ceButton.grid(row=0, column=1, sticky='ew')
#
# sevenButton = tkinter.Button(buttonFrame, text='7')
# sevenButton.grid(row=1, column=0, sticky='ew')
# eightButton = tkinter.Button(buttonFrame, text='8')
# eightButton.grid(row=1, column=1, sticky='ew')
# nineButton = tkinter.Button(buttonFrame, text='9')
# nineButton.grid(row=1, column=2, sticky='ew')
# plusButton = tkinter.Button(buttonFrame, text='+')
# plusButton.grid(row=1, column=3, sticky='ew')
#
# fourButton = tkinter.Button(buttonFrame, text='4')
# fourButton.grid(row=2, column=0, sticky='ew')
# fiveButton = tkinter.Button(buttonFrame, text='5')
# fiveButton.grid(row=2, column=1, sticky='ew')
# sixButton = tkinter.Button(buttonFrame, text='6')
# sixButton.grid(row=2, column=2, sticky='ew')
# minusButton = tkinter.Button(buttonFrame, text='-')
# minusButton.grid(row=2, column=3, sticky='ew')
#
# oneButton = tkinter.Button(buttonFrame, text='1')
# oneButton.grid(row=3, column=0, sticky='ew')
# twoButton = tkinter.Button(buttonFrame, text='2')
# twoButton.grid(row=3, column=1, sticky='ew')
# threeButton = tkinter.Button(buttonFrame, text='3')
# threeButton.grid(row=3, column=2, sticky='ew')
# multiplyButton = tkinter.Button(buttonFrame, text='*')
# multiplyButton.grid(row=3, column=3, sticky='ew')
#
# zeroButton = tkinter.Button(buttonFrame, text='0')
# zeroButton.grid(row=4, column=0, sticky='ew')
#
# equalButton = tkinter.Button(buttonFrame, text='=')
# equalButton.grid(row=4, column=1, columnspan=2, sticky='ew')
# equalButton['padx'] = 14
#
# slashButton = tkinter.Button(buttonFrame, text='/')
# slashButton.grid(row=4, column=3, sticky='ew')
#
# mainWindow.mainloop()

"""Instead of writing so many lines of code, we can create calculator GUI using below loop. We can add the keypad values
in a nested list and iterate over the list to create the calculator keypad."""
mainWindowPadding = 8
mainWindow = tkinter.Tk()
mainWindow.title('Calculator')
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = mainWindowPadding

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)]]
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')
keypad = tkinter.Frame(mainWindow)
keypad.grid(row=1, column=0, sticky='nsew')

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keypad, text=key[0]).grid(row=row, column=col, columnspan=key[1], stick='ew')
        col += key[1]
    row += 1
mainWindow.update()
mainWindow.minsize(keypad.winfo_width() + mainWindowPadding, result.winfo_height() + keypad.winfo_height())
mainWindow.maxsize(keypad.winfo_width() + mainWindowPadding, result.winfo_height() + keypad.winfo_height())

mainWindow.mainloop()