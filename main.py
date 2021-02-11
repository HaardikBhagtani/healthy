from time import time
from musiconloop import musiconloop
from lognow import log_now

print("Welcome to the Beautiful Day")
user_name = input("Enter Your name\n").capitalize()


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water_secs = 40*60          # water sound playing time every 40 minutes
    exercise_secs = 30*60       # exercise sound playing time every 30 minutes
    eyes_secs = 45*60           # eyes sound playing time every 30 minutes

    while True:
        if time() - init_water > water_secs:
            print(f"Water Drinking time {user_name}.\nEnter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at ")

        if time() - init_eyes > eyes_secs:
            print(f"Eye exercise time {user_name}.\nEnter 'done eyes' to stop the alarm.")
            musiconloop('eyes.mp3', 'done eyes')
            init_eyes = time()
            log_now("Eyes Relaxed at ")

        if time() - init_exercise > exercise_secs:
            print(f"Physical Activity Time {user_name}.\nEnter 'done exercise' to stop the alarm.")
            musiconloop('physical.mp3', 'done exercise')
            init_exercise = time()
            log_now("Physical Activity done at ")
