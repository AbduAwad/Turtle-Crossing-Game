import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import Car_manager

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = Car_manager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_on = True

while game_on:
  scoreboard.update_scoreboard()
  time.sleep(0.1)
  screen.update()
  
  car_manager.generate_car()
  car_manager.move_car()

  #Detect turtle collision with car
  for i in car_manager.cars:
    if i.distance(player) <= 20:
      game_on = False
      scoreboard.game_over()

  # Detect when turtle reaches other side of screen and take back to start pos
  if player.ycor() >= 300:
    player.back_to_start()
    car_manager.inc_speed()
    scoreboard.inc_level()