import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
from gtts import gTTS
import os
import subprocess

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # adjusted duration to 0.5 seconds
        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:
                audio = recognizer.listen(source, timeout=10)
                break
            except sr.WaitTimeoutError:
                retries += 1
                print("Timeout. Retrying...")
        if retries == max_retries:
            print("Failed to recognize speech after", max_retries, "retries")
            return
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio, language="en-US").lower()
            print("You said:", data)
        except sr.UnknownValueError:
            print("Didn't understand what you said")
            return
        except sr.RequestError as e:
            print("Error:", e)
            return
        return data


def speechtx(x):
    # Convert the text to a.mp3 file using gTTS
    tts = gTTS(text=x, lang='en', slow=False)
    tts.save("good.mp3")

    # Play the.mp3 file using mpg123
    try:
        subprocess.call(["mpg123", "good.mp3"])
    except FileNotFoundError:
        print("Error: mpg123 not found. Please install it first.")


if __name__ == '__main__':
    while True:
        
        data1 = sptext()
        if "hey rani how are you" in data1:
            name = "i am fine"
            speechtx(name)
            
        elif "your name" in data1:
            name = "my name is rani"
            speechtx(name)
            
        elif "how old are you" in data1:
            age = "my age is not defined"
            speechtx(age)
            
        elif "time" in data1:
            now = datetime.datetime.now()
            time = "The current time is {} hours and {} minutes".format(now.hour, now.minute)
            speechtx(time)
            
        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
        
        elif "knight rider" in data1:
            webbrowser.open("https://www.youtube.com/@nightrider03")
            
        elif "tell me joke" in data1:
            joke_1=pyjokes.get_joke(language="en",category="neutral")
            print(joke_1)
            speechtx(joke_1)
            
        elif "exit" in data1:
            speechtx("thank you")
            break
            
        else:
            print("Thanks for using me!")
     