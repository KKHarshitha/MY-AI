import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import pyscreeze
import openai
import json
import requests
import pywhatkit as kit
import smtplib as sm
import sample
import os

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZmNhMzE1NzQtZWZkYS00MWM5LWE1MGQtNGRiYmEwYTZkNjMzIiwidHlwZSI6ImFwaV90b2tlbiJ9.FdfHmAFqzsK9NEpodqgztHRw9gPjE0BhgtGhFVsa-l8"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hello tell me a joke!...  ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "abcd"
}
# Initialize pyttsx3 engine
engine = pyttsx3.init()
#response = requests.post(url, json=payload, headers=headers)

#result = json.loads(response.text)
#print(result['openai']['generated_text'])


def aicall(query):
    payload["text"] = query
    #print(payload)
    response = requests.post(url, json=payload, headers=headers)
    #print(response.text)
    result = json.loads(response.text)
    speak(result['openai']['generated_text'])

# Initialize pyttsx3 engine
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    t = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is " + t)

def date():
    today = datetime.datetime.now()
    speak("Today's date is " + today.strftime("%B %d, %Y"))

def wish():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    elif hour < 21:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("How can I help you today?")

def command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print("User said:", query)
    except Exception as e:
        print(e)
        speak("Can you repeat that?")
        command()
        return "None"    
    return query.lower()

def screenshot():
    im1=pyscreeze.screenshot()
    im2=pyscreeze.screenshot('C:/Users/cruel joke/Desktop/AI workshop/image.png')
    
def youtube(elem):
    kit.playonyt(elem)
    
def browser(que):
    kit.search()
    
def whatsapp(t, msg):
    kit.sendwhatmsg_instantly(t, msg)

def sendemail(to,msg):
    server = sm.SMTP('smtp.gamil.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('komalaharshitha72@gmail.com','ipoz dodv hcdo camf')
    server.sendmail('21pa1a0587@vishnu.edu.in', to, msg)
    server.close()

if __name__ == "__main__":
    wish()
    # t = command()
    # while t="hi":
    while True:
        query = command()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            search = wiki.summary(query, sentences=2)
            print(search)
            speak(search)
        elif "screenshot" in query:
            speak("Taking screenshot...")
            screenshot()
        elif "open youtube" in query:
            try:
                speak("what is needed to be search?")
                elem = command()
                speak("opening youtube...")
                youtube(elem)
            except Exception as e:
                print(e)
                speak("Failed to open youtube")
            # exit()
        elif "open browser" in query:
            try:
                speak("search...")
                que = command()
                speak("searching...")
                browser(que)
            except Exception as e:
                print(e)
                speak("Failed to browse")
        elif "send whatsapp message" in query:
            try:
                speak("provide Number")
                t=input()
                speak("provide message")
                msg=command()
                whatsapp(t,msg)
            except Exception as e:
                print(e)
                speak("Failed to send")
        elif "remember" in query:
            speak("what to remember...")
            data = command()
            speak("your input is" +data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif "say what you remember" in query:
            remember = open('data.txt', 'r')
            speak("this is the data i remember" +remember.read())
        elif "send email" in query:
            try:
                speak("what you want to send")
                msg=command()
                speak("enter email")
                to = input()
                sendemail(to,msg)
                speak("sent successfully")
            except Exception as e:
                print(e)
                speak("Failed to send")
        elif "exit" in query:
            speak("Bye Bye")
            print("Exiting")
            break
        elif "play song" in query:
            path = input("Enter path")
            sample.playsong(path)
        elif "pause the song" in query:
            sample.control("pause")
        elif "unpause" in query:
            sample.control("unpause")
            try:
                sample.playsong(path)
            except:
                print("please say play a song")
        elif "stop" in query:
            sample.control("stop")
        elif "shoutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart my pc" in query:
            os.system("shutdown /r /t/ 1")
        else:
            aicall(query)



