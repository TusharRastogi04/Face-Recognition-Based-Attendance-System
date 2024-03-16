import pyttsx3 as p
import speech_recognition as sr
import threading

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)  # adjust for ambient noise
        # audio = r.listen(source)

    # try:
    #     # Using the Google Web Speech API for speech recognition
    #     r.recognize_google(audio, language='en')

    # except sr.UnknownValueError:
    #     print("Sorry, could not understand audio.")
    # except sr.RequestError as e:
    #     print(f"Could not request results; {e}")

engine = p.init()  
engine.setProperty('rate', 155)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
r = sr.Recognizer() 
listen_thread = threading.Thread(target=listen)
listen_thread.start()

# speak("Welcome to dj club")
 