import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("initializing jarvis")
MASTER = "Gautam"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# speak('  welcome to world...hello Gautam ... i am a jarvis how can help you


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir + MASTER!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir + MASTER !")

    else:
        speak("Good Evening Sir + MASTER !")

    assname = ("Jarvis 1 point o")
    speak("I am your Assistant")
    speak(assname)

    speak("initializing jarvis...")
    wishMe()
