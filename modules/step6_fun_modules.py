import pyttsx3
import pyjokes
import feedparser
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)  # Slow speech rate
    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()

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

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your note...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    except:
        speak("Sorry, I did not catch that.")
        return ""

def save_note(note_text):
    with open("notes.txt", "a") as f:
        f.write(note_text + "\n")
    speak("Note saved.")

def dictate_note():
    speak("What should I write in your note?")
    note = listen_command()
    if note:
        save_note(note)

tell_joke()
read_news()
dictate_note()
