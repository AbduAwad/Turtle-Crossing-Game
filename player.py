START_POS = (0, -250)
MOVE_DIST = 10

from turtle import Turtle
class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.setheading(90)
    self.penup()
    self.back_to_start()

  def up(self):
    self.forward(MOVE_DIST)

  def back_to_start(self):
    self.goto(START_POS)

  