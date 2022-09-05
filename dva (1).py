import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib
import subprocess as sp
import pywhatkit as kit
import requests
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning! Aayush")
        speak("Good Morning! Aayush")

    elif hour>=12 and hour<18:
        print("Good Afternoon! Aayush")
        speak("Good Afternoon! Aayush")

    else:
        print("Good Evening! Aayush")
        speak("Good Evening! Aayush")

    print("I am D V A. Please tell me how may I help you")
    speak("I am D V A! Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 1
        r.energy_threshold=3000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print('Sorry, I could not understand. Could you please say that again?')
        speak('Sorry, I could not understand. Could you please say that again?')
        return "None"
    return query

def sendEmail(to,content):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('aayushchoursia200@gmail.com','A@yush2000')
    server.sendmail('aayushchoursia200@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching in Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif 'leave' in query or 'bye' in query or 'get out' in query:
            speak("I am Leaving")
            hour = int(datetime.datetime.now().hour)
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            break

        elif 'open youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = takeCommand().lower()
            kit.playonyt(video)

        elif 'open google' in query:
            speak('What do you want to search on Google, sir?')
            query = takeCommand().lower()
            kit.search(query)

        elif 'play music' in query:
            music_dir= "C:\\Users\\dell\\Music"
            song= os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir,song[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%I:%M:%S") # use %H insted of %I if you want to time in 24 hours
            speak(f"Sir, the time is {strTime} ")
        elif 'open pycharm' in query:
            pycharmPath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2\\bin\\pycharm64.exe"
            os.startfile(pycharmPath)
        elif 'open vs code' in query:
            vscodePath="C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodePath)
        elif 'send email' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                print("Enter email id")
                to = input() #"rockingrenkuparmar@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir! I am unable to send this email")
        elif 'who are you' in query:
            speak("I am D V A, sir")
            speak("I am here to help you")

        elif 'who am i' in query or 'who i am' in query:
            speak("You are Aayush! My Creater")

        elif 'love you' in query:
            speak("I love You to babu")

        elif 'hello'in query or 'hi' in query:
            speak("Hello Sir, How may I help You?")

        elif 'open camera' in query:
            sp.run('start microsoft.windows.camera:', shell=True)

        elif 'open whatsapp' in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            print("Speak Number")
            number = takeCommand().lower()
            speak("What is the message sir?")
            message = takeCommand().lower()
            kit.sendwhatmsg_instantly(f"+91{number}", message)
            speak("I've sent the message sir.")

        elif "news" in query:
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=582313f8aa824682b3009c6f584302c3"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict["articles"]
            for index, article in enumerate(arts):
                print(f"News {index + 1}")
                if index < 4:
                    print(article["title"])
                    print(article["url"])
                    speak(article["title"])
                    print("Moving Toward Next News")
                    speak("Moving Toward Next News")
                if index == 4:
                    print(article["title"])
                    print(article["url"])
                    speak(article["title"])
                    print("Thank for listining")
                    speak("Thank for listining")
                    break
