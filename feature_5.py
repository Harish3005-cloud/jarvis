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



if 'tell me a joke' in text:
        jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"]
    
        joke = random.choice(jokes)
        speak(joke)
        print(joke)