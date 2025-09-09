import speech_recognition as sr
import webbrowser
import datetime

def process_command(command):
    command = command.lower()
    if "google" in command:
        webbrowser.open("https://www.google.com")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        print("The time is", now)
    else:
        print("Command not supported.")

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("What do you want to do?")
    audio = recognizer.listen(source)
try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
    process_command(text)
except:
    print("Could not recognize your speech.")