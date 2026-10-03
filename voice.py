import speech_recognition as sr
import webbrowser
import pyttsx3
import time

recognizer = sr.Recognizer()

MICROPHONE_INDEX = 1


def speak(text):
    print("Assistant:", text)

    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

    time.sleep(0.5)


speak("Hello Sami. I am ready. Please give me a command.")

while True:
    try:
        with sr.Microphone(device_index=MICROPHONE_INDEX) as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=7)

        print("Processing...")

        command = recognizer.recognize_google(audio).lower()

        print("You said:", command)

        if "hello" in command:
            speak("Hello Sami! I am hearing you. How can I assist you today?")

        if "how are you" in command:
            speak("I am doing well, thank you for asking. And you?")

        if "i am fine" in command:
            speak("That's great to hear! Do you need any help?")












        elif "open youtube" in command:
            speak("YouTube opening.")
            webbrowser.open("https://www.youtube.com")

        elif "open my github" in command:
            speak("Opening your GitHub.")
            webbrowser.open("https://github.com/mdnajamuddinsami32-maker")

        elif "open google" in command:
            speak("Google opening.")
            webbrowser.open("https://www.google.com")

        elif "open my university website" in command:
            speak("Opening your university website.")
            webbrowser.open("https://metrouni.edu.bd/")

        elif "open my facebook account" in command:
            speak("Opening your Facebook account.")
            webbrowser.open("https://www.facebook.com/")
            
        elif "open my instagram account" in command:
            speak("Opening your Instagram account.")
            webbrowser.open("https://www.instagram.com/")

        elif "open my portfolio" in command:
            speak("Opening your portfolio.")
            webbrowser.open(
                "https://mdnajamuddinsami32-maker.github.io/Portfolio-website/"
            )

        elif "stop" in command or "exit" in command:
            speak("Goodbye Sami.")
            break

        else:
            speak("Sorry, I don't understand that command.")

    except sr.WaitTimeoutError:
        print("No voice detected.")

    except sr.UnknownValueError:
        print("Could not understand.")
        speak("Sorry, I couldn't understand.")

    except sr.RequestError as e:
        print("Speech recognition error:", e)
        speak("There is a problem with speech recognition.")

    except Exception as e:
        print("Error:", e)



# pyinstaller --clean --onefile --console voice.py   ei command diye exe file banano jabe/ update kora hoy. jate new changes reflect hoy.
       