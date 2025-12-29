import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys

# --- CONFIGURATION ---
AI_NAME = "Orion"

# --- ENGINE SETUP ---
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 

def speak(audio):
    print(f"{AI_NAME}: {audio}")
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak(f"Good Morning! {AI_NAME} is online.")
    elif 12 <= hour < 18:
        speak(f"Good Afternoon! {AI_NAME} is online.")
    else:
        speak(f"Good Evening! {AI_NAME} is online.")
    speak("How may I assist you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        return "None"
    return query.lower()

if __name__ == "__main__":
    wish_me()
    
    while True:
        query = take_command()
        if query == "None": continue

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("No results found.")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening YouTube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'who are you' in query:
            speak(f"I am {AI_NAME}, your AI assistant.")

        elif 'shutdown' in query:
            speak("Goodbye.")
            sys.exit()
          
