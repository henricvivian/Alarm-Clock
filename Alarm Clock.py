import datetime
import time
from pydub import AudioSegment
from pydub.playback import play

def set_alarm(alarm_time):
    while True:
        time.sleep(1)
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == alarm_time:
            print("Time's up!")
            sound = AudioSegment.from_mp3("alarm_sound.mp3")
            play(sound)
            break

print("Welcome to the alarm clock!")
alarm_time = input("Enter the time for the alarm (in HH:MM:SS format): ")
set_alarm(alarm_time)
print("Thanks for using the alarm clock!")
