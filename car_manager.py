from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_MOVE_DIST = 5
MOVE_INC = 10
NUM_CARS = 10
NUM_CARS_INC = 5


class Car_manager:
  def __init__(self):
    self.cars = []
    self.car_speed = START_MOVE_DIST
    
  def generate_car(self):
    rand_chance = random.randint(0, 5) #Around every 5 times the while loop runs it will generate the car
    if rand_chance == 1: #Will reduce the number of cars generated 
      car = Turtle()
      car.shape("square")
      car.color(random.choice(COLORS))
      car.shapesize(1, 2)
      car.penup()
      car.goto(280, random.randint(-225, 300))
      car.setheading(180)
      self.cars.append(car)
      
  def car_move(self):
    self.forward(START_MOVE_DIST)

  def move_car(self):
    for car in self.cars:
      car.forward(self.car_speed)

  def inc_speed(self):
    self.car_speed += MOVE_INC
   
        