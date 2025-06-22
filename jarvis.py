from utils.voice import speak, listen
from utils.wikepedia import tell_about
from utils.weather import get_weather
from utils.jokes import tell_joke
from utils.notes import write_note, read_notes
from utils.news import get_news


def main():
    speak("Hello! I am JARVIS. How can I help you?")
    while True:
        command=listen()

    
        if "stop" in command or "exit" in command:
              speak("Goodbye!")
              break
        
        elif "who is" in command or "what is" in command:
              topic = command.replace("who is", "").replace("what is", "").strip(" ?.").lower()
              tell_about(topic.strip())

        elif "who is" in command or "what is" in command:
               topic = (
                  command.replace("who is", "")
                  .replace("what is", "")
                  .strip(" ?.").lower()
               )
               tell_about(topic)

        elif "weather in" in command:
             city = command.replace("weather in", "").strip()
             get_weather(city) 

        elif "joke" in command:
             tell_joke()

        elif "make a note" in command or "take a note" in command:
             speak("What should I write?")
             note = listen()
             write_note(note)
         
        elif "read notes" in command or "show notes" in command:
             read_notes()

        elif "news" in command:
             get_news()

        else:
              speak("I didn't understand that command.")


if __name__ == "__main__":
    main()


