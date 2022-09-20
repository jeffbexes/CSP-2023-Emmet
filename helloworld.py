fav_color= input ("what is your favorite color?")
ndfavcolor= input ("what is the second best colour")
thickness= input ("how thick do you like to draw?")
print ("Good choices!")

from cgitb import grey
import turtle as trtl


painter = trtl.Turtle()
painter.fillcolor(fav_color)
painter.begin_fill()
painter.pensize(thickness)
painter.forward(150)
painter.right (90)
painter.forward(120)
painter.right(90)
painter.forward(150)
painter.right(90)
painter.forward(120)
painter.end_fill()
#painter.penup should be here
painter.penup()
painter.right(180)
painter.forward(30)
painter.left(90)
#2nd shape here
painter.fillcolor(ndfavcolor)
painter.begin_fill()
painter.forward(30)
painter.pendown()
painter.forward(90)
painter.right(90)
painter.forward(50)
painter.right(90)
painter.forward(90)
painter.right(90)
painter.forward(50)
painter.end_fill()
#ears begin hear if I have time
painter.penup()
painter.forward(30)
painter.right(90)
painter.pendown()
painter.fillcolor(fav_color)
painter.begin_fill()
painter.circle(45)
painter.end_fill()
painter.penup()
#2nd circle here
painter.forward(90)
painter.pendown()
painter.fillcolor(fav_color)
painter.begin_fill()
painter.circle(45)
painter.end_fill()





wn = trtl.Screen()
wn.mainloop()
