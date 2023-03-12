# Alarm Clock Program
This is a Python program that allows users to set an alarm and play an audio file when the alarm goes off. The program uses the datetime, time, pydub, and pydub.playback modules.

# Installation
Before using the program, make sure to install the pydub module by running the following command:
```bash
    pip install pydub
```

# Usage
To use the program, simply run the alarm_clock.py script in the command line or in an IDE. The program will prompt you to enter a time for the alarm in the format HH:MM:SS. Once you enter the time, the program will run in the background and continuously check the current time. When the current time matches the alarm time, the program will play an audio file (alarm_sound.mp3) and print "Time's up!" in the console.

To stop the alarm, simply press Ctrl-C in the console.

# Customization
If you want to use a different audio file for the alarm, simply replace alarm_sound.mp3 with your preferred audio file in the set_alarm() function.

# Contributing
If you want to contribute to the program, feel free to fork the repository and submit a pull request.