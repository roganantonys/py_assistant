import speech_recognition as sr  #used for speech recognition
import pyttsx3    # used to convert text to speech
import pywhatkit  #used for operating with whatsapp and youtube
import datetime  
import wikipedia  #to acces the wikipedia
import pyjokes

listener = sr.Recognizer() #it will recognize the input(voice)
engine = pyttsx3.init()
voices = engine.getProperty('voices') #to get a voice
engine.setProperty('voice', voices[1].id) #to get a female voice
master='ROGAN' #you can use your name here


def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('initializing python assistant(Antony)...')
print('initializing python assistant(Antony)...')


def wish_me():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            talk("Good Morning"+ master)
            print("Good Morning"+" "+ master)
        elif hour>=12 and hour<18:
            talk("Good Afternoon"+master)
            print("Good Afternoon"+" "+master)
        else:
            talk("Good Evening"+master)
            print("Good Evening"+" "+master)
        talk("i am your python assistant(Antony).How may i help you? ")
        print("i am your python assistant(Antony).How may i help you? ")

wish_me()
    
def take_command():
    try:
        with sr.Microphone() as source: #creating microphone as a source to transmit input(voice)
            listener.adjust_for_ambient_noise(source,duration=1)
            print('Listening....')
            voice = listener.listen(source) #it will listen to the input(voice)
            command = listener.recognize_google(voice) #it will take the input using google api
            command = command.lower()
            if 'antony' in command:
                command = command.replace('antony', '')
                print("your order :"+" "+command)
    except: 
        print("error occured")
        command=None
    return command


def run_antony():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        print("wait for few seconds to open YOUTUBE......")
        talk('playing ' + song)
        pywhatkit.playonyt(song)     
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')  #%I for hour(0-12),%M for minutes(0-59),%p for (AM/PM)
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        print("searching wikipedia.....")
        info = wikipedia.summary(person, 20) #it will tell about the person for 20 lines
        print(info) 
        talk(info)
    elif 'date' in command:                               
         talk('sorry, I have a headache')                     
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')                          
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_antony()

      
