from main import say
import pywhatkit
import wikipedia as wp
import webbrowser
from bs4 import BeautifulSoup
import requests

q = 'search ipl score in google'

def searchGoogle(text):
    text = text.replace("search", "")
    q = ' ipl score in google'
    text = text.replace("in google", "")
    q = 'ipl score'
    say('This is what I found on google')
    try:
        pywhatkit.search(text) #search function is used to search in browser
        # result = wp.summary(text, sentences=1)
        print(f'Bot : Searching on Google')
        say('Your Search has been ready on google')
    except:
        print('Bot : Search output is on google search')
        say('No output for speak')
def searchYoutube(text):
    text = text.replace("please", "")
    text = text.replace("search", "")
    text = text.replace("find", "")
    text = text.replace("in youtube", "")
    say("Okay, Let's search it on Youtube")
    web = 'https://www.youtube.com/results?search_query=' + text
    try:
        webbrowser.open(web)
        if 'play' in text.lower():
            text = text.replace('play',"")
            pywhatkit.playonyt(text)
        print(f'Bot : Searching it in youtube')

    except Exception as e:
        print('Bot : Unable to search')
        # say('No output for speak')

def searchWiki(text):
    say('Searching in wikipedia')
    text = text.replace('wikipedia', '')
    text = text.replace('search from wikipedia', '')
    text = text.replace('bot', '')
    result = wp.summary(text, sentences=2)
    say('According to wikipedia..')
    print('Bot : ' + result)
    say(result)

def searchTemp(text):
    if 'in' in text:
        words = text.split()
        location = words[words.index('in') + 1]
    else:
        say('Yes sure,Please tell me your location name')
        location = input('Location : ')
    web = f'https://www.google.com/search?q=temp+in+{location}'
    try:
        r = requests.get(web)
        data = BeautifulSoup(r.text, 'html.parser')
        temp = data.find('div', class_='BNeawe').text
        say(f'Current temperature in {location} is {temp}')
        print(f'Bpt : Current temperature in {location} is {temp}')
    except AttributeError as ae:
        print(ae)
        say('Try again to fetch Temp with different prompt')
    except Exception as e:
        say('Something went wrong,Try Again')
