import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import keyboard
import requests
import os

engine = pyttsx3.init('sapi5')

# This line connect voices to our AI.
voices = engine.getProperty('voices')   # print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetme():
    # speak("Hi Voxie here. How can I help you?")

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Manas") 
        speak("Hi Voxie here. How can I help you?")


    elif hour > 12 and hour < 18:
        speak("Good Afternoon manas")
        speak("Hi Voxie here. How can I help you?")


    else:
        speak("Good evening Manas")
        speak("Hi Voxie here. How can I help you?")

def get_weather(city):
    api_key = "6cbe782d761c4147df6163863c0f3834"
    base_url = "http://api.openweathermap.org/data/2.5/weather"


    params = {
        "q":city,
        "appid": api_key,
        "units": "metric"  
    }

    response = requests.get(base_url,params=params)
    weather_data= response.json()

    if response.status_code == 200:
        temperature = weather_data["main"]["temp"]
        conditions = weather_data["weather"][0]["description"]
        return f"The current weather in {city} is {conditions} with a temperature of {temperature} degress Celsius. "
    else:
        return "Sorry, I couldn't retrieve the weather information at the moment. "   




def takeCommand():
    # It takes microphone input from the user and return string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("Listening")
            print("Listening...")
            r.pause_threshold = 0.7
            r.timeout = 4
            r.phrase_time_limit = 4
            # audio = r.listen(source, timeout=5, phrase_time_limit=5, threshold=3000, pause_threshold=0.8)
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query} \n ")

        except Exception as e:
            # print(e)
            speak("Say that again please")
            print("Say that again please....")
            return "None"
        return query

# def launch_application

def close_tab():
    speak("Closing all tab")
    keyboard.press_and_release('ctrl + w')

if __name__ == "__main__":
    # speak("Manas is a good boy")
    greetme()
    while True:
        query = takeCommand().lower()

        if 'please stop' in query:
            speak("Ok!!! feel free to ask any query")
            break  # Exit the loop when "stop" is said

    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'weather' in query:
            speak("Sure! Please specify the city")
            city = takeCommand().lower()
            weather_info = get_weather(city)
            print(weather_info)
            speak(weather_info)

        elif'youtube open kro' in query:
            webbrowser.open("youtube.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open indeed' in query:
            webbrowser.open("indeed.com")

        elif 'open naukri' in query:
            webbrowser.open("naukri.com")

        elif 'open linkedin'in query:
            webbrowser.open("linkedin.com")

        elif 'closed all  tab' in query:
            close_tab()

        elif 'play music' in query:
            music_dir = 'E://GameModerz/audio'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" sir The time is {strTime}")