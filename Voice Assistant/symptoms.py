import pyaudio
import speech_recognition as sr
from pygame import mixer
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
        print("Say your symptoms you have")
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


        if ('headache') in list1:                          
            a='Conditions that might cause nonprimary chronic daily headaches include: Inflammation or other problems with the blood vessels in and around the brain, including stroke. Infections, such as meningitis. Intracranial pressure that either too high or too low'
            lan(a,language)           
            
        if ('fever') in list1:
            a='Fevers can result from various factors, including: an infection, such as strep throat, the flu, chickenpox, pneumonia, or COVID-19. rheumatoid arthritis'
            lan(a,language)

        if ('chickenpox') in list1:
            a='The itchy blister rash caused by chickenpox infection appears 10 to 21 days after exposure to the virus and usually lasts about five to 10 days and synptoms are fever Loss of appetite Headache Tiredness and a general feeling of being unwell'
            lan(a,language)

        if ('loose motion') in message:
            a='Share on Pinterest Loose stools may be caused by diets that are high in coffee and alcohol. Certain foods, drinks, or supplements can increase the likelihood of loose stools or diarrhea occurring. Sometimes, the body can have problems digesting certain types of sugars, such as sugar alcohols and lactose'
            lan(a,language)

        if  ('how are you') in message or ('and you') in message or ('are you okay') in message:
            a='Fine thank you'
            lan(a,language)

        if  ('*') in message:
            rand = ['Be polite please']
            speekmodule.speek(rand,n,mixer)

        if ('name') in list1:
            a='My name is Jarvis, at your service sir'
            lan(a,language)

        if ('sleep mode') in message:
            rand = ['good night']
            speekmodule.speek(rand,n,mixer)
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')


        if ('what time') in message:
            tim = strftime("%X", localtime())
            rand = [tim]
            speekmodule.speek(rand,n,mixer)

    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))
