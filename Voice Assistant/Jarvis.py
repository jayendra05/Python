import pyaudio
import speech_recognition as sr
# from pygame import mixer
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
        print("Say Something")
        a="Say something"
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


        if ('goodbye') in list1 or ('bye') in list1:                          
            a='Goodbye Sir'
            lan(a,language)
            
            break
            
        elif ('hello') in list1 or ('hi') in list1:
            a='Welcome to  virtual intelligence World. At your service jayendra sir'
            lan(a,language)



        elif ('thanks') in message or ('thanks') in message or ('thank you') in message:
            a='You are wellcome'
            lan(a,language)

        elif message == ('jarvis'):
            a='Yes Sir?', 'What can I doo for you sir?'
            lan(a,language)

        elif  ('how are you') in message or ('and you') in message or ('are you okay') in message:
            a='Fine thank you'
            lan(a,language)


        # elif  ('*') in message:
        #     rand = ['Be polite please']
        #     speekmodule.speek(rand,n,mixer)

        elif ('name') in list1:
            a='My name is Jarvis, at your service sir'
            lan(a,language)

        

        elif ('sleep mode') in message:
            rand = ['good night']
            speekmodule.speek(rand,n,mixer)
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        elif ('wikipedia') in message:
           import wiki.py 

        elif ('mouse') in list1:
           import mouse.py

        elif ('write in text') in message:
            import to_write.py

        elif('write in word') in message:
            import in_words.py


        if "write a note" in message: 
            # speak("What should i write, sir") 
            note = takeCommand() 
            file = open('jarvis.txt', 'w') 
            # speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 


        if ('what time') in message:
            tim = strftime("%X", localtime())
            rand = [tim]
            speekmodule.speek(rand,n,mixer)
    except ModuleNotFoundError:
        print(" ")
    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))
