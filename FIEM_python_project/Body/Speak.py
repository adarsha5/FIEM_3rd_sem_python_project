import pyttsx3

def Speak(Text):
    engine = pyttsx3.init("sapi5") # sapi5 windows API to help to speak
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',150)
    print("")
    print(f"You: {Text}")
    print("")
    engine.say(Text)
    engine.runAndWait()

# Speak("hello how can i help")