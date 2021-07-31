#!/usr/bin/env python
#
# Copyright 2010 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

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

while (i<1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        n=(n+1)     
        print("Say something!")
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



# POLITE JARVIS ============================================================================================================= BRAIN 1
    
        if ('goodbye') in list1 or ('bye') in list1:                          
            rand = ['Goodbye Sir']
            speekmodule.speek(rand,n,mixer)
            break
            
        if ('hello') in list1 or ('hi') in list1:
            rand = ['Wellcome to Jarvis virtual intelligence project. At your service sir.']
            speekmodule.speek(rand,n,mixer)

        if ('thanks') in message or ('tanks') in message or ('thank you') in message:
            rand = ['You are wellcome', 'no problem']
            speekmodule.speek(rand,n,mixer)

        if message == ('jarvis'):
            rand = ['Yes Sir?', 'What can I doo for you sir?']
            speekmodule.speek(rand,n,mixer)

        if  ('how are you') in message or ('and you') in message or ('are you okay') in message:
            rand = ['Fine thank you']
            speekmodule.speek(rand,n,mixer)

        if  ('*') in message:
            rand = ['Be polite please']
            speekmodule.speek(rand,n,mixer)

        if ('name') in list1:
            translations = translator.translate('My name is Jarvis, at your service sir', dest=language)  # translate two phrases to Hindi
            rand=(translations.text)
            # rand1 = ['My name is Jarvis, at your service sir']
            # speekmodule.speek(rand1,n,mixer)
            tts = gtts.gTTS(rand)
            tts.save("hello.mp3")
            playsound("hello.mp3")
            os.remove('hello.mp3')

# USEFUL JARVIS ============================================================================================================= BRAIN 2

        if ('wi-fi') in message:  
            REMOTE_SERVER = "www.google.com"
            speekmodule.wifi()
            rand = ['We are connected']
            speekmodule.speek(rand,n,mixer)

        if ('.com') in message :
            rand = ['Opening' + message]         
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            speekmodule.speek(rand,n,mixer)
            webbrowser.get(Chrome).open('http://www.'+message)
            print ('')
            

        if ('google maps') in message:
            query = message
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
            rand = [result+'on google maps']
            speekmodule.speek(rand,n,mixer)


        if ('sleep mode') in message:
            rand = ['good night']
            speekmodule.speek(rand,n,mixer)
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')


        if ('what time') in message:
            tim = strftime("%X", localtime())
            rand = [tim]
            speekmodule.speek(rand,n,mixer)

    # exceptions
    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))
