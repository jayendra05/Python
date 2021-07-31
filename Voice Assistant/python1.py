# from googletrans import Translator  # Import Translator module from googletrans package

# translator = Translator() # Create object of Translator.
# translated = translator.translate('aap ka naam kya hai',) 
# print(" Source Language:" + translated.src) 
# # Output: Source Language: ko

# print(" Translated string:" + translated.text)
from googletrans import Translator
import gtts
from playsound import playsound
def lan(a):
    translator = Translator()  # initalize the Translator object
    translations = translator.translate(a, dest='mr')  # translate two phrases to Hindi
    a=(translations.text)

    tts = gtts.gTTS(a)
    tts.save("hello.mp3")
    playsound("hello.mp3")
lan('hi how are you')
# tts = gtts.gTTS("what is your name", lang="hi")
# tts.save("hola.mp3")
# playsound("hola.mp3")
# print(gtts.lang.tts_langs())

