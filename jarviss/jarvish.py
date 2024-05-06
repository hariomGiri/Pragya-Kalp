import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyautogui
import pywhatkit
import pyautogui
import pyjokes


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")
    elif hour>=12 and hour<18:
         speak("Good Afternoon Boss!")
    else:
        speak("Good Evening Boss!")

def takecommond():#It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
           print("Listening...")
           r.pause_threshold = 1
           r.adjust_for_ambient_noise(source, duration=1)
           audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query
if __name__=="__main__" :
    wishme()
    while True:
        # if 1:
        query = takecommond().lower()
            # Logic for executing tasks based on query
    # Logic for executing tasks based on query
        if 'wikipedia' in query:
         speak('Searching Wikipedia...')
         try:
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2)
             speak("According to Wikipedia")
             print(results)
             speak(results)
         except:
             speak("sorry sir i am not able to find")
             print("sorry sir i am not able to find")
        elif 'play' in query:
            query=query.replace("play","")
            speak('playing'+query)
            pywhatkit.playonyt(query)
            
        elif 'open google' in query:
            speak("sir what should i search on google")
            cm = takecommond().lower()
            webbrowser.open(f"{cm}")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'lnct indore' in query:
            webbrowser.open("https://www.lnctindore.edu.in/")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        # elif 'send message' in query:
        #     pywhatkit.sendwhatmsg("+919343770661","this is for testing",9,15)
        elif 'open code' in query:
            codePath = "C:\\Users\\HARIOM GIRI\\OneDrive\\Documents\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)
        elif 'type' in query:
            speak("what should i write")
            while True:
                writeInNotepad=takecommond()
                if writeInNotepad=='exit typing':
                    speak("done sir")
                else:
                    pyautogui.write(writeInNotepad)
        elif 'joke' in query:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif 'exit program' in query:
            speak("i am leaving sir, Bye")
            quit()
            
        else:
            import chatbot
            reply = chatbot.jarvychitchat(query)
            speak(reply) 
        