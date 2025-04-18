import datetime
import time
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time} ⏰")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("🔔 Time to Wake Up!")
            speak("Wake up! It's time to start your day!")
            break
        time.sleep(10)  # Check every 10 seconds

# --- Input Alarm Time ---
user_time = input("Enter alarm time in HH:MM format (24-hour clock): ")
set_alarm(user_time)