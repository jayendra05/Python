import subprocess
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
import keyboard



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
        print("what you want to write in text file?")
        a="what you want to write in text file?"
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
            file1 = open("C:\\Users\\Jayendra\\Desktop\\Jayendra\\speech\\myfile.txt","a")#append mode 
            file1.write(message) 
            file1.write(' ')
            file1.close() 
            a='we have written the message'
            lan(a,language)
         
        elif ('space') in message:
            keyboard.write(' ')
            a='we have given the space'
            lan(a,language)

        elif('new line') in message:
            keyboard.write('\n')   
            a='move to new line'
            lan(a,language)   

        elif('dot') in list1 or ('full stop') in message:
            keyboard.write('.')   
            a='done'
            lan(a,language)   

        elif('ampersand') in message or ('and') in message:
            keyboard.write('&')   
            a='done'
            lan(a,language) 

        elif('apostrophe') in message or ('single quote') in message:
            keyboard.write("'")   
            a='done'
            lan(a,language)

        elif('asterisk') in message or ('star') in message:
            keyboard.write("*")   
            a='done'
            lan(a,language) 

        elif('at') in message or ('at the rate') in message:
            keyboard.write("@")   
            a='done'
            lan(a,language)

        elif('backslash') in message or ('back line') in message:
            keyboard.write("\")   
            a='done'
            lan(a,language) 

        elif('first curly braces') in message or ('first braces') in message ('open brace') in message:
            keyboard.write("{")   
            a='done'
            lan(a,language) 

        elif('second curly braces') in message or ('second braces') in message ('close brace') in message:
            keyboard.write("}")   
            a='done'
            lan(a,language) 
        
        elif('first bracket') in message or ('first square bracket') in message or ('open bracket') in message or ('open square bracket') in message :
            keyboard.write("[")   
            a='done'
            lan(a,language) 

        elif('second bracket') in message or ('second square bracket') in message ('close bracket') in message or ('close square bracket') in message:
            keyboard.write("]")   
            a='done'
            lan(a,language) 

        elif('colon') in message or ('double dot') in message:
            keyboard.write(":")   
            a='done'
            lan(a,language) 

        elif('comma') in message:
            keyboard.write(",")   
            a='done'
            lan(a,language) 

        elif('dollar') in message:
            keyboard.write("$")   
            a='done'
            lan(a,language) 

        elif('open parenthesis') in message or ('open circle bracket') in message:
            keyboard.write("(")   
            a='done'
            lan(a,language)

        elif('close parenthesis') in message or ('close circle bracket') in message:
            keyboard.write(")")   
            a='done'
            lan(a,language) 

        elif('equal') in message:
            keyboard.write("=")   
            a='done'
            lan(a,language) 

        elif('exclamation  mark') in message:
            keyboard.write("!")   
            a='done'
            lan(a,language) 
        
        elif('greater than') in message:
            keyboard.write(">")   
            a='done'
            lan(a,language) 

        elif('less than') in message:
            keyboard.write("<")   
            a='done'
            lan(a,language) 

        elif('minus') in message:
            keyboard.write("{")   
            a='done'
            lan(a,language) 

        elif('percent') in message:
            keyboard.write("%")   
            a='done'
            lan(a,language) 

        elif('pipe') in message or ('bar') in message:
            keyboard.write("|")   
            a='done'
            lan(a,language) 

        elif('plus') in message:
            keyboard.write("+")   
            a='done'
            lan(a,language) 
        
        elif('hash') in message:
            keyboard.write("#")   
            a='done'
            lan(a,language) 

        elif('semi-colon') in message:
            keyboard.write(";")   
            a='done'
            lan(a,language) 

        elif('forward slash') in message:
            keyboard.write("/")   
            a='done'
            lan(a,language) 

        elif('underscore') in message:
            keyboard.write("_")   
            a='done'
            lan(a,language) 

        elif('question Mark') in message:
            keyboard.write("?")   
            a='done'
            lan(a,language) 

        elif('dot') in list1:
            keyboard.write('.')   
            a='given the dot'
            lan(a,language)   

        

        elif ('goodbye') in list1 or ('bye') in list1 or ('thank') in list1:                          
            a='Goodbye Sir'
            lan(a,language)   
            break





    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))
