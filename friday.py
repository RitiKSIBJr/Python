import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import wikipedia as wp


name = "ritik"

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')
# print(voices)

#setting the voice
engine.setProperty('voice',voices[1].id)

paths = {
    'notepad'   :"C:\\Program Files\\Notepad++\\notepad++.exe",
    'calculator' : "C:\\Windows\\System32\\calc.exe",
    'illustrator' : "C:\\Program Files (x86)\\Illustrator\\x86\\Support Files\\Contents\\Windows\\Illustrator.exe",
    'code' : "C:\\Users\\lette\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
}

def speak(you_speak):
    engine.say(you_speak)
    engine.runAndWait()

def wish_me():
    time = int(datetime.datetime.now().hour)

    if time >= 0 and time < 12:
        speak("Good Morning!")
    elif time >=12 and time < 17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
   
    speak(f"Hello {name}, this is friday. How can I help you?")

def take_command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)  

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')

    except Exception as e:
        print(e)
        speak("Sorry! I cannot understand. Please say again")
        query = "None"
    return query

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("Today's date is")
    speak(year)
    speak(month)
    speak(day)
   
def time():
    hour = datetime.datetime.now().hour
    min = datetime.datetime.now().minute

    speak("The time is")
    speak(hour)
    speak(min)


def open_calculator():
    speak('opening the calculator')
    os.popen(paths['calculator'])

def open_notepad():
    speak('opening the notepad')
    os.startfile(paths['notepad'])

def open_cmd():
    os.startfile(paths['start cmd'])

def open_illustrator():
    speak("Opening the illustrator cc")
    os.startfile(paths['illustrator'])

def vs_code():
    speak("Opening the vs code")
    os.startfile(paths['code'])

def wikipedia_search(query):
    result = wp.summary(query,sentences = 2)
    print(result)
    speak(result)

def greeting():
    if 'hello' in query:
        speak('hi'+name)
    elif 'bye' in query:
        speak ("bye" + name)


     
wish_me()

while True:
    query = take_command().lower()

    if 'open youtube' in query:
        webbrowser.open("youtube.com")
        #opens youtube using web browser

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open calculator' in query:
        open_calculator()

    elif 'open notepad' in query:
        open_notepad()

    elif 'open command' in query:
        open_cmd()

    elif 'open illustrator' in query:
        open_illustrator()

    elif 'open code' in query:
        vs_code()

    elif 'wikipedia' in query:
        wikipedia_search(query)

    elif 'hello' in query or 'bye' in query:
        greeting()

    elif 'exit' in  query:
        exit()

    
