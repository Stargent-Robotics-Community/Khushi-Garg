import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
import speech_recognition as sr
from speech_recognition.__main__ import r, audio

a = pp.init()
a.say("Hello, I am Christan! How can I help you?")
a.runAndWait()
a.stop()

voices = a.getProperty('voices')
print(voices)
a.setProperty('voice', voices[0].id)
a.setProperty('rate',150)

r = sr.Recognizer()

wish = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
ques1 = ['How are you?', 'How are you doing?']
ques2 = ['who made you', 'who created you']
reply2 = ['I was created by Khushi right in his computer.', 'Khushi']
ques3 = ['what time is it', 'what is the time', 'time']
ques4 = ['who are you', 'what is you name']
order1 = ['open browser', 'open google']
order2 = ['open youtube', 'i want to watch a video']
exit = ['exit', 'close', 'goodbye', 'shutdown']
ques5 = ['what is your color', 'what is your colour', 'your color', 'your color?', 'what is your favourite colour', 'what is your favourite color']
order3 = ['thank you']
reply3 = ['youre welcome', 'glad i could help you']

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    r.pause_threshold = 1
    print("Listening....")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print(text)
    a.say(text)
    a.runAndWait()
except:
    print("Sorry can't understand")

if text in wish:
    random_wish = random.choice(wish)
    print(random_wish)
    engine.say(random_wish)
    engine.runAndWait()

elif text in ques1:
    engine.say('I am fine')
    engine.runAndWait()
    print('I am fine')

elif text in ques2:
    engine.say('I was made by Khushi')
    engine.runAndWait()
    reply = random.choice(reply2)
    print(reply)

elif text in order3:
    print(random.choice(reply3))
    engine.say(random.choice(reply3))
    engine.runAndWait()

elif text in ques5:
    print('Red')
    engine.say('Red')
    engine.runAndWait()

elif text in ques4:
    engine.say('I am a chatbot, silly')
    engine.runAndWait()
    print('I am a chatbot')
elif text in order2:
    webbrowser.open('www.youtube.com')

elif text in exit:
    print('see you later')
    engine.say('see you later')
    engine.runAndWait()
    exit()

elif text in ques3:

    now = datetime.datetime.now()
    print("Current date and time : ")
    print(now.strftime("The time is %H:%M"))
    engine.say(now.strftime("The time is %H:%M"))
    engine.runAndWait()

elif text in order1:
    webbrowser.open('www.google.com')

else:
    engine.say("please wait")
    engine.runAndWait()
    print(wikipedia.summary(text))
    engine.say(wikipedia.summary(text))
    engine.runAndWait()
    userInput3 = input("or else search in google")
    webbrowser.open_new('www.google.com/search?q=' + userInput3)