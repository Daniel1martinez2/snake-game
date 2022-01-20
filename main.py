from food import Food
import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

tim = Snake()
food = Food()

game_is_on = True

screen.listen()
screen.onkey(key="Up", fun=tim.turn_up)
screen.onkey(key="Left", fun=tim.turn_left)
screen.onkey(key="Down", fun=tim.turn_down)
screen.onkey(key="Right", fun=tim.turn_right)

while game_is_on:
  screen.update()
  time.sleep(0.1)
  tim.move_snake()

  #Detect collisions with food
  if tim.head.distance(food) < 15:
    print("nom nom nom")
    food.refresh()
    tim.grow()

# screen.update()
# screen.exitonclick()