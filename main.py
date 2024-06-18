import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import requests
import json
import pyjokes

# Initialize the speech engine
jarvis = pyttsx3.init('sapi5')
jarvis.setProperty('voice', jarvis.getProperty("voices")[1].id)
jarvis.setProperty('rate', 150)

# Function to make Jarvis speak
def speak(audio):
    jarvis.say(audio)
    jarvis.runAndWait()

# Function to take command from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        # r.energy_threshold = 1000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}")
        return query

    except:
        print("Say that again please...")
        return "Say that again please..."

# Function to get the current time
def get_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    speak(f"The current time is {time_str}")

# Function to tell a joke
def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

if __name__ == "__main__":
    speak("Hi This is Jarvis")
    while True:
        if takeCommand().lower() == "hey jarvis":
            speak("hi, how can i help you?")
            query = takeCommand().lower()
            if "open google" in query:
                speak("Opening Google")
                webbrowser.open("https://www.google.com/")
                continue
            elif "open youtube" in query:
                speak("Opening Youtube")
                webbrowser.open("https://www.youtube.com/")
                continue
            elif "what time is it" in query or "current time" in query:
                get_time()
                continue
            elif "tell me a joke" in query:
                tell_joke()
                continue
            elif "bye" in query or "exit" in query:
                speak("Bye")
                exit()

