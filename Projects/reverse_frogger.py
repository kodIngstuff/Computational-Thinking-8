#Section 1 - Setup

import random
import time
import codesters
from codesters import StageClass
stage = StageClass()
stage.disable_all_walls()
stage.set_background("road")
frog_speed = -3
car_lives = 3
person_lives = 1
person_speed = 2
car = codesters.Sprite("car",-200,0)
car.set_size(0.25)

#Section 2 - Object 1 (Frog)

def falling_object():
    global frog_speed, car_lives
    if car_lives > 0:
        x = 200
        y = random.randint(-175,200)
        frog = codesters.Sprite("frog",x,y)
        frog.set_size(0.125)
        frog.set_x_speed(frog_speed)
stage.event_interval(falling_object,5)

#Section 3 - Collision

def collision(car,frog):
    global frog_speed, car_lives
    if frog.get_image_name() == "frog":
        stage.remove_sprite(frog)
        car_lives -= 1
        if car_lives == 0:
            car.goto(0,0)
            car.say(f"Out of lives - you lost!")
        else:
            car.say(f"{car_lives} lives",0.5)
car.event_collision(collision)

#Section 4 - Controls

def go_up():
    car.move_up(10)
car.event_key("w",go_up)
car.event_key("up",go_up)
def go_down():
    car.move_down(10)
car.event_key("s",go_down)
car.event_key("down",go_down)

