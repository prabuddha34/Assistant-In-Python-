import pyttsx3
import pywhatkit
import datetime
import wikipedia


engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  

def speak(text):
    print("💬 Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def get_command():
    command = input("🧑 You: ").lower()
    return command

def run_assistant():
    command = get_command()

    if "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {time}")

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        info = wikipedia.summary(person, 1)
        speak(info)

    elif "date" in command:
        date = datetime.datetime.now().strftime('%B %d, %Y')
        speak(f"Today's date is {date}")

    elif "joke" in command:
        speak("Why do programmers prefer dark mode? Because light attracts bugs.")

    elif "hello" in command or "hi" in command:
        speak("Hello there! How can I assist you today?")

    elif "stop" in command or "bye" in command:
        speak("Goodbye! Have a great day!")
        exit()

    else:
        speak("Sorry, I didn't understand that. Please try again.")


while True:
    run_assistant()
