import speech_recognition as sr
import pyttsx3
import pyjokes
import feedparser
import webbrowser
import datetime

# -------------------- SPEAK FUNCTION --------------------
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)  # Speech rate
    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()

# -------------------- LISTEN FUNCTION --------------------
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, the service is unavailable.")
        return ""

# -------------------- COMMAND FUNCTIONS --------------------
def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def get_news():
    feed = feedparser.parse('https://news.google.com/rss')
    headlines = []
    for entry in feed.entries[:5]:
        headlines.append(entry.title)
    return headlines

def read_news():
    news_list = get_news()
    for news in news_list:
        speak(news)

def save_note(note_text):
    with open("notes.txt", "a") as f:
        f.write(note_text + "\n")
    speak("Note saved.")

def dictate_note():
    speak("What should I write in your note?")
    note = listen_command()
    if note:
        save_note(note)

def process_command(command):
    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "joke" in command:
        tell_joke()
    elif "news" in command:
        read_news()
    elif "note" in command:
        dictate_note()
    elif "exit" in command or "quit" in command or "goodbye" in command:
        speak("Goodbye!")
        return False
    else:
        speak("Command not supported.")
    return True

# -------------------- MAIN LOOP --------------------
def main():
    speak("Hi, I am your voice assistant. How can I help you?")
    while True:
        command = listen_command()
        if command:
            if not process_command(command):
                break

if __name__ == "__main__":
    main()
