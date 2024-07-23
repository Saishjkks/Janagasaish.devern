import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
from time import sleep
#import wikipedia
from pyautogui import press, write

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("How can I help you?")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')
    except Exception as e:
        print("Say that again please...")
        return "none"
    return query.lower()

if __name__ == "__main__":
    wishme()
    while True:
        query = command()
        
        # Tasks
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open code' in query:
            codePath = "C:\\Users\\SAISH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open spotify' in query:
            press('win')
            write('spotify')
            sleep(1)
            press('enter')
        elif 'okay bye' in query:
            break
        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.in/")
        elif 'i love you' in query:
            speak('Love you too, Saish!')
        elif 'open store' in query:
            press('win')
            write('store')
            sleep(1)
            press('enter')
        elif 'open snapchat' in query:
            webbrowser.open("https://www.snapchat.com/")
