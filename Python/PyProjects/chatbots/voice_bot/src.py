import speech_recognition as sr
import pyttsx3
import datetime
from datetime import date
import wikipedia
import webbrowser
import pywhatkit
import os

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        dialog = "Good Morning"
        print(dialog)
        speak(dialog)

    elif 12 <= hour < 18:
        dialog = "Good Afternoon"
        print(dialog)
        speak(dialog)

    else:
        dialog = "Good Evening"
        print(dialog)
        speak(dialog)

    dialog = "how may I help you?"
    print(dialog)
    speak(dialog)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1)
        print('Listening...')
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en')
        print(f'User said: {query}\n')

    except Exception as e:
        dialog = "Sorry, I didn't get it, Please say it again..."
        print(dialog)
        speak(dialog)
        return 'None'
    return query


if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time = datetime.datetime.now().strftime('%I %M %p')
            print(time)
            speak('Right now, the time is' + time)

        elif 'date' in query:
            date = date.today().strftime('%d %B %Y %A')
            print(date)
            speak('Today, it is' + date)

        elif 'how are you' in query:
            dialog1 = 'I am absolutely fine, thank you'
            print(dialog1)
            speak(dialog1)

        elif 'stupid' in query:
            dialog2 = (
                'I am absolutely Sorry for disappointing you, please tell me to do something again and I shall not disappoint you.')
            print(dialog2)
            speak(dialog2)

        elif 'awesome' in query:
            dialog3 = (
                'Thank You for the compliment, nice to know that I was useful to you, By the way, you are awesome too.')
            print(dialog3)
            speak(dialog3)

        elif 'tell me about' in query:
            query = query.replace('tell me about', '')
            results = wikipedia.summary(query, 5)
            print(results)
            speak(results)

        elif 'google' in query:
            speak('opening google')
            webbrowser.open('google.com')

        elif 'youtube' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')

        elif 'facebook' in query:
            speak('opening facebook')
            webbrowser.open('fb.com')

        elif 'insta' in query:
            speak('opening instagram')
            webbrowser.open('instagram.com')

        elif 'telegram' in query:
            speak('opening telegram')
            webbrowser.open('telegram.com')

        elif 'github' in query:
            speak('opening github')
            webbrowser.open('github.com')

        elif 'kaggle' in query:
            speak('opening kaggle')
            webbrowser.open('kaggle.com')

        elif 'search' in query:
            results = query.replace('search', '')
            dialog4 = 'What do you want me to search?'
            print(dialog4)
            speak(dialog4)
            word = takeCommand()
            dialog5 = 'Redirecting to Google'
            print(dialog5)
            speak(dialog5)
            pywhatkit.search(word)

        elif 'play' in query:
            ytvideo = query.replace('play', '')
            speak('playing' + ytvideo)
            pywhatkit.playonyt(ytvideo)

        elif 'happy song' in query:
            speak("playing a chosen happy song for you")
            webbrowser.open('https://youtu.be/pRbxlpvXw2s')

        elif 'sad song' in query:
            speak("playing a chosen sad song for you")
            webbrowser.open('https://youtu.be/rNhW1KwjqJw')

        elif 'mail' in query:
            speak('opening gmail')
            webbrowser.open('gmail.com')

        elif 'restart pc' in query:
            speak('Restarting the system')
            os.system('shutdown /r /t 1')

        elif 'shutdown pc' in query:
            speak('Shutting down the system')
            os.system('shutdown /s /t 1')

        elif 'exit' in query:
            dialog6 = 'Thank you for using me, have a nice day'
            print(dialog6)
            speak(dialog6)
            exit()

        else:
            speak('Sorry, I am not able to do that, please try again')
