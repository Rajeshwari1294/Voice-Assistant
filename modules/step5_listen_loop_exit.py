import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    with sr.Microphone() as source:
        print("Waiting for command (say 'exit' to quit)...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        if "exit" in command.lower():
            speak("Goodbye!")
            break
        else:
            speak("You said " + command)
    except:
        speak("Sorry, I did not catch that.")