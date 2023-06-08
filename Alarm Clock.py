import datetime
import time
from pydub import AudioSegment
from pydub.playback import play

def set_alarm(alarm_time):
    alarm_datetime = datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time's up!")
            sound = AudioSegment.from_mp3("alarm_sound.mp3")
            play(sound)
            break
        time.sleep(1)

def get_user_input(prompt):
    return input(prompt)

def main():
    print("Welcome to the alarm clock!")
    alarm_time = get_user_input("Enter the time for the alarm (in HH:MM:SS format): ")
    try:
        set_alarm(alarm_time)
    except ValueError:
        print("Invalid time format. Please enter the time in HH:MM:SS format.")
    print("Thanks for using the alarm clock!")

if __name__ == "__main__":
    main()
