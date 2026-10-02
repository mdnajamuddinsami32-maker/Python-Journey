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

        elif "open my github" in command:
            webbrowser.open("https://github.com/mdnajamuddinsami32-maker")

        elif "open my facebook account" in command:
            webbrowser.open("https://www.facebook.com")

        elif "open my instagram account" in command:
            webbrowser.open("https://www.instagram.com/?__pwa=1")

        elif "open my university website" in command:
            webbrowser.open("https://metrouni.edu.bd/")

        elif "open my portfolio" in command:
            webbrowser.open("https://mdnajamuddinsami32-maker.github.io/Portfolio-website/")






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