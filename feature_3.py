import time
import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import wikipedia
import os
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
recognizer = sr.Recognizer()
exit_flag = False
with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything...')
        try:
            recordedaudio = recognizer.listen(source)
            text = recognizer.recognize_google(recordedaudio, language='en_US')
            text = text.lower()
            print('Your message:', text)
        except Exception as ex:
            print("Could not recognize your voice. Error:", ex)
            #return  # Exit early if no valid input

def speak(text):
    """Speak the given text using pyttsx3."""
    engine.say(text)
    try:
        engine.runAndWait()
    except RuntimeError:
        pass  # Ignore runtime errors if the event loop is already running

if 'set an alarm' in text:
        speak("What time should I set the alarm for?")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            follow_up_audio = recognizer.listen(source)
        try:
            alarm_time = recognizer.recognize_google(follow_up_audio, language='en_US')
            speak(f"Opening Alarms & Clock for {alarm_time}. Please set the alarm manually.")
            subprocess.run(['start','ms-clock:'],shell=True)
        except Exception as e:
            speak("Sorry, I couldn't understand the time. Please try again.")