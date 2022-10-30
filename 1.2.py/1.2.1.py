# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import random as randy
#-----game configuration----
t.shape("circle")
t.fillcolor("orange")
t.begin_fill()
t.end_fill()
score=0
timer =5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
score_writer=t.Turtle()
score_writer.penup()
score_writer.goto(0,400)
font_setup=("Arial", 20, "normal")
counter=t.Turtle()
font_setup=("Arial", 20, "normal")
counter.penup()
counter.hideturtle()
counter.goto(-800,400)
#-----game functions--------
def t_click(x,y):
    x_pos=randy.randint(-200,200)
    y_pos=randy.randint(-150,150)
    x_pos
    y_pos
    t.hideturtle()
    t.penup()
    t.goto(x_pos,y_pos)
    update_score()
    t.showturtle()
    if timer==0:
        t.hideturtle()

def update_score():
    score_writer.hideturtle()
    global score
    score+=1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
#-----events----------------



wn=t.Screen()
wn.bgcolor("purple")
wn.ontimer(countdown, counter_interval) 
t.onclick(t_click)
wn.mainloop()

