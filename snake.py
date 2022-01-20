from turtle import Turtle

class Snake:
  def __init__(self):
    init_body = []
    for index in range(3):
      current_segment = self.create_segment(index*-20,0)
      init_body.append(current_segment)
    self.body = init_body
    self.head = self.body[0]
  
  def turn_up(self):
    if not self.body[0].heading() == 270:
      self.body[0].setheading(90)
  
  def turn_left(self):
    if not self.body[0].heading() == 0:
      self.body[0].setheading(180)

  def turn_right(self):
    if not self.body[0].heading() == 180:
      self.body[0].setheading(0)
    
  def turn_down(self):
    if not self.body[0].heading() == 90:
      self.body[0].setheading(270)
  
  def move_snake(self):
    for segment in range( len(self.body) -1 , 0, -1):
      new_x = self.body[segment -1].xcor()
      new_y = self.body[segment -1].ycor()
      self.body[segment].goto(new_x, new_y)
    self.body[0].fd(20)
  
  def create_segment(self, pos_x, pos_y):
    body_segment = Turtle(shape="square")
    body_segment.pu()
    body_segment.color("green")
    body_segment.goto(pos_x,pos_y)
    return body_segment

  def grow(self):
    last_segment = self.body[-1]
    current_segment = self.create_segment(last_segment.xcor(), last_segment.ycor())
    self.body.append(current_segment)
    print(f"snake is {len(self.body)} currently")

    
    
      
     
