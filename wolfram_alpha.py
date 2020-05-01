import wolframalpha
from gtts import gTTS 
import os
import speech_recognition as sr

f = open("substitutions.txt","r")
l = f.readlines()
d = {}
for i in l:
    k = i.strip().split(";")
    d[k[0]] = k[1]
f.close()

f = open("meanings.txt","r")
l = f.readlines()
d2 = {}
for i in l:
    k = i.strip().split(";")
    d2[k[0]] = k[1]
f.close()
# obtain audio from the microphone
r = sr.Recognizer()
while(True):
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source,1,10)
    
    text = ''
    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio).lower()
        l2 = text.split(" ")
        l3 = []
        for i in l2:
            if i in d:
                l3.append(d[i])
            else:
                l3.append(i)
        text = ''
        for i in l3:
            text+=i+" "
        print("Google Speech Recognition thinks you said " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        text = "nothing"
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    if text == "repeat" or text == "repeat ":
        os.system("mplayer text.mp3")
    elif text == "stop" or text == "stop ":
        break
    elif text != "nothing":
        #wolfram alpha computation
        client = wolframalpha.Client("QWK49J-GR4UTVUPH7")
        res = client.query(text)
        print(next(res.results).text)
        text = str(next(res.results).text)

        # read it
        for i in d2.keys():
            if i in text:
                text = text.replace(i,d2[i])
        language = "en"
        speech = gTTS(text = text, lang = language, slow = True)
        speech.save("text.mp3")
        os.system("mplayer text.mp3")
