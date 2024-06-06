import google.generativeai as genai
import win32com.client
from bs4 import BeautifulSoup
import requests
import datetime
import speech_recognition as sr
import os
import webbrowser
speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    speaker.Speak(text)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1

        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="eng-in")
            # print(f'user said: {query}')
            return query
        except Exception as e:
            return 'Unable to hear you'

if __name__ == "__main__":
    print('AI is ready to assist')
    say('Bot is ready what can I do for you?')
    print('Bot : Welcome, Enter your prompt here')
    while True:
        # print("Listening....")
        # text = take_command()

        print('User : ', end="")
        try:
            # text = take_command().lower()
            # print(text)
            text = input().lower()
        except:
            print('Sorry, I am unable  to hear you,Enter manually')
            say('Sorry, I am unable  to hear you,Enter manually')
            text = input().lower()

        if 'site' in text.lower():
            from Actions import openSites
            openSites(text)
        elif 'play music'.lower() in text:
            from Actions import playingMusic
            playingMusic(text)
        elif 'time'.lower() in text:
            from Actions import tellTime
            tellTime(text)
        elif 'open camera'.lower() in text:
            from Actions import openCamera
            openCamera(text)
        elif 'open apps' in text:
            from Actions import openApps
            openApps(text)
        elif 'screenshot' in text:
            from Actions import takeScreenshot
            takeScreenshot(text)
        elif 'exit' in text:
            from Actions import takeExit
            takeExit(text)
        elif 'wikipedia' in text:
            from Search import searchWiki
            searchWiki(text)
        elif 'youtube' in text:
            from Search import searchYoutube
            searchYoutube(text)
        elif 'google' in text:
            from Search import searchGoogle
            searchGoogle(text)
        elif 'temp' in text:
            from Search import searchTemp
            searchTemp(text)
        else:
            print('Processing...')
            from Actions import chat
            try:
                chat(text)
            except Exception as e:
                say('Unable to fetch')
                print('Bot : Unable to fetch')
