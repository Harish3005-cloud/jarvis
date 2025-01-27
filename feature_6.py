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

if any(phrase in text for phrase in ['how are you', 'hello', 'hi', 'goodbye','bye']):
        if"how are you" in text:
            speak("I'm doing great, thank you for asking!")
        elif "hello" in text or "hi" in text:
            speak("Hello! How can I assist you today?")
        elif "goodbye" in text or "bye" in text:
            speak("Hasta la vista! Have a great understand that.")
        else:
            speak("Sorry, I didn't quite understand that. ")
else:
        speak('I am a prototype; I need more development.')
