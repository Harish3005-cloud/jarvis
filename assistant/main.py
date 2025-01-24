import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
recognizer = sr.Recognizer()
exit_flag = False

def speak(text):
    """Speak the given text using pyttsx3."""
    engine.say(text)
    try:
        engine.runAndWait()
    except RuntimeError:
        pass  # Ignore runtime errors if the event loop is already running

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Ready to comply. What can I do for you?")

def cmd():
    global exit_flag
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
            return  # Exit early if no valid input

    if 'chrome' in text:
        speak('Opening Chrome...')
        programName = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
    elif 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak(time)
    elif any(phrase in text for phrase in ['who is', 'what is', 'how is', 'when is']):
        try:
            wikisearch = wikipedia.summary(text, sentences=2)
            speak(wikisearch)
        except Exception as e:
            speak("Sorry, I couldn't find anything on that.")
    elif 'youtube' in text:
        speak('Opening YouTube...')
        webbrowser.open('www.youtube.com')
    elif any(phrase in text for phrase in ['who are you', 'what is your name', 'who developed you', 'what can i call you', 'introduce yourself']):
        speak('I am Jarvis, developed by Harish.')
    elif 'vs code' in text or 'visual studio code' in text:
        speak('Already you are in Visual Studio Code.')
    elif 'whatsapp' in text:
        speak('Opening WhatsApp...')
        pg1 = r"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2502.3.0_x64__cv1g1gvanyjgm\WhatsApp.exe"
        subprocess.Popen([pg1])
    elif 'spotify' in text:
        speak('Opening Spotify...')
        pg2 = r"C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.255.235.0_x64__zpdnekdrzrea0\Spotify.exe"
        subprocess.Popen([pg2])
    elif 'exit' in text or 'stop' in text or 'shut up' in text or 'thank you' in text: 
        speak('Exiting. If there is anything else you need help with, let me know.')
        exit_flag = True
    elif any(op in text for op in ['+', '-', '*', '/', 'plus', 'minus', 'times', 'into', 'by', 'mod']):
     try:
        # Replace keywords with math-friendly operators
        text = text.replace('plus', '+').replace('+', '+') \
                   .replace('minus', '-').replace('-', '-') \
                   .replace('times', '*').replace('*', '*') \
                   .replace('into', '*').replace('/', '/') \
                   .replace('by', '/').replace('mod', '%')

        # Identify and execute the operation
        for operator in ['+', '-', '*', '/', '%']:
            if operator in text:
                numbers = text.split(operator)
                num1 = float(numbers[0].strip())
                num2 = float(numbers[1].strip())
                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '%':
                    result = num1 % num2
                elif operator == '/':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        result = "Undefined (division by zero)"
                break

        # Announce and print the result
        speak(f"The result is {result}")
        print(f"The result is {result}")

     except Exception as e:
        speak("Sorry, I couldn't perform the calculation. Please try again.")
        print("Error:", e)

                           
                
    else:
        speak('I am a prototype; I need more development.')

if __name__ == "__main__":
    wishme()
    while not exit_flag:
        cmd()
