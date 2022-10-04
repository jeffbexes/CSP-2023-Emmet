#   a116_buggy_image.py
import turtle as trtl
#draw body
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
spider.speed(-1)
#configure leg
leg = 8
length = 100
angle = 180/ leg
spider.pensize(5)
leg_remain = 0
#draw legs
while (leg_remain < leg/2):
  spider.goto(0,20)
  spider.setheading(angle*leg_remain)
  spider.forward(length)
  leg_remain= leg_remain+ 1
while (leg_remain<leg):
  spider.goto(0,20) 
  spider.setheading(angle*leg_remain-270)
  spider.forward(length)
  leg_remain= leg_remain+ 1


spider.goto(0,20)
spider.forward(15)
spider.pencolor("red")
spider.fillcolor("red")
spider.begin_fill()
spider.circle(5,-360)
spider.end_fill()
spider.penup()
spider.goto(0,20)
spider.left(70)
spider.forward(15)
spider.pendown()
spider.pencolor("red")
spider.fillcolor("red")
spider.begin_fill()
spider.circle(5,-360)
spider.end_fill()
spider.penup()


spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()
