from utils.voice import speak

def write_note(text):
    with open("notes.txt", "a") as f:
        f.write(text + "\n")
    speak("Note saved.")

def read_notes():
    try:
        with open("notes.txt", "r") as f:
            notes = f.read()
            speak("Here are your notes.")
            speak(notes)
    except:
        speak("No notes found.")
