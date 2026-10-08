from turtle import *

# colors and extras
bgcolor("beige")

# Write "Sam's movies" at the top
color("dark red")
penup()
goto(-250, 350)
pendown()
write("Sam's movies", font=("Courier", 24, "bold"))

# Create top line
pensize(50)
penup()
goto(-350, 275)
pendown()
forward(675)

# Create square where everything will go
penup()
color("gold")
pensize(5)
goto(320, 250)
begin_fill()
pendown()
right(90)
forward(575)

color("dark red")
right(90)
pensize(50)
forward(675)

penup()
color("gold")
pensize(5)
goto(-350, -300)
pendown()
right(90)
forward(550)
end_fill()

# Create the dictionary
myMovies = {
    "Interstellar": "Christopher Nolan",
    "Soul": "Pete Docter",
    "Avengers Infinity War": "Anthony Russo and Jose Russo",
    "Star Wars: Episode III - Revenge of the Sith": "George Lucas",
    "Backrooms": "Kane Parsons"
}

# Write the dictionary inside the box
penup()
hideturtle()
goto(-325, 200)
pendown()
color("black")

# Print each movie and director neatly
for movie, director in myMovies.items():
    write(movie + " - " + director, font=("Courier", 12, "normal"))
    penup()
    sety(ycor() - 75)
    pendown()
    
done()
