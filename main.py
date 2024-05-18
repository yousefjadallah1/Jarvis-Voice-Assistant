import datetime
import random
import wikipedia
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 180)
engine.setProperty('voice', voices[2].id)



start_sentence = [
    "Hi, I am jarvis",
    "Hello there, I am jarvis, at your service.",
    "Hey there, I am jarvis, at your service.",
    "Hello, I am jarvis, designed to assist you.",
    "Hey, I am jarvis, designed to assist you.",
    "Hello sir, I am jarvis",
    "Hi, I am jarvis, At your service",
    "Hey, I am jarvis"
]

help_sentences = [
    "How may I assist you?",
    "What can I do for you?",
    "How may I be of service?",
    "What do you require?",
    "How can I help?",
    "In what way can I assist you?",
    "How may I be of assistance?",
    "What is your command?",
    "How can I support you today?"
]

greetings = [
    "hi jarvis",
    "hello jarvis",
    "Hi",
    "Hello",
    "hey there",
    "hi there",
    "hey Siri",
    "good morning jarvis",
    "good afternoon jarvis",
    "good evening jarvis",
    "jarvis, greetings",
]

greeting_responses = [
    "Hello, sir!",
    "Hi there!",
    "Hey, how can I assist you?",
    "Greetings, master!",
    "Yes, sir?",
    "At your service!",
    "How may I help you?",
    "What can I do for you, sir?",
    "Hello! What's on your mind?"
]
else_keywords = ["didn't get it", "again please", "What's that", "another time please"]
stupid_keywords = ["haha think thats funny", "No you are", "crazy really", "Don't say that or I will block you", "I'm smarter than you if you now lol"]
music_keywords = ['play', 'song', 'music', 'play for me']
how_are_you_keywords = ["I'm great thanks for asking", "I'm good", "I'm fine thanks", "I am OK", "not my best day"]
wikipedia_keywords = ['search' , 'who is', 'what is', 'wikipedia']


start_sen = random.choice(start_sentence)
engine.say(start_sen)
help_sen = random.choice(help_sentences)
engine.say(help_sen)
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()
    print("Jarvis: "+text)



def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening to you ...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You: "+command)
            return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
    return ''




def run_jarvis():
    command = take_command()
        # check for greeting
    if any(greeting.lower() in command for greeting in greetings):
        response = random.choice(greeting_responses)
        talk(response)

    elif 'how are you' in command:
        talk(random.choice(how_are_you_keywords))

    elif 'stupid' in command:
        talk(random.choice(stupid_keywords))

        # check music commands
    elif any(keyword in command for keyword in music_keywords):
        music(command)
    #     check for time
    elif 'time' in command:
        time()
    #     check in wikipedia
    elif any(keyword in command for keyword in wikipedia_keywords):
        informantion(command)
    #     check for jokes
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    #     if it didn't get it
    else:
        talk("say that again")


def informantion(command):
    something = command.replace('search about', '')
    info = wikipedia.summary(something, 2)
    talk(info)

def music(command):
    song = command.replace('play', '')
    talk('Playing' + song)
    pywhatkit.playonyt(song)


def time():
    time_now = datetime.datetime.now().strftime('%I:%M %p')
    talk('Current time is ' + time_now)


while True:
    run_jarvis()
