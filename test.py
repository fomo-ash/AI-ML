from utils.voice import speak, listen

speak("Hello! Please say something after the beep.")
command = listen()

if command:
    speak(f"You said: {command}")
else:
    speak("I couldn't hear you properly.")
