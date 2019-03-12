import re
import os
import sys
import pafy
import urllib
import pyttsx3
import smtplib
import playsound
import webbrowser
import urllib.parse
from random import *
from gtts import gTTS
import urllib.request
from datetime import date
from datetime import time
from datetime import datetime
from bs4 import BeautifulSoup
import speech_recognition as sr
city = ['Pokhara' , 'Kathmandu' , 'India']
def talk(audio):
    engine = pyttsx3.init()
    print(audio)
    engine.say(audio)
    engine.runAndWait()
def talk_to_me(audio):
    print(audio)
    tts = gTTS(text = audio , lang='en')
    tts.save('audio.mp3')
    #os.system('vlc audio.mp3')
    playsound.playsound('audio.mp3', True)

def myCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source , duration = 1)
        audio= r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said " + command + "\n")
    except sr.UnknownValueError:
        command = myCommand()
    return command
def download(text):
    talk("Downloading Songs")
    query_string = urllib.parse.urlencode({"search_query" : text})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    print("http://www.youtube.com/watch?v=" + search_results[0]) 
    url = "http://www.youtube.com/watch?v=" + search_results[0]
    video = pafy.new(url)
    print(video.title)
    filename = video.title + '.mp3'
    if os.path.exists(filename):
        talk("File already Exists")
        #playsound.playsound(filename,True)
    else:
        bestaudio = video.getbestaudio()
        bestaudio.download(filename)
        talk("Song Downloaded")
        #playsound.playsound(filename,True)
    
def play(text):
    talk("Downloading Songs")
    query_string = urllib.parse.urlencode({"search_query" : text})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    print("http://www.youtube.com/watch?v=" + search_results[0]) 
    url = "http://www.youtube.com/watch?v=" + search_results[0]
    video = pafy.new(url)
    print(video.title)
    filename = video.title + '.mp3'
    if os.path.exists(filename):
        talk("File already Exists")
        playsound.playsound(filename,True)
    else:
        bestaudio = video.getbestaudio()
        bestaudio.download(filename)
        talk("Song Downloaded")
        playsound.playsound(filename,True)
    

    
    
   
def search(query):
    address2 = "https://en.wikipedia.org/wiki/%s" % (query)
    getRequest2 = urllib.request.Request(address2, None, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})
    urlfile2 = urllib.request.urlopen(getRequest2)
    htmlResult2 = urlfile2.read(200000)
    urlfile2.close()
    soup2= BeautifulSoup(htmlResult2,'lxml')
    
    unwantedTags = ['a' , 'i' , 'b' , 'strong','cite']
    for tag in unwantedTags:
        for match in soup2.findAll(tag):
            match.replaceWithChildren()
    results2 = soup2.find_all('p')
    for i in range(5):
        print(results2[i].text)
        talk(results2[i].text)
def news():
    address = "http://www.foxnews.com"
    getRequest = urllib.request.Request(address, None, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})
    
    urlfile = urllib.request.urlopen(getRequest)
    htmlResult = urlfile.read(200000)
    urlfile.close()

    soup = BeautifulSoup(htmlResult,'lxml')
    unwantedTags = ['a' , 'cite' , 'b', 'strong']
    for tag in unwantedTags:
        for match in soup.findAll(tag):
            match.replaceWithChildren()

    results = soup.find_all('h2')
    number  = int(input("Enter the number of new you want to listen: "))
    for i in range(number):
        talk(results[i].text)

def location(query):
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    url = 'https://www.google.com/maps/place/%s' % (query)
    talk("Opening Maps")
    web = webbrowser.get(chrome_path)
    web.open_new_tab(url)
def makegooglesearch(query):
    webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % query)


    
def assistant(command):
    if 'Facebook' in command:
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        url = 'https://www.facebok.com'
        talk("Opening Facebook")
        
        web = webbrowser.get(chrome_path)
        web.open_new_tab(url)
    elif 'what\'s up' in command:
        talk("Chilling bro")
    elif 'email' in command:
        talk("Who is the recipient")
        recipient = myCommand()
        if 'John' in recipient:
            talk("What should I say")
            content = myCommand()
            mail = smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login('onvideo55@gmail.com' ,'Canubeatmenme1')
            mail.sendmail('Sangat Baral' , 'baralsangat55@gmail.com' , content)
            mail.close()
            talk('Email Sent')
    elif 'song' in command:
        talk("Which song would you like to listen")
        song = myCommand()
        talk("Would you like to listen or download?")
        whattodo = myCommand()
        if 'play' in whattodo:
            play(song)
        if 'download' in whattodo:
            download(song)
    elif 'today' in command:
        audio = date.today()
        talk(audio)
    elif 'time' in command:
        audio = datetime.now().strftime('%H:%M:%S')
        talk(audio)
    elif 'City' in command:
        talk("Which city you want me to locate")
        location(myCommand())
    elif ' make search'  in command:
        talk("What should I search, Sir?")
        query = myCommand()
        talk("Should I search in GOOGLE or in Wikipedia?")
        command = myCommand()
        if 'Wikipedia' in command:
            talk("searching wikipedia")
            search(query)
        elif 'Google' in command:
            
            makegooglesearch(query)
        else:
            talk("No decision taken")
       
    elif 'news' in command:
        
        news()
    elif 'shutdown my PC' in command:
        talk("Are you sure you want to shut down your pc")
        yesorno = myCommand()
        if 'yes' in yesorno:
            os.system("shutdown /s /t 1")
        elif 'no' in yesorno:
            exit()
    elif 'restart my pc' in command:
        talk("Are you sure you want to shut down your pc")
        if 'yes' in yesorno:
            os.system("shutdown /r /t 1")
        elif 'no' in yesorno:
            exit()
        
    elif 'Youtube' in command:
        talk('What should I search')
        query = myCommand()
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        url = 'https://www.youtube.com/results?search_query=' + query
        talk("Opening Youtube")
        
        web = webbrowser.get(chrome_path)
        web.open_new_tab(url)
        
    elif 'exit' in command:
         sys.exit()
            
    else:
        print("No action found")

talk("Hello Sir, How can I help you?")

while(True):
    assistant(myCommand())
            
            
        
        
        
        
