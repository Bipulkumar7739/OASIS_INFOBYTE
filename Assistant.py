import speech_recognition as sr
import pyttsx3
from datetime import datetime
import pywhatkit

# Speech engine
talker = pyttsx3.init()
voices = talker.getProperty('voices')
talker.setProperty('voice', voices[1].id)
talker.setProperty('rate', 140)

# Function speak text
def speak(bipul):
    talker.say(bipul)
    talker.runAndWait()

# capture voice commands
def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Did it Speak Something")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        instruction = recognizer.recognize_google(audio)
        instruction = instruction.lower()
        print(f"You said: {instruction}")
    except sr.UnknownValueError:
        speak("I could not understand that. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Network issue. Please check your connection.")
        return ""

    return instruction

# process commands
def process_command():
    command = get_command()

    if "hello and Hii" in command:
        speak("Hello! How can I assist you today?")

    elif "time" in command:
        current_time = datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {current_time}")

    elif "date" in command:
        today_date = datetime.now().strftime('%B %d, %Y')
        speak(f"Today's date is {today_date}")

    elif "search" in command:
        search_term = command.replace("search", "").strip()
        if search_term:
            speak(f"Searching for {search_term} on the web.")
            pywhatkit.search(search_term)
        else:
            speak("Please tell me what to search for.")

    elif "about yourself" in command or "tell me about yourself" in command:
        speak("Mera naam New Hindi hai, mujhe Bipul ne banaya hai, main Bipul ka dost hoon.")

    elif command != "":
        speak("Sorry, I didn't get that. Can you please repeat?")
# Run in assistant continuously
if __name__ == "__main__":
    speak("Hello,sir I can help you")
    while True:
        process_command()