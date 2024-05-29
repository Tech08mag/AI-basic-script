import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init()



def speak(audio):
    # say the output on the speaker
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def wishme():
    speak("Willkommen zurück Meister")
    speak("the current time is")
    time()
    speak("Jarvis on your service please tell me how to help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongizing...")
        query =  r.re(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"

    return query

takeCommand()