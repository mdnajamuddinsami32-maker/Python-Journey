import speech_recognition as sr
import sounddevice as sd
import webbrowser

recognizer = sr.Recognizer()

print("Voice Assistant started!")
print("Say something...")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        command = recognizer.recognize_google(audio)
        command = command.lower()

        print("You said:", command)

        if "hello" in command:
            print("Hello Sami!")

        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")

        elif "open google" in command:
            webbrowser.open("https://www.google.com")

        elif "stop" in command or "exit" in command:
            print("Assistant stopped.")
            break

        else:
            print("I don't understand that command.")

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")

    except sr.RequestError:
        print("Internet connection problem.")