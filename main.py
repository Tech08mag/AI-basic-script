import pyttsx3
import datetime

engine = pyttsx3.init()



def speak(audio):
    # say the output on the speaker
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

time()