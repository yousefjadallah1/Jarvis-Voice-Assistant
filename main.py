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
engine.setProperty('rate', 150)
engine.setProperty('voice', voices[2].id)

start_sentence = [
    "Hi, I am Jarvis",
    "Hello there, I am Jarvis, at your service.",
    "Hey there, I am Jarvis, at your service.",
    "Hello, I am Jarvis, designed to assist you.",
    "Hey, I am Jarvis, designed to assist you.",
    "Hello sir, I am Jarvis",
    "Hi, I am Jarvis, At your service",
    "Hey, I am Jarvis"
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
    "hi Jarvis",
    "hello Jarvis",
    "Hi",
    "Hello",
    "hey there",
    "hi there",
    "hey Jarvis",
    "good morning Jarvis",
    "good afternoon Jarvis",
    "good evening Jarvis",
    "Jarvis, greetings",
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

music_keywords = ['play', 'song', 'music', 'play for me']

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
            print('Listening to you Sir ...')
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

        # check music commands
    elif any(keyword in command for keyword in music_keywords):
        music(command)
    #     check for time
    elif 'time' in command:
        time()
    #     check for wikipedia
    elif 'who is' in command or 'search about' in command:
        informantion(command)
    #     check for jokes
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    #     if it didn't get it
    else:
        talk("say that again")


def informantion(command):
    something = command.replace('search about' or 'who is', '')
    info = wikipedia.summary(something, 1)
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
