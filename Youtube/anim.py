import random
import time
from tkinter import *

class  Cat():
    def __init__(self, path_img, id_img_x, id_img_y, canvas):
        self.path_img =path_img
        self.id_img_x, self.id_img_y = id_img_x, id_img_y
        self.obj_PhotoImage = PhotoImage(file=self.path_img)
        self.canvas = canvas
        self.set_cat()
        self.canvas.delete(self.id_img)

    def set_cat(self, stepX=0, stepY=0):
        self.id_img = self.canvas.create_image(self.id_img_x + stepX, self.id_img_y + stepY, anchor=NW, image=self.obj_PhotoImage)


    def move(self, step_animationX, step_animationY=0, counter=1):
        self.set_cat(stepX=counter * step_animationX)
        self.canvas.move(self.id_img, step_animationX, step_animationY)


root = Tk()
mx = 1000
my = 600

c = Canvas(root, width=mx, height=my)
c.pack()
cp = 5
sl = 0.05
id_img_x = 50
id_img_y = 50
step_animation = 5

color = "#{:06x}".format(random.randint(0, 256 ** 3))
ball = c.create_oval(id_img_x+450, id_img_y+300, id_img_x+550, id_img_y+400, fill=color, outline = color)


obj_cat = Cat(path_img='cat.png',
              id_img_x=id_img_x,
              id_img_y=id_img_y,
              canvas=c)
obj_cat2 = Cat(path_img='cat2.png',
              id_img_x=id_img_x,
              id_img_y=id_img_y,
              canvas=c)

counter = 0
for i in range(mx//step_animation):
    color = "#{:06x}".format(random.randint(0, 256 ** 3))
    c.delete(ball)
    ball = c.create_oval(id_img_x + 450 + counter*step_animation, id_img_y + 300,
                         id_img_x + 550 + counter*step_animation, id_img_y + 400,
                         fill=color, outline=color)
    counter += 1

    if (counter % 2) == 0:
        c.delete(obj_cat2.id_img)
        obj_cat.move(step_animation, counter=counter)
    else:
        c.delete(obj_cat.id_img)
        obj_cat2.move(step_animation, counter=counter)
    c.move(ball, step_animation, 0)
    root.update()
    time.sleep(sl)


