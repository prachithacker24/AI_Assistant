import os
from main import say
import datetime
import google.generativeai as genai
import webbrowser
import pywhatkit
import pyautogui

sites = {
    'youtube': 'https://www.youtube.com/',
    'google': 'https://www.google.com/',
    'wikipedia': 'https://www.wikipedia.com/',
    'instagram': 'https://www.instagram.com/'
}
def openSites(text):
    for i in sites:
        if f'open {i}'.lower() in text.lower():
            say(f'opening {i}')
            webbrowser.open(sites[i])
            print(f'Bot : opening {i}')

def playingMusic(text):
    musicPath = 'C:/Users/User/Music/Itrati-chali.mp3'
    print('Bot : Playing music')
    say('Playing music')
    os.system(musicPath)

def tellTime(text):
    strfTime = datetime.datetime.now().strftime("%H:%M:%S")
    print(f'Bot : Current time is {strfTime}')
    say(f'Current time is {strfTime}')

def openCamera(text):
    os.system('start microsoft.windows.camera:')
    print('Bot : Opening Camera')
    say('Opening Camera')

def openApps(text):
    os.system('start shell:AppsFolder')
    print('Bot : Opening Apps')
    say('Opening Apps')

def takeExit(text):
    print("Bot : I am taking exit Have a good day!")
    say("I am taking exit Have a good day!")
    exit()

def chat(prompt):
    chatStr = ""
    chatStr += f"Bot : "

    genai.configure(api_key="AIzaSyBABpOxFgTjsdS_1wWa_8TiJMQ85VNPyQM")

    # Set up the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])

    convo.send_message(prompt)
    response = convo.last.text
    chatStr += response
    print(chatStr)
    if len(response.splitlines()) > 2:
        say('Here is data about your search')
    else:
        say(response)

def takeScreenshot(text):
    im = pyautogui.screenshot()
    im.save("D:/ss.jpg")

