from turtle import Turtle

class Score(Turtle):

  def __init__(self):
    super().__init__()
    self.score_number = 0
    self.color("white")
    self.pu()
    self.hideturtle()
    self.goto(0, 250)
    self.update()
  
  def update(self):
    self.write(f"score: {self.score_number}", align="center", font=("Arial", 24, "normal") )

  def increase_score(self):
    self.score_number += 1
    self.clear()
    self.update()
  
  def game_over(self):
    self.score_number = 0
    self.color("red")
    self.goto(0,0)
    self.hideturtle()
    self.write("GAME OVER", align="center", font=("Arial", 24, "normal") )