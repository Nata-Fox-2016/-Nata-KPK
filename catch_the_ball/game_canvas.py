import tkinter


def paint(event):
    """ obrabot sob canvas
    :param event: sob
    :return: not
    """
    print(event.x, event.y)
    if event.widget != canvas:
        print('Stranno,  paint() privas canvas...')
        return
    canvas.coords(line, 0, 0, event.x, event.y)


root = tkinter.Tk()

canvas = tkinter.Canvas(root, background='white', width=400, height=400)
canvas.bind("<Motion>", paint)
canvas.pack()

line = canvas.create_line(0, 0, 10, 10)
for i in range(10):
    canvas.create_oval(2+i*40, 2+i*40, i*40+30, i*40+30, width=2, fill='green')


root.mainloop()
print("Pri vihode.")