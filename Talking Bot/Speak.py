# importing speech recognition package from google api
import speech_recognition as sr  # to understand user speech
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
import wolframalpha  # to calculate strings into formula
from selenium import webdriver  # to control browser operations
import sys  # to allow closing program
import winsound  # allows to make noise
from pynput import keyboard  # log keys
import time  # finds time
from datetime import date  # retrieves time

num = 1  # mp3 file num
frequency = 500  # set Frequency To 2500 Hertz
duration = 100  # set Duration To 1000 ms == 1 second
name = 'Jacob'  # name bot will refer to you as
botName = 'Jarvis'  # bots name

# Bot Speaking


def assistantSpeaks(output):
    global num

    num += 1
    print(botName, ':', output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    file = str(num)+'.mp3'
    toSpeak.save(file)

    playsound.playsound(file, True)
    os.remove(file)

# Driver Code


def mainCode():
    assistantSpeaks('What can i do for you?')
    text = getAudio().lower()
    processText(text)

# Record User Audio


def getAudio():

    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print('Speak...')

        audio = rObject.listen(source, phrase_time_limit=5)
    print('Stop.')
    try:

        text = rObject.recognize_google(audio, language='en-US')
        print('You : ', text)
        return text

    except:

        assistantSpeaks('Could not understand your audio, PLease try again !')
        mainCode()

# Speech Processing


def processText(input):
    try:
        if 'search' in input or 'play' in input or 'open' in input:
            search_web(input)
            return

        elif 'nothing' in input:
            speak = 'Ok'
            assistantSpeaks(speak)
            return

        elif 'who are you' in input or 'define yourself' in input or 'what can you do' in input or 'what are you' in input:
            speak = '''Hello, I am ''', botName, '''. Your personal Assistant.
			I am here to make your life easier, as well as act in the same manner
			a slave would in the 17th century. '''
            assistantSpeaks(speak)
            return

        elif 'hello' in input or 'hi' in input or 'hey' in input:
            speak = 'Hello'
            assistantSpeaks(speak)
            return

        elif 'time' in input.lower():
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            speak = 'It is ' + current_time + ' currently'
            assistantSpeaks(speak)

        elif 'date' in input.lower() or 'day' in input.lower():
            today = date.today()
            d1 = today.strftime("%B %d, %Y")
            speak = 'Today is ' + d1
            assistantSpeaks(speak)

        elif 'who made you' in input.lower() or 'created you' in input.lower() or 'coded you' in input.lower():
            speak = 'I have been created by Jacob Veenchevski. Just that fact makes me loathe life.'
            assistantSpeaks(speak)
            return

        elif 'work out' in input.lower():

            app_id = 'WOLFRAMALPHA_APP_ID'
            client = wolframalpha.Client(app_id)

            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistantSpeaks('The answer is ' + answer)
            return

        elif 'exit' in input.lower() or 'bye' in input.lower() or 'sleep' in input.lower() or 'end' in input.lower() or 'finish' in input.lower() or 'terminate' in input.lower():
            assistantSpeaks('Ok bye, ' + name+'.')
            sys.exit()

        else:

            assistantSpeaks(
                'I can search the web for you. Do you want to continue?')
            ans = getAudio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return
    except:

        assistantSpeaks('A general error has occured.')

# Open Browser


def openWeb():
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.maximize_window()
    return driver

# Simple Web Search Engine


def search_web(input):

    if 'in youtube' in input.lower() or 'on youtube' in input.lower():
        driver = openWeb()
        assistantSpeaks('Opening in youtube')
        indx = input.lower().split().index('open' or 'search' or 'play')
        query = input.split()[indx + 1:]
        query = query[:-2]
        driver.get(
            "https://www.youtube.com/results?search_query=" + '+'.join(query))
        return

    elif 'youtube' in input.lower():
        driver = openWeb()
        assistantSpeaks('Opening youtube')
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get(
            "https://www.youtube.com/results?search_query=" + '+'.join(query))
        return

    elif 'in wikipedia' in input.lower() or 'on wikipedia' in input.lower():
        driver = openWeb()
        assistantSpeaks('Opening in Wikipedia')
        indx = input.lower().split().index('open' or 'search' or 'play')
        query = input.split()[indx + 1:]
        query = query[:-2]
        print(query)
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    elif 'wikipedia' in input.lower():
        driver = openWeb()
        assistantSpeaks('Opening Wikipedia')
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        print(query)
        driver.get('https://en.wikipedia.org/wiki/' + '_'.join(query))
        return

    elif 'firefox' in input or 'mozilla' in input:
        driver = openWeb()
        assistantSpeaks('Opening Mozilla Firefox')
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return

    elif 'discord' in input:
        assistantSpeaks('Opening Discord')
        os.startfile('C:/Users/jakub/AppData/Local/Discord/app-0.0.309//Discord.exe')
        return

    elif 'excel' in input:
        assistantSpeaks('Opening Microsoft Excel')
        os.startfile(
            'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return

    elif 'on the web' in input or 'on the internet' in input:
        indx = input.lower().split().index('search')
        query = input.split()[indx + 1:]
        query = query[:-3]
        driver.get('https://duckduckgo.com/?q=' +
                   '+'.join(query) + '&t=newext&atb=v249-1&ia=web')
        return

    elif 'search' in input:
        driver = openWeb()
        indx = input.lower().split().index('search')
        query = input.split()[indx + 1:]
        driver.get('https://duckduckgo.com/?q=' +
                   '+'.join(query) + '&t=newext&atb=v249-1&ia=web')
        return

    else:

        assistantSpeaks('Application not available')
        return


# Introduction Leading Driver
if __name__ == '__main__':
    assistantSpeaks('Hello, ' + name + '.')

    def on_release(key):
        if str(key) == "'`'":
            winsound.Beep(frequency, duration)
            mainCode()

    while(1):
        with keyboard.Listener(on_release=on_release) as listener:
            listener.join()
