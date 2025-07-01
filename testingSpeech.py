import pyttsx3
import random
import time

confuciusQuotes = [
    "无欲速，无见小利。欲速，则不达，见小利，则大事不成",
    "三人行，必有我师焉",
    "学而时习之，不亦说乎？",
    "君子坦荡荡，小人长戚戚",
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





