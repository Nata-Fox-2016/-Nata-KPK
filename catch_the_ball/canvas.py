import tkinter


def paint(event):
    """ Obrabotchik canvas
    :param event: sobitie
    :return: nichego
    """
    print(event.x, event,y)
    if event.widget != canvas:
        print('Stranno, ved paint() privizali tolko k canvas...'
    return
    canvas.coords(line, 0, 0, event.x, event.y)


root = tkinter.Tk()

canvas = tkinter.Canvas(root)
canvas.bind("<Motion>", paint)
canvas.pack()

line = canvas.create_line(0, 0, 10, 10)

root.mainloop()
print("Eto stroka budet pri vihode")
