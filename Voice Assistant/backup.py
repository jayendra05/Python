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
def lan(a,language):
    translator = Translator()  # initalize the Translator object
    translations = translator.translate(a, dest=language)  # translate two phrases to Hindi
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
    
        # translations = translator.translate('', dest=language)  # translate two phrases to Hindi
        # rand=(translations.text)
           
        # tts = gtts.gTTS(rand)
        # tts.save("hello.mp3")
        # playsound("hello.mp3")
        # os.remove('hello.mp3')
        
    

        if ('goodbye') in list1 or ('bye') in list1:                          
            # rand = ['Goodbye Sir']
            # speekmodule.speek(rand,n,mixer)
            translations = translator.translate('Goodbye', dest=language)  # translate two phrases to Hindi
            rand=(translations.text)
            
            tts = gtts.gTTS(rand)
            tts.save("hello.mp3")
            playsound("hello.mp3")
            os.remove('hello.mp3')
            break
            
        if ('hello') in list1 or ('hi') in list1:
            # rand = ['Wellcome to Jarvis virtual intelligence project. At your service sir.']
            # speekmodule.speek(rand,n,mixer)
            # translations = translator.translate('Wellcome to  virtual intelligence World. At your service sir', dest=language)  # translate two phrases to Hindi
            # rand=(translations.text)
           
            # tts = gtts.gTTS(rand)
            # tts.save("hello.mp3")
            # playsound("hello.mp3")
            # os.remove('hello.mp3')
            a='Welcome to  virtual intelligence World. At your service sir'
            lan(a,language)

        if ('thanks') in message or ('tanks') in message or ('thank you') in message:
            # rand = ['You are wellcome', 'no problem']
            # speekmodule.speek(rand,n,mixer)
            translations = translator.translate('You are wellcome', dest=language)  # translate two phrases to Hindi
            rand=(translations.text) 
            tts = gtts.gTTS(rand)
            tts.save("hello.mp3")
            playsound("hello.mp3")
            os.remove('hello.mp3')

        if message == ('jarvis'):
            # rand = ['Yes Sir?', 'What can I doo for you sir?']
            # speekmodule.speek(rand,n,mixer)
            translations = translator.translate('Yes Sir?', 'What can I doo for you sir?', dest=language)  # translate two phrases to Hindi
            rand=(translations.text)
            
            tts = gtts.gTTS(rand)
            tts.save("hello.mp3")
            playsound("hello.mp3")
            os.remove('hello.mp3')

        if  ('how are you') in message or ('and you') in message or ('are you okay') in message:
            # translator = Translator()
            # translations = translator.translate('Fine thank you', dest='hi')  
            # rand=(translations.text)
            # tts = gtts.gTTS(rand)
            # tts.save("hello1.mp3")
            # playsound("hello1.mp3")
            # os.remove('hello1.mp3')
            # a=Fine thank you
            # rand = ['Fine thank you']
            # speekmodule.speek(rand,n,mixer)
            lan('Fine thank you',language)

        if  ('*') in message:
            rand = ['Be polite please']
            speekmodule.speek(rand,n,mixer)

        if ('name') in list1:

            translations = translator.translate('My name is Jarvis, at your service sir', dest=language)
            rand=(translations.text)
            # rand1 = ['My name is Jarvis, at your service sir']
            # speekmodule.speek(rand1,n,mixer)
            tts = gtts.gTTS(rand)
            speekmodule.speek(tts,n,mixer)
            # tts.save("hello.mp3")
            # playsound("hello.mp3")
            # os.remove('hello.mp3')


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
