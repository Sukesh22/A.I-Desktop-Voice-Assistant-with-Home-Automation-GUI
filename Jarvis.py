from bs4 import BeautifulSoup as bs  # pip install bs4
from plyer import notification  # pip install plyer
from sketchpy import library as lib
import speedtest
import webbrowser
import time
import PyPDF2
import sys
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QTimer, QTime, QDate, Qt,QStringListModel
from PyQt5 import QtGui
from JARVISmainfile import Ui_Frame

import sys
import pyttsx3  # pip install pyttsx3 == text data into speech using python
import datetime  # pip install SpeechRecognition == speech from mic to text
import speech_recognition as sr
import smtplib
from secrets_1 import password, my_gmail, destination
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
from pywikihow import search_wikihow
import requests
from requests import get
from newsapi import NewsApiClient
import clipboard
import os
import numpy as np
import pyjokes
import time as tt
import string
import random
import psutil
#import serial
#ser = serial.Serial('COM3', 9600)

p = password
g = my_gmail
d = destination

for i in range(3):
    a = input("Enter Password to open Jarvis :- \n")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        break
    elif (i == 2 and a != pw):
        exit()

    elif (a != pw):
        print("Try Again")

engine = pyttsx3.init()
state = None

def speak(audio):
    ui.updateMovieDynamically("Speaking")
    engine.say(audio)
    engine.runAndWait()

