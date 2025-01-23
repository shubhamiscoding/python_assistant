import pyttsx3
import speech_recognition as sr
import random
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 125)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = " "
    while content == "":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("GIVE ORDER")
            audio = r.listen(source)

            try:
                content = r.recognize_google(audio, language='en-in')
                print("command = " + content)
            except Exception as e:
                print("please try again buddy...")
                content = ""
    return content

def main_process():
    while True:
        request = command().lower()
        if "hello" in request:
            speak("welcome, how can I help you")
        elif "play music" in request:
            speak("playing music")
            song = random.randint(1, 5)
            if song == 1:
                webbrowser.open("https://youtu.be/Qq-pTZaozcs?si=HlR_D7iW9cPZQsGh")
            elif song == 2:
                webbrowser.open("https://youtu.be/_wfrNbLguWw?si=svtZ-lRzz6yxhr-T")
            elif song == 3:
                webbrowser.open("https://youtu.be/U0OsKaiDQZM?si=2DSKAbHaowPhkS_I")
            elif song == 4:
                webbrowser.open("https://youtu.be/r6LNuLH4skg?si=YoCD9hk0F12Rn1UZ")
            elif song == 5:
                webbrowser.open("https://youtu.be/fWVtPYZxRXE?si=LqegDXlQ8GV4LMo1")


main_process()
