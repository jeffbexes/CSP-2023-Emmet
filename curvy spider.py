#setup
import numbers
import turtle as trtl
turtle=trtl
import random as random
#QOL changes
trtl.hideturtle()
trtl.speed(0)
#calculations and inputs/outputs
input1= input("How many zombies were there initaily")
start= int(input1)
input2= input("how fast do they replicate")
replication=int(input2)
input3= input("how many days have it been")
days=int(input3)
zombies= int(start**replication)
zombozo= int(zombies*days)
print("there are", zombozo, "zombies existing after", days,"days")
#configure zomibe bodies
radius=int(500/zombozo)
#drawing the zombozos
for step in range(zombozo):
    trtl.penup()
    for i in range (zombozo):
        random_angles=random.randint(1,360)
        random_distances=random.randrange(1,5)
    trtl.pencolor("green")
    trtl.fillcolor("green")
    trtl.begin_fill()
    for step in range (zombozo):
        trtl.penup()
        trtl.setheading(random_angles)
        trtl.forward(random_distances)
        trtl.pendown()
    if zombozo<=9:
     trtl.circle(radius)
    elif zombozo >= 10:
     trtl.circle(radius)
    elif zombozo<=11:
        trtl.circle(1)
    trtl.penup()
    trtl.goto(0,0)
    trtl.pendown()
    trtl.end_fill()
wn = trtl.Screen()
wn.mainloop()
