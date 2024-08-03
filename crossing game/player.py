from turtle import Turtle

COORDINATES = (0,-320)
FINISH_LINE = (320)
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.goto(COORDINATES)
        self.color('forest green')



    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def restart_position(self):
        self.goto(COORDINATES)
