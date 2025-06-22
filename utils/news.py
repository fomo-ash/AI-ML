import requests
from utils.voice import speak

def get_news():
    try:
        res = requests.get("https://inshortsapi.vercel.app/news?category=technology")
        if res.status_code == 200:
            articles = res.json().get("data")[:3]
            for article in articles:
                speak(article["title"])
        else:
            speak("Couldn't fetch news.")
    except:
        speak("Network error.")