class jarvisMainClass(QThread):
    def __init__(self):
        super(jarvisMainClass, self).__init__()
        
    def run(self):
        self.TaskExecution()       

    def getvoices(self, voice):
        voices = engine.getProperty('voices')
        # ui.terminalPrint(voices[1].id)
        if voice == 1:
            engine.setProperty('voice', voices[2].id)
            engine.setProperty("rate", 180)
            speak("Hello this is Jarvis")

        if voice == 2:
            engine.setProperty('voice', voices[2].id)
            engine.setProperty("rate", 180)
            speak("Hello this is Jarvis")

    def time(self):
        Time = datetime.datetime.now().strftime(
            "%I:%M:%S")  # hour = I minutes = M seconds = S
        speak("The current time is:")
        speak(Time)

    def date(self):
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        date = int(datetime.datetime.now().day)
        speak("The current date is:")
        speak(date)
        speak(month)
        speak(year)

    def greeting(self):
        hour = datetime.datetime.now().hour
        if hour >= 6 and hour < 12:
            speak("Good morning sir!")
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon sir!")
        elif hour >= 18 and hour < 24:
            speak("Good Evening sir!")
        else:
            speak("Good Night sir!")

    def wishme(self):
        ui.updateMovieDynamically("Speaking")
        speak("Welcome back sir!")
        self.time()
        self.date()
        self.greeting()
        speak("Iam at your service, please tell me how can i help you")

    # while True:
    #   voice = int(input("Press 1 for female voice\nPress 2 for male voice\n"))
    #   speak(audio)
    # getvoices(voice)
    # wishme()

    def takeCommandCMD(self):
        self.query = input("please tell me how can i help you?")
        return self.query

    def takeCommandMic(self):
        ui.updateMovieDynamically("Listening")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            ui.terminalPrint("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=4, phrase_time_limit=7)
        try:
            ui.updateMovieDynamically("Loading")
            ui.terminalPrint("recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            ui.terminalPrint(f"User said: {self.query}")
        except Exception as e:
            print(e)
            speak("Say that again please...")
            return "None"
        return self.query

    def sendemail(self, to, content):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()  # server connect gmail server
        server.starttls()  # to provide security
        server.login(g, p)
        server.sendmail(g, d, content)
        server.close()

    def sendwhatsmsg(self, phone_no, message):
        Message = message
        wb.open('https://web.whatsapp.com/send?phone=' +
                phone_no+'&text='+Message)
        sleep(10)
        pyautogui.press('enter')

    def searchgoogle(self):
        speak('What should i search for?')
        search = self.takeCommandMic()
        wb.open('https://www.google.com/search?q='+search)

    def news(self):
        newsapi = NewsApiClient(api_key='6899dac2178e4126ab9220b0dd8d16a4')
        speak('What topic you need the news about?')
        topic = self.takeCommandMic()
        data = newsapi.get_top_headlines(q=topic,
                                         language='en',
                                         page_size=5)
        newsdata = data['articles']
        for x, y in enumerate(newsdata):
            ui.terminalPrint(f'{x}{y["description"]}')
            speak(f'{x}{y["description"]}')

        speak("That's it for now, i'll update you in some time")

    def text2speech(self):
        text = clipboard.paste()
        ui.terminalPrint(text)
        speak(text)

    def screenshot(self):
        name_img = tt.time()
        name_img = f'C:\\Users\\91914\\Project\\screenshot\\{name_img}.png'
        img = pyautogui.screenshot(name_img)
        img.show()

    def passwordgen(self):
        s1 = string.ascii_uppercase
        s2 = string.ascii_lowercase
        s3 = string.digits
        s4 = string.punctuation

        passlen = 8
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))

        random.shuffle(s)
        newpass = ("".join(s[0:passlen]))
        ui.terminalPrint(newpass)
        speak(newpass)

    def flip(self):
        speak("okay sir, flipping a coin")
        coin = ['Heads', 'Tails']
        toss = []
        toss.extend(coin)
        random.shuffle(toss)
        toss = ("".join(toss[0]))
        speak("I flipped the coin and you got"+toss)
        ui.terminalPrint("I flipped the coin and you got"+toss)

    def roll(self):
        speak("okay sir, rolling a die for you")
        die = ['1', '2', '3', '4', '5', '6']
        roll = []
        roll.extend(die)
        random.shuffle(roll)
        roll = ("".join(roll[0]))
        speak("I rolled a die and you got"+roll)
        ui.terminalPrint("I rolled a die and you got"+roll)

    def cpu(self):
        usage = str(psutil.cpu_percent())
        speak('CPU is at'+usage)
        ui.terminalPrint('CPU is at'+usage)
        battery = psutil.sensors_battery()
        speak("Battery is at ")
        speak(battery.percent)
        ui.terminalPrint("Battery is at ")
        ui.terminalPrint(battery.percent)

    def pdf_reader(self):
        book = open('phase1 report.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        speak(f"Total number of pages in this pdf {pages} ")
        speak("Sir please enter the page number i have to read")
        pg = int(input("Please enter the page number: "))
        page = pdfReader.getPage(pg)
        text = page.extractText()
        ui.terminalPrint(text)
        speak(text)

    def TaskExecution(self):
        self.getvoices(1)
        self.wishme()
        while True:
            self.query = self.takeCommandMic().lower()
            if 'time' in self.query:
                self.time()

            elif 'date' in self.query:
                self.date()

            elif 'email' in self.query:

                try:
                    speak('What should i say')
                    content = self.takeCommandMic()
                    to = d
                    self.sendemail(to, content)
                    speak("email has been send successfully")
                except Exception as e:
                    ui.terminalPrint(e)
                    speak("Unable to send the email")
            elif 'message' in self.query:
                user_name = {
                    'Akash': '+91 9448902880',
                    'Likhin': '+91 8088796910',
                    'Chetan': '+91 9483276735',
                    'Sukesh': '+91 9148243502',
                    'user': '+91 9483876340'
                }
                try:
                    speak('To whom you want to send the whats app message?')
                    name = self.takeCommandMic()
                    phone_no = user_name[name]
                    speak('What is the message?')
                    message = self.takeCommandMic()
                    self.sendwhatsmsg(phone_no, message)
                    speak('Message has been send')
                except Exception as e:
                    speak("Unable to send the Message")
                    print(e)

            elif 'wikipedia' in self.query:
                speak('searching on wikipedia...')
                self.query = self.query.replace('wikipedia', "")
                result = wikipedia.summary(self.query, sentences=2)
                print(result)
                speak(result)

            elif 'hello' in self.query:
                speak('Hello sir, I am Jarvis')

            elif 'how are you' in self.query:
                speak("Perfect sir")

            elif 'thank you' in self.query:
                speak('You are welcome sir')

            elif 'open command prompt' in self.query:
                os.system("start cmd")

            elif 'go to sleep' in self.query:
                speak("Ok sir, You can call me anytime")
                break

            elif 'search' in self.query:
                self.searchgoogle()

            elif 'youtube' in self.query:
                speak("What should i search on youtube?")
                topic = self.takeCommandMic()
                pywhatkit.playonyt(topic)

            elif 'weather' in self.query:
                url = 'http://api.openweathermap.org/data/2.5/weather?q=sulya&units=imperial&appid=4f30c849f85da83b8439f7244f8853b7'

                res = requests.get(url)
                data = res.json()
                weather = data['weather'][0]['main']
                temp = data['main']['temp']
                desp = data['weather'][0]['description']
                temp = round((temp - 32) * 5/9)
                print(weather)
                print(temp)
                print(desp)
                speak('Temperature : {} degree celcius'.format(temp))
                speak('weather is {}'.format(desp))

            elif 'news' in self.query:
                self.news()

            elif 'read the' in self.query:
                self.text2speech()

            elif 'open notepad' in self.query:
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif 'open vs code' in self.query:
                codepath = 'C:\\Users\\91914\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                os.startfile(codepath)

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")

            elif 'pdf reader' in self.query:
                self.pdf_reader()
                
            elif "who are you" in self.query:
               ui.terminalPrint('My Name Is Jarvis')
               speak('My Name Is Jarvis')
               ui.terminalPrint('I can Do Everything that my creator programmed me to do')
               speak('I can Do Everything that my creator programmed me to do')
 
            elif "who created you" in self.query:
               ui.terminalPrint('I Do not Know Their Name, I created with Python Language, in Visual Studio Code.')
               speak('I Do not Know Their Name, I created with Python Language, in Visual Studio Code.')    

            elif 'joke' in self.query:
                speak(pyjokes.get_joke())
                ui.terminalPrint(pyjokes.get_joke())
                
            elif "write" in self.query:
                pyautogui.hotkey('win')
                time.sleep(1)
                pyautogui.write('notepad')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.write("Team Members are:-\nSukesh S\n Akash K J\n Chethan K M\n Likhin B K", interval = 0.1)    

            elif 'screenshot' in self.query:
                self.screenshot()

            elif 'remember that' in self.query:
                rememberMessage = self.query.replace("remember that", "")
                rememberMessage = self.query.replace("Jarvis", "")
                speak("You told me to"+rememberMessage)
                remember = open("Remember.txt", "w")
                remember.write(rememberMessage)
                remember.close()

            elif 'what do you remember' in self.query:
                remember = open('Remember.txt', 'r')
                speak("You told me to "+remember.read())

            elif 'password' in self.query:
                self.passwordgen()

            elif "click my photo" in self.query:
                pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.press("enter")
                pyautogui.sleep(3)
                speak("SMILE")
                pyautogui.press("enter")

            elif 'draw' in self.query:
                speak("ok sir")
                obj = lib.rdj()
                obj.draw()

            elif 'tired' in self.query:
                speak("Playing your favorite song, sir")
                a = (1, 2, 3)
                b = random.choice(a)
                if b == 1:
                    webbrowser.open("https://www.youtube.com/watch?v=QJO3ROT-A4E")

            elif 'team members' in self.query:
                speak("Ok sir")
                speak("Your team members are :- Akash, Chethan, Likhin and Sukesh")
                ui.terminalPrint("Your team members are :- Akash, Chethan, Likhin and Sukesh")

            elif 'flip' in self.query:
                self.flip()

            elif 'roll' in self.query:
                self.roll()

            elif 'cpu' in self.query:
                self.cpu()
                
            elif "mute" in self.query:
                pyautogui.press("volumemute")    

            elif 'play music' in self.query:
                songs_dir = "D:\\Music"
                songs = os.listdir(songs_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(songs_dir, rd))

            elif 'logout' in self.query:
                os.system("shutdown -l")

            elif 'shutdown' in self.query:
                os.system("shutdown /s /t 1")

            elif 'restart' in self.query:
                os.system("shutdown /r /t 1")

            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")
                ui.terminalPrint(f"Your IP address is {ip}")

            elif 'open instagram' in self.query:
                webbrowser.open("https://www.instagram.com/")

            elif 'open facebook' in self.query:
                webbrowser.open("https://www.facebook.com/")

            elif 'open chrome' in self.query:
                webbrowser.open("https://www.chrome.com/")

            elif 'open stack overflow' in self.query:
                webbrowser.open("https://stackoverflow.com/")
                
            elif 'open gmail' in self.query:
                webbrowser.open("https://mail.google.com//")    

            elif 'internet speed' in self.query:
                import speedtest
                wifi = speedtest.Speedtest()
                upload_net = wifi.upload()/1048576  # Megabyte = 1024*1024 Bytes
                download_net = wifi.download()/1048576
                speak(f"Wifi upload speed is {upload_net}")
                speak(f"Wifi download speed is {download_net}")
                print("Wifi upload speed is", upload_net)
                print("Wifi download speed is", download_net)

            elif 'how to' in self.query:
                speak("Getting Data from the Internet !")
                op = self.query.replace("Jarvis", "")
                max_result = 1
                how_to_func = search_wikihow(op, max_result)
                assert len(how_to_func) == 1
                how_to_func[0].ui.terminalPrint()
                speak(how_to_func[0].summary)

            elif 'on the light' in self.query:
                speak("Okay sir, turning on the light")
                ser.write(b'Y')

            elif 'off the light' in self.query:
                speak("Okay sir, turning off the light")
                ser.write(b'N')

            elif 'on the fan' in self.query:
                speak("Okay sir, switching on the Fan")
                ser.write(b'Y')

            elif 'off the fan' in self.query:
                speak("Okay sir, switching off the Fan")
                ser.write(b'N')

            elif 'offline' in self.query:
                quit()
                
startExecution = jarvisMainClass()                
                
class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.jarvisUI = Ui_Frame()
        self.jarvisUI.setupUi(self)
        
        self.jarvisUI.start.clicked.connect(self.runAllMovies)
        self.jarvisUI.quit.clicked.connect(self.close)  
    
    def terminalPrint(self, text):
         self.jarvisUI.terminalOutputBox.appendPlainText(text)
         self.jarvisUI.terminalOutputBox
        
    def updateMovieDynamically(self, state):
        if state == "Speaking":
            self.jarvisUI.speak.raise_()
            self.jarvisUI.speak.show()
            self.jarvisUI.listen.hide()
            self.jarvisUI.load.hide()
        elif state == "Listening":
            self.jarvisUI.listen.raise_()
            self.jarvisUI.listen.show()
            self.jarvisUI.speak.hide()
            self.jarvisUI.load.hide()
        elif state == "Loading":
            self.jarvisUI.load.raise_()
            self.jarvisUI.load.show()
            self.jarvisUI.listen.hide()
            self.jarvisUI.speak.hide()       
            
            
    def runAllMovies(self):
    
        self.jarvisUI.codingMovie = QtGui.QMovie("C:\\Users\\91914\\Project\\GUI files\\B.G_Template_1.gif")
        self.jarvisUI.codelabel.setMovie(self.jarvisUI.codingMovie)
        self.jarvisUI.codingMovie.start()
        
        self.jarvisUI.listenMovie = QtGui.QMovie("C:\\Users\\91914\\Project\\GUI files\\listening.gif")
        self.jarvisUI.listen.setMovie(self.jarvisUI.listenMovie)
        self.jarvisUI.listenMovie.start()
        
        self.jarvisUI.speakMovie = QtGui.QMovie("C:\\Users\\91914\\Project\\GUI files\\speaking.gif")
        self.jarvisUI.speak.setMovie(self.jarvisUI.speakMovie)
        self.jarvisUI.speakMovie.start()
        
        self.jarvisUI.arcreactMovie = QtGui.QMovie("C:\\Users\\91914\\Project\\GUI files\\techcircle.gif")
        self.jarvisUI.arcreact.setMovie(self.jarvisUI.arcreactMovie)
        self.jarvisUI.arcreactMovie.start()
        
        self.jarvisUI.loadMovie = QtGui.QMovie("C:\\Users\\91914\\Project\\GUI files\\tech loading-cropped.gif")
        self.jarvisUI.load.setMovie(self.jarvisUI.loadMovie)
        self.jarvisUI.loadMovie.start()
        
        self.jarvisUI.earthMovie = QtGui.QMovie("C:\\Users\\91914\\Project\\GUI files\\Earth_Template.gif")
        self.jarvisUI.earth.setMovie(self.jarvisUI.earthMovie)
        self.jarvisUI.earthMovie.start()
        
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startExecution.start()
        
    def showtime(self):
        currentTime = QTime.currentTime()
        labelTime = currentTime.toString("hh:mm:ss")
        labbel = "Time : " +labelTime
        self.jarvisUI.textBrowser.setText(labbel)    
    
        
app = QApplication(sys.argv)  
ui = Gui_start()
ui.show()
sys.exit(app.exec_())  