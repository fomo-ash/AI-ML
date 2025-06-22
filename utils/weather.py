import requests
from utils.voice import speak

def get_weather(city):
    try:
        res = requests.get(f"https://wttr.in/{city}?format=3")
        if res.status_code == 200:
            speak(res.text)
        else:
            speak("Couldn't fetch weather.")
    except:
        speak("Network error.")
