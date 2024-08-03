from turtle import Turtle
POSITION = (-320, 290)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.pencolor('dark turquoise')
        self.level = 1
        self.update_level()


    def update_level(self):
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=('Comic Sans MS', 22, 'normal'))


    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.color('Black')
        self.goto(0, 0)
        self.write(f'Game Over.' , align='center', font=('Courier', 22, 'normal'))
