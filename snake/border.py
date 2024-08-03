from turtle import Turtle
coordinates = [(295, 295), (-295, 295), (-295, -295),(295, -295)]


class Border(Turtle):


    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('red')
        self.penup()
        self.pensize(10)
        self.hideturtle()


    def draw_border(self):
        for position in coordinates:
            self.goto(position)
            self.pendown()
