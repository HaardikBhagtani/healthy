from datetime import datetime


def log_now(msg):
    """Logging the time and message when an activity is done"""
    with open("lognow.log", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")
    f.close()
