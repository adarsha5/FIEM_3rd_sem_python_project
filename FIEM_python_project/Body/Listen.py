

import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator # pip install googletrans==3.0.0

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) #Listening
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="bn-IN")
    except:
        return ""

    query = str(query).lower()
    return query

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}")
    return data 

def Mic():
    data = Listen()
    data = TranslationHinToEng(data)
    data =data.lower()
    return data

def MicExecution():
    try:
       return Mic()
    except:
        pass

# print(Mic())