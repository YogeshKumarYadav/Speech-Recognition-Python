#import pyttsx3
import datetime
#import speech_recognition as tellme
import wikipedia
import webbrowser
import os
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wakeup():
  timeh = int(datetime.datetime.now().hour)
    
  if (timeh >= 0 and timeh < 12):
    print("\nGood morning sir")
    speak("Good morning sir.....")
    
  elif(timeh >= 12 and timeh < 4):
    print("\nGood afternoon sir")
    speak("Good afternoon sir.....")

  else:
    print("\nGood Evening sir")
    speak("Good Evening sir.....")

  print("I am Jarvis\nHow may I help you")
  speak("I am Jarvis.......how may i help you.....")    
     
def takecommand():
  data = tellme.Recognizer()
    
  with tellme.Microphone() as source:
    print ("\nListening...")
    data.energy_threshold=1000
    data.pause_threshold = 1
    data.operation_timeout = 6
    ask = data.listen(source)   

  try:
    print ("Recognising...")
    query = data.recognize_google(ask,language='en-in')
    print ("%s\n"%(query))
      
  except Exception as exp:
    #print(exp)
    #print ("Could not understand Please ask it again...")
    query="Could not understand Please ask it again..."

  return query   

wakeup()

while True:
  query = takecommand().lower()
      
  if ("wikipedia" in query):
    speak("Searching wikipedia...")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences=2)
    print("According to wikipedia %s"%(results))
    speak("According to wikipedia...")
    speak(results)

  elif ("youtube" in query):
    speak("Opening youtube...")
    webbrowser.open("youtube.com")    

  elif ("google" in query):
    speak("opening google...")
    webbrowser.open("google.com")

  elif ("search" and "on web" in query):
    query = query.replace("search ","")
    query = query.replace("on web","")
    speak("searching...")
    webbrowser.open(query)    

  elif ("time" in query):
    timeh = int(datetime.datetime.now().hour)
    timem = int(datetime.datetime.now().minute)        
    print("The time is %d:%d"%(timeh,timem))
    speak("It's %d %d"%(timeh,timem))

  elif ("open visual studio" in query):
    path1="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(path1)

  elif ("say" in query):
    query=query.replace("say ","")
    print(query)
    speak(query)
      
  elif ("go and sleep" in query):
    print("Good bye sir...  Thank you for your time")
    speak("good bye sir.....thank you for your time")
    exit()

  else:
    print (query)
    speak("can not say anything about it.........please ask another question") 
