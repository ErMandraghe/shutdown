import os

def shutdown():
    if os.name == 'nt':  # For Windows
        os.system('shutdown /s /t 1')  # /s for shutdown, /t for time delay (1 second)

shutdown()