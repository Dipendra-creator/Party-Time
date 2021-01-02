#    2021 First Project

import vlc
import os
import datetime
import time
from datetime import date

today = date.today()

# Add default VLC directories for libvlc.dll

# Needed for interacting with VLC
try:
    os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')  # 64-Bt
except FileNotFoundError:
    pass
try:
    os.add_dll_directory(r'C:\Program Files (x86)\VideoLAN\VLC')  # 32-Bit
except FileNotFoundError:
    pass


def skip_vid():
    if hour == givenHour:
        if minute > givenMin:
            time_to_skip = float(calc_time())
            media.set_time(int(time_to_skip*1000))
            print(f"Movie Skipped {time_to_skip} Seconds")


def calc_time():
    current_time = datetime.datetime.now  # Current Time for difference
    target_time = datetime.datetime(int(today.strftime("%Y")), int(today.strftime("%m")), int(today.strftime("%d")), hour, minute, second)

    return (target_time - current_time()).total_seconds()


file = "E:/Movies/ww.mkv"

media = vlc.MediaPlayer(file)

# Party Time
print(f"Please input Party Time")
hour, minute = list(map(int, input('Enter a time in future: HH:MM (24-Hour): ').strip().split(':')))
givenHour = hour
givenMin = minute
second = 0

media.play()
media.set_pause(True)
# Seek to a time (MS)
media.set_time(0)

# Sleep till the Party starts
try:
    time.sleep(calc_time())
except ValueError:
    time.sleep(2)
    hour, minute = list(map(int, input('Enter a time in future: HH:MM (24-Hour): ').strip().split(':')))
    print(f"Movie Starts in : {calc_time()}")
    skip_vid()
    time.sleep(calc_time())

# Video length in seconds
video_length = media.get_length() / 1000

print(f"Movie length in: {video_length}")
video_length /= 2
print(f"Movie Interval Time in: {video_length}")
media.set_fullscreen(True)

# Play for one Hour
media.play()
time.sleep(video_length)


# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


# Pause for 10 Minutes
media.set_pause(True)
print("Break Time For 10 Mins Guyzz")
countdown(600)

# Play Again
media.play()
time.sleep(video_length)
# media.close()
input("Goodbye!! Press any key to exit ")
