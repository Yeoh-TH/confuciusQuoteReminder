import pyttsx3
import random
import time

confuciusQuotes = [
    "无欲速，无见小利。欲速，则不达，见小利，则大事不成",
    "三人行，必有我师焉",
    "学而时习之，不亦说乎？",
    "君子坦荡荡，小人长戚戚",
    "己所不欲，勿施于人",
    "知之者不如好之者，好之者不如乐之者",
    "温故而知新，可以为师矣",
    "不患人之不己知，患不知人也",
    "君子和而不同，小人同而不和",
    "君子求诸己，小人求诸人",
    "礼之用，和为贵",
]

randomQuote = 0

speaker = pyttsx3.init()

rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate-75)

voices = speaker.getProperty('voices')

def selectVoice(name):
    for voice in voices:
        if voice.name == name:
            speaker.setProperty('voice', voice.id)

# selectVoice("Grandpa (Chinese (China mainland))")
selectVoice("Sinji")
# selectVoice("Tingting")
# selectVoice("Binbin")

speaker.say("孔日：")
speaker.runAndWait()
speaker.say(confuciusQuotes[random.randint(0, len(confuciusQuotes)-1)])
speaker.runAndWait()

def showAllVoices():
    for voice in voices:
        speaker.setProperty('voice', voice.id)
        print(voice.id)
        print(voice.name)
        speaker.say(f"Hi my name is {voice.name}" )
        speaker.runAndWait()





