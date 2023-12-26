import speech_recognition as Assistant
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener=Assistant.Recognizer()

machine=pyttsx3.init()

def talk(text):
    #global instruction
    machine.say(text)
    machine.runAndWait()

def inpuut_instruction():
    global instruction
    try:
        with Assistant.Microphone() as origin:
            print("Listening...")
            speech=listener.listen(origin)
            instruction=listener.recognize_google(speech)
            print(instruction)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction=instruction.replace("jarvis"," ")
                talk(instruction)
                print(instruction)
           
    except:
        pass
    return instruction

def play_jarvis():
    #global instruction
    instruction=inpuut_instruction()
    print(instruction)

    if "play" in instruction:
        song=instruction.replace("play","")
        talk("playing"+song)
        print("playing"+song)
        pywhatkit.playonyt(song)
    elif "time" in instruction:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is"+time)
        print(time)

    elif "date" in instruction:
        date=datetime.datetime.now().strftime('%d %B %Y')
        talk("Today's date is"+date)
        print(date)
    
    elif "are you single" in instruction:
        talk("I am in a relationship with wifi")
        #print("I am in a relationship with wifi")
    elif "how are you" in instruction:
        talk("I am fine, Thank you")
    elif "whats up" in instruction:
        talk("I am fine, Thank you")
    elif "what is your age" in instruction:
        talk("I am a program, I have no age")
        print("I am a program, I have no age")
    elif "who is your creator" in instruction:
        talk("My creator is a human being")
        print("My creator is a human being")
    elif "what is your name" in instruction:
        talk("My name is Wish! how cam i help you?")
        print("My name is Wish! how cam i help you?")
    elif "who is" in instruction:
        human=instruction.replace("who is","")
        info=wikipedia.summary(human,1)
        talk(info)
        print(info)
    elif "what is" in instruction:
        human=instruction.replace("what is","")
        info=wikipedia.summary(human,1)
        talk(info)
        print(info)
    else:
        talk("Please say the command again")
        print("Please say the command again")

play_jarvis()

