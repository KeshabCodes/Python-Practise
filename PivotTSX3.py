import speech_recognition as sr
import pyttsx3 as p
import webbrowser as w


r = sr.Recognizer()

def speak(text):
    engine = p.init()

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    
    engine.setProperty("rate", 185)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

while True:

    try:
        with sr.Microphone() as source:
            print("Listening.....")
            audio = r.listen(source)

        command = r.recognize_google(audio)
        command = command.lower()

        if "hello" in command:
            print("Hello sir, How can I help You ?")
            speak("hello sir how can I help you")
        elif "name" in command:
            print("My name is DORA-X. I am your personal AI assistant.")
            speak("My name is dora-x. I am your personal AI assistant.")
        elif "google" in command:
            print("Opening google...")
            speak("opening google")
            w.open("https://www.google.com")
            break
        elif "youtube" in command:
            print("Opening youtube...")
            speak("Opening youtube")
            w.open("https://www.youtube.com")
            break
        elif "facebook" in command:
            print("Opening facebook...")
            speak("Opening facebook")
            w.open("https://www.facebook.com")
            break
        elif "instagram" in command:
            print("Opening instagram...")
            speak("Opening instagram")
            w.open("https://www.instagram.com")
            break
        elif "exit" in command:
            print("Goodbye!")
            speak("goodbye")
            break
        else:
            print("Sorry sir, I can't do that!")
            speak("sorry sir I can't do that")

    except sr.UnknownValueError:
        print("I couldn't understand your sound. Please try again!")
        speak("I couldn't understand your voce please try again")

    except sr.RequestError:
        print("Speech Recognition service is not available!")
        speak("Speech Recognition service is not available.")