from turtle import *
bgcolor("gold")
hideturtle()
#right wing
pensize(15)
penup()
goto(8, -100)
circle(100, 30)
pendown()
circle(100, 125)

#top part of right wing
left(170)
circle(-20, 225)

#head-right ear
forward(25)
left(150)
forward(20)

#head-left ear
right(70)
forward(15)
right(70)
forward(20)
left(150)
forward(30)

#top part of left wing
right(185)
circle(20, -230)

#left wing
circle(100, 125)
circle(23, -220)
left(13)
backward(40)
right(60)

#bottom part of right wing
forward(40)
left(4)
circle(-24, 230)


done()
