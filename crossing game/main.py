from turtle import Screen
import time
from scoreboard import Scoreboard
from player import Player
from cars import Car_manager


screen = Screen()
screen.setup(width=800, height=700)
screen.bgcolor('beige')
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()



screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')
screen.onkey(player.move_left, 'Left')
screen.onkey(player.move_right, 'Right')


car_manager = Car_manager()


game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    # detect level pass
    if player.ycor() > 320:
        player.restart_position()
        car_manager.level_up()
        scoreboard.level_up()

    #detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()