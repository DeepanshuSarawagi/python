import tkinter
# import math


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill='black')
    page.create_line(0, -y_origin, 0, y_origin, fill='black')


def circles(page, radius, g, h, color):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill='red')


mainWindow = tkinter.Tk()
mainWindow.title("Circles")
mainWindow.geometry('640x480-8-200')

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)
# Call the function to create axes in the canvas
draw_axes(canvas)
circles(canvas, 100, 100, 100, 'green')
circles(canvas, 100, -100, 100, 'blue')
circles(canvas, 100, 100, -100, 'black')
circles(canvas, 100, -100, -100, 'orange')
circles(canvas, 10, 30, 30, 'red')
circles(canvas, 10, -30, 30, 'red')
circles(canvas, 10, 30, -30, 'black')
circles(canvas, 10, -30, -30, 'orange')
circles(canvas, 30, 0, 0, 'green')

mainWindow.mainloop()
