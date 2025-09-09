import pyttsx3

def speak(output):
    engine = pyttsx3.init()
    engine.say(output)
    engine.runAndWait()

speak("hi i am voice assistant.")