from time import sleep
print(">> Starting The Jarvis")
from Body.Speak import Speak
Speak(">> Starting The Jarvis")

def webcam():
    Speak(">> You can say now")
    while True:
        from Body.Listen import MicExecution
        Data = MicExecution()
        Data = str(Data)
        Data = Data.lower()
        if Data==None:
            Speak("Not recognized")
        elif 'stop' in Data:
            Speak("Ok sir .... good bye")
            break
        else:
            from Brain.AIBrain import ReplyBrain
            Reply = ReplyBrain(Data)
            Speak(Reply)
        sleep(5)
        Speak(">> give me the next command...")
webcam()









































# webcam()
# ClapDetect()
# time()
# MainExecution()
# while True:
#     from Brain.AIBrain import ReplyBrain
#     kk= input("Enter : ")
#     print(ReplyBrain(kk))
# tasks()
# from Brain.AIBrain import ReplyBrain
# abc = ReplyBrain("hi jarvis")
# Speak(abc)


# from clapNewDetection import clapNewDetection
# def clap():
#     if clapNewDetection()==True:
#         run_php_locally("another1.php")
#         print("")
#         Speak(">> Clap detected!! >>")
#         print("")
#         MainExecution()
#     else:
#         pass

# clap()




# analog_clock_show()

