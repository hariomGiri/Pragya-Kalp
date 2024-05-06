import sys
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QThread 
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
import openrouter



from ass import Ui_mainfront


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
#ui.terminalPrint(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    ui.updateMovieDynamically("speaking")
    engine.say(audio) 
    
    engine.runAndWait() #Without this command, speech will not be audible to us.
def wishme():
    ui.updateMovieDynamically("loading")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        ui.terminalPrint("Good Morning Boss!")
        speak("Good Morning Boss!")
    elif hour>=12 and hour<18:
         ui.terminalPrint("Good Afternoon Boss!")
         speak("Good Afternoon Boss!")
    else:
        ui.terminalPrint("Good Evening  Boss!")
        speak("Good Evening Boss!")
def wakeUpcommands():
    ui.updateMovieDynamically("sleeping")
    ui.terminalPrint("jarvis is sleeping...")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio,language='en-in')
            ui.terminalPrint(f"You jaust said: {query}\n")
        except:
            query = "none"
        if "wake up" in query:
            break
        
        
        
                
        

class jarvisMain(QThread):
    def __init__(self):
        super(jarvisMain, self).__init__()
        
        

    


    def run(self):
        self.runJarvis()
    
    
    # Method to interact with the OpenRouter API
    def callOpenRouterAPI(self, query):
     try:
        response = openrouter.generate(query)  # Call the OpenRouter API
        print("Received response from OpenRouter API:", response)
        return response 
     except Exception as e :
        print("Error calling OpenRouter API:", e)
        return None 
         
    
    '''
    def ai(self, prompt):
        text = ""
        client = Groq(self.apikey)
        completion = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(completion["choices"][0]["text"])
        if os.path.exists("meta files"):
            os.mkdir("meta files")

        with open (f"meta files/prompt- {random.randint(1, 234234356)}", "W") as f:
            f.write(text)
    '''
        
    def filterTheQueryForSpecificWord(self, queryToBeFiltered):
        queryToBeFiltered = queryToBeFiltered.replace("jarvis",'')
        query = queryToBeFiltered.replace("hariom",'')
        query = query.replace("hey",'')
        query = query.replace("bro",'')
        return query

        
    def takecommond(self):#It takes microphone input from the user and returns string output
        ui.updateMovieDynamically("Listening")
        r = sr.Recognizer()
        with sr.Microphone() as source:
           
           ui.terminalPrint("Listening")
           r.pause_threshold = 1
           r.adjust_for_ambient_noise(source, duration=1)
           audio = r.listen(source)
        try:
            ui.updateMovieDynamically("loading")
            
            ui.terminalPrint("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            ui.terminalPrint(f"You just said: {query}\n")
        except sr.UnknownValueError:
            ui.terminalPrint("Sorry, I didn't understand what you said.")
            return "None"
        except Exception as e:
            ui.terminalPrint(str(e))    
            speak("Say that again please...")  
            return "None"
        return query

            
        
        

        
    
    
    
    def runJarvis(self):
        wakeUpcommands()
        
        wishme()
        
        while True:
            
            query = self.takecommond().lower()
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                try:
                   query = query.replace("wikipedia", "")
                   results = wikipedia.summary(query, sentences=2)
                   speak("According to Wikipedia")
                   ui.terminalPrint(results)
                   speak(results)
                except:
                     speak("sorry sir i am not able to find")
                     ui.terminalPrint("sorry sir i am not able to find")
            elif 'play' in query:
                query=query.replace("play","")
                speak('playing'+query)
                pywhatkit.playonyt(query)

                
            
            elif 'open google' in query:
                speak("sir what should i search on google")
                cm = self.takecommond().lower()
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

            elif 'joke' in query:
                joke=pyjokes.get_joke()
                ui.terminalPrint(joke)
                speak(joke)
            elif 'exit program' in query:
                speak("i am leaving sir, Bye")
                quit()
            

            elif 'write a note' in query or 'notepad' in query:
                os.startfile("C:\\Windows\\notepad.exe")
                speak("opened Notepad application sir")
                speak("please dictate me whaat should I write")
                while True:
                  
                    query = self.takecommond().lower()
                    pyautogui.write(query)
                    filteredQuery = self.filterTheQueryForSpecificWord(query)
                    if filteredQuery.startswith('exit') or filteredQuery.startwith('stop'):
                        speak('okay sir')
                        pyautogui.hotkey('ctrl','w')
                        pyautogui.press('tab')
                        pyautogui.press('enter')
                        break
                     
                
            
                
        
             # After taking input from the user, call the OpenRouter API
            response = self.callOpenRouterAPI(query)
            if response:
                ui.terminalPrint("AI>> " + response)  # Print AI response in the terminal
                speak(response)  # Speak the AI response
            else:
                print("No response from OpenRouter API")
                speak("Sorry, I couldn't get a response from the OpenRouter API")
                
            


             
                                        
    '''          
    def excuteJarvis(self):
        wishme()
        while True:
            self.query = self.listen()
            if self.query:
                self.commands()
            else:
                pass
            '''
            
startExecution = jarvisMain()
            

class jarvisGui(QWidget):
    def __init__(self):
        super(jarvisGui, self).__init__()
        self.loginUi = Ui_mainfront()
        self.loginUi.setupUi(self)
        self.runAllMovies()
        
        self.loginUi.exit.clicked.connect(self.close)
        self.loginUi.Enter.clicked.connect(self.manualcodefromTerminal)   
                

    def runAllMovies(self):
        self.loginUi.code = QMovie("H:\\study\\vad\\UI\\code.gif")
        self.loginUi.codes.setMovie(self.loginUi.code)
        self.loginUi.code.start()
        
        self.loginUi.code = QMovie("H:\\study\\vad\\UI\\loadd.gif")
        self.loginUi.loading.setMovie(self.loginUi.code)
        self.loginUi.code.start()
        
        self.loginUi.code = QMovie("H:\\study\\vad\\UI\\wave.gif")
        self.loginUi.Label.setMovie(self.loginUi.code)
        self.loginUi.code.start()
        
        self.loginUi.code = QMovie("H:\\study\\vad\\UI\\load.gif")
        self.loginUi.load.setMovie(self.loginUi.code)
        self.loginUi.code.start()
        
        self.loginUi.code = QMovie("H:\\study\\vad\\UI\\listening.gif")
        self.loginUi.listening.setMovie(self.loginUi.code)
        self.loginUi.code.start()
        
        self.loginUi.code = QMovie("H:\\study\\vad\\UI\\venus.gif")
        self.loginUi.venus.setMovie(self.loginUi.code)
        self.loginUi.code.start()
        
        self.loginUi.code = QMovie("H:\\study\\vad\\UI\\sleeping.gif")
        self.loginUi.sleep.setMovie(self.loginUi.code)
        self.loginUi.code.start()
        
        self.loginUi.code = QMovie("H:\\study\\vad\\UI\\circle.gif")
        self.loginUi.arc.setMovie(self.loginUi.code)
        self.loginUi.code.start()
        
        startExecution.start()
    def updateMovieDynamically(self, state):
        if state == "Listening":
            self.loginUi.listening.raise_()
            self.loginUi.venus.hide()
            self.loginUi.sleep.hide()
            self.loginUi.load.hide()
            self.loginUi.loading.hide()
            self.loginUi.listening.show()
        elif state == "speaking":
            self.loginUi.venus.raise_()
            self.loginUi.listening.hide()
            self.loginUi.sleep.hide()
            self.loginUi.load.hide()
            self.loginUi.loading.hide()
            self.loginUi.venus.show()
        elif state == "loading":
            self.loginUi.loading.raise_()
            self.loginUi.venus.hide()
            self.loginUi.sleep.hide()
            self.loginUi.load.hide()
            self.loginUi.listening.hide()
            self.loginUi.loading.show()
        elif state == "sleeping":
            self.loginUi.sleep.raise_()
            self.loginUi.loading.hide()
            self.loginUi.venus.hide()
            self.loginUi.load.hide()
            self.loginUi.listening.hide()
            self.loginUi.sleep.show()
    def terminalPrint(self, text):
            self.loginUi.terminaloutput.appendPlainText(text)
    def manualcodefromTerminal(self):
            cmd = self.loginUi.lineEdit.text()
            if cmd:
                self.loginUi.lineEdit.clear()
                self.loginUi.terminaloutput.appendPlainText(f"you just typed >>{cmd}")
                if cmd == 'exit':
                 ui.close()
                elif cmd == 'help':
                        text = "I can Perform various tasks which is programmed inside me by hariom sir.\n"
                        text += "Examples are: Time, Wikipedia, play music, Google search, screenshot, joke, play YouTube video, type anything you say, sleep well or else I'll chit chat"
                        self.terminalPrint(text)
                        speak(text)  # Speak the text
                else:
                   pass
            
            else:
                pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = jarvisGui()
    ui.show()
    startExecution.start()
    sys.exit(app.exec_())