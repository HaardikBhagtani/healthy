from pygame import mixer


def musiconloop(file, stopper):
    """Music Playing and Stopping by a stopper word Function"""
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break
