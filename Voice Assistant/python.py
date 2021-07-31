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
from word2number import w2n


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
        print("Say where you want to move mouse!")
        audio = r.listen(source)


    with sr.Microphone() as source1:
        audio1 = r.adjust_for_ambient_noise(source1)
        n=(n+1)     
        print("Say the number")
        audio1 = r.listen(source1)
        


                                                   # interprete audio (Google Speech Recognition)
    try:
        s = (r.recognize_google(audio))
        result = translator.translate(s)
        message1=result.text
        message = (message1.lower())
        print (message)

        list1=x = message.split()
        language=result.src


        s1 = (r.recognize_google(audio1))
        result1 = translator.translate(s1)
        message12=result.text
        message2 = (message12.lower())
        ra=w2n.word_to_num(message2)
        print (message2)
        print(ra)

        # list2= message1.split()
        language=result.src



        if ('left') in list1:     
            pyautogui.moveRel(-ra,0, duration = 1) 
            a='Mouse have been move to left'
            lan(a,language)
            
        elif ('bottom') in list1 or ('down') in list1:
            pyautogui.moveRel(0,ra, duration = 1) 
            a='Mouse have been move to downward'
            lan(a,language)


        elif ('up') in message or ('top') in message:
            pyautogui.moveRel(0,-ra, duration = 1) 
            a='Mouse have been move to upward'
            lan(a,language)

        elif ('right') in message:
            pyautogui.moveRel(ra,0, duration = 1) 
            a='Mouse have been move to right'
            lan(a,language)

        elif ('click') in message:
            pyautogui.click()   
            a='We have click'
            lan(a,language)

        

        elif ('goodbye') in list1 or ('bye') in list1 or ('thank') in list1:                          
            a='Goodbye Sir'
            lan(a,language)   
            break





    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))
