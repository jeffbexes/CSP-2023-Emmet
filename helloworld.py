user_name= input("what is your name?")
print ("hello", user_name, "welcome")

from cgitb import grey
import turtle as trtl


painter = trtl.Turtle()
painter.fillcolor("red")
painter.begin_fill()
painter.pensize(3)
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
painter.fillcolor("blue")
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

wn = trtl.Screen()
wn.mainloop()
