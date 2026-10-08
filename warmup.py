from turtle import *
# star imports everything below
shape("turtle")
pensize(3)

print(pos())

#square
for i in range(4):
    forward(150) # pixels
    left(90)

#title area
penup()
goto(-200, 250)
pendown()
write("Tracy's Bookshelf", font=("Courier", 24, "bold"))

penup()
goto(-100, -250)
pendown()
circle(100, 180) # radius degrees
#keeps window open 
done()