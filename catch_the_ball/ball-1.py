import tkinter 
from random import choice, randint

ball_initial_number = 20
ball_minimal_radius = 15 
ball_maximal_radius = 40 
ball_available_colors = ['green', 'blue', 'red', 'lightgray', '#FF00FF', '#FFFF00'] 
balls_coord = []#cpis kor
balls_num = []#cpic nom

def click_ball(event):
     """ ooo canvas
     :param event: cob
     po klik
     zaschit.
     """
     global points, label,  balls_coord, balls_num
     obj = canvas.find_closest(event.x, event.y)
     x1, y1, x2, y2 = canvas.coords(obj)
     num = obj[0]# vitas
     if x1 <= event.x <= x2 and y1 <= event.y <= y2:
          canvas.delete(obj) 
          index = balls_num.index(num)# opr
          balls_num.pop(index)# udal
          balls_coord.pop(index)# udal
          points+=1 
          label['text']=points 
          create_random_ball() 

 
def move_all_balls(event): 
     """ peredvigaet
     """
     for obj in canvas.find_all():
          dx = randint(-1, 1)
          dy = randint(-1, 1)
          canvas.move(obj, dx, dy)
 
def create_random_ball():
     """ 
     sozdaet canvas,
     pri
     """
     global balls_coord, balls_num
     R = randint(ball_minimal_radius, ball_maximal_radius)
     x = randint(0, int(canvas['width'])-1-2*R)
     y = randint(0, int(canvas['height'])-1-2*R)
     #ris sharik v num_oval
     num_oval = canvas.create_oval(x, y, x+R, y+R, width=0, fill=random_color())
     balls_coord.append([x,y])# zap
     balls_num.append(num_oval)# zap nom
 
def random_color():
     """
     :return: sluch svet
     """
     return choice(ball_available_colors)

 
def init_ball_catch_game(): 
     """ 
     soz neob kol shar
     """
     for i in range(ball_initial_number):
          create_random_ball()
 
def init_main_window():
     global root, canvas, label, points

     root = tkinter.Tk()
     label_text = tkinter.Label(root, text = 'ochki')
     label_text.pack()
     points = 0
     label = tkinter.Label(root, text=points)#priv
     label.pack()
     canvas = tkinter.Canvas(root, background='white', width=400, height=400)
     canvas.bind("<Button>", click_ball)
     canvas.bind("<Motion>", move_all_balls)
     canvas.pack()


if __name__ == "__main__":
     init_main_window()
     init_ball_catch_game()
     root.mainloop()
     print("esche!")
