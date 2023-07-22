from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.current_level = 1
    

  def update_scoreboard(self):
    self.clear()
    self.hideturtle()
    self.penup()
    self.goto(-280, 250)
    self.write(f"LEVEL: {self.current_level} ", align = "left", font = FONT)
    
  def inc_level(self):
    self.current_level += 1

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER!", align = "center", font = FONT)