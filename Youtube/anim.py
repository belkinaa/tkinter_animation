import random
import time
from tkinter import *

class  Cat():
    def __init__(self, path_img):
        self.path_img =path_img

    def get_cat(self):
        return c.create_image(id_img_x, id_img_y, anchor=NW, image=PhotoImage(file=self.path_img))

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

cat_obj = PhotoImage(file="cat2.png")
cat_obj2 = PhotoImage(file="cat.png")

id_img = c.create_image(id_img_x, id_img_y, anchor=NW, image=cat_obj)
id_img2 = c.create_image(id_img_x, id_img_y, anchor=NW, image=cat_obj2)
c.delete(id_img)
c.delete(id_img2)

counter = 0
for i in range(mx//step_animation):
    color = "#{:06x}".format(random.randint(0, 256 ** 3))
    c.delete(ball)
    ball = c.create_oval(id_img_x + 450 + counter*step_animation, id_img_y + 300, id_img_x + 550 + counter*step_animation, id_img_y + 400, fill=color, outline=color)
    counter += 1
    if (counter % 2) == 0:
        c.delete(id_img2)
        id_img = c.create_image(id_img_x + counter*step_animation, id_img_y, anchor=NW, image=cat_obj)
        c.move(id_img, step_animation, 0)
    else:
        c.delete(id_img)
        id_img2 = c.create_image(id_img_x + counter*step_animation, id_img_y, anchor=NW, image=cat_obj2)
        c.move(id_img2, step_animation, 0)
    c.move(ball, step_animation, 0)
    root.update()
    time.sleep(sl)


