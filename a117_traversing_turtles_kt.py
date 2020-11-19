#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  new_color = turtle_colors.pop()
  t.pencolor(new_color)
  t.fillcolor(new_color)

#  
startx = 0
starty = 0
direction = 90
increase = 1
#
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.setheading(direction + increase)
  t.pendown()
  t.pensize(increase)
  t.right(45)    
  t.forward(increase * 15)
  direction = t.heading()

  increase = increase + 1

  

#
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()