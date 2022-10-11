#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []
direction=40
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color=turtle_colors.pop()
  t.begin_fill()
  t.fillcolor(new_color)
  my_turtles.append(t)
  t.end_fill()

# go back to orgin
startx = 0
starty = 200

#the legs of the mobile
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.setheading(direction)
  t.pendown()     
  t.right(20)
  t.forward(50)
  direction=t.heading()
#the start positon for the next item
  
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()
