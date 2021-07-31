import pyaudio
import speech_recognition as sr
import os
import random
import socket
import webbrowser
import subprocess
import glob
from time import localtime, strftime
import speekmodule
from googletrans import Translator
import gtts
from playsound import playsound
import time 
import pyautogui 
import wikipedia  


doss = os.getcwd()
i=0
n=0

translator = Translator()
def lan(a,language):
    translator = Translator()  
    translations = translator.translate(a, dest=language)
    a=(translations.text)
    tts = gtts.gTTS(a)
    tts.save("hello.mp3")
    playsound("hello.mp3")
    os.remove('hello.mp3')

while (i<1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        n=(n+1)     
        print("What you want to search in wikipedia?")
        a=('What you want to search in wikipedia?')
        lan(a,'en')
        audio = r.listen(source)
                                                   # interprete audio (Google Speech Recognition)
    try:
        s = (r.recognize_google(audio))
        result = translator.translate(s)
        message1=result.text
        message = (message1.lower())
        print (message)

        list1=x = message.split()
        language=result.src


        if len(message)!=0:     
            a = wikipedia.summary(message, sentences = 20)  
            lan(a,language)        
            break
        



    except ModuleNotFoundError:
        print(" ")
    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))
