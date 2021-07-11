import pyttsx3 as pp
import speech_recognition as sr
import webbrowser

a = pp.init()
a.say("Hello, I am Christan! How can I help you?")
a.runAndWait()
a.stop()

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    r.pause_threshold = 1

    print("Listening....")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    userinput = text.lower()
    print(userinput)

    if "who are you" in userinput:
        a.say("Hello, I am a  created chatbot by Khushi" )
        a.runAndWait()

    elif "what's your hobby?" in userinput:
        a.say("I love to code, what you like to do?")
        a.runAndWait()

    userinput = input().lower()

    if userinput:
        a.say("I like that to")
        a.runAndWait()
    elif "what is your gender?" in userinput:
     a.say("I don't have a gender")
    a.runAndWait()

    elif "open google" in userinput:
        webbrowser.open("google.com")
        
    elif "open youtube" in userinput:
        webbrowser.open("youtube.com")
           

except:
    print("sorry!! I don't understand.")