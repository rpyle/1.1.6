#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)
number_of_legs = 6
leg_length = 70
leg_angle = 380 / number_of_legs
painter.pensize(5)
current_leg = 0
while (current_leg < number_of_legs):
  painter.goto(0,0)
  painter.setheading(leg_angle*n)
  painter.forward(leg_length)
  n = n + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()