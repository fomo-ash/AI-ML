import requests
from utils.voice import speak
def tell_joke():
    try:
        res=requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
        if res.status_code==200:
            joke=res.json().get("joke")
            speak(joke)
        else:
            speak("No joke found.")
    except:
        speak("Error getting a joke")