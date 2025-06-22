import wikipedia
import requests

from utils.voice import speak

def get_duckduckgo_summary(query):
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        response = requests.get(url).json()
        summary = response.get("Abstract", "")
        return summary if summary else "Sorry, I couldn't find anything about that."
    except Exception as e:
        print(f"DuckDuckGo Error: {e}")
        return "Sorry, even DuckDuckGo couldn't find anything useful."

def tell_about(topic):
    try:
        topic = topic.strip(" ?.").title()
        print(f"Searching Wikipedia for: {topic}")

        summary = wikipedia.summary(topic, sentences=2)
        speak(summary)

    except wikipedia.exceptions.DisambiguationError as e:
        print(f"DisambiguationError: {e.options[:5]}")  
        speak("That topic is too broad. Try being more specific.")

    except wikipedia.exceptions.PageError:
        print("PageError: No matching page found.")
        speak(f"Sorry, I couldn't find anything about {topic}.")

    except wikipedia.exceptions.HTTPTimeoutError:
        print("Wikipedia request timed out.")
        speak("The Wikipedia service took too long to respond.")

    except Exception as e:
        print(f"Unexpected Error: {e}")
        speak("Something went wrong while searching Wikipedia.")
