
import webbrowser as wb
import speech_recognition as sr
import pyttsx3 
# import pyaudio
import datetime
import wikipedia 
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty("voice",voices[0].id)


def speak(audio):    # speak function so that engine speaks
    engine.say(audio)
    engine.runAndWait()


def wishMe(): #function to wish me at appropriate time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else :
        speak("Good evening")

    # speak("Activating Jarvis")
    # speak("jarvis Activated")
    # speak("I am jarvis, your personal assistant")
    # speak("Please Tell me what can I do for you!")


def takeCommand():
    speak("Give Command")
    print("Taking Command")

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    # response = {
    #     # "success": True,
    #     "error": None,
    #     "transcription": None
    # }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        # response["transcription"] = recognizer.recognize_google(audio)
        response = recognizer.recognize_google(audio)
    
    except sr.UnknownValueError:
        # speech was unintelligible
        # response["error"] = "Unable to recognize speech"
        print("say that again please")
        return "none"
    print("User Said", response)
    return response

if __name__ == "__main__":
     
    wishMe()
    while(1):
        query = takeCommand().lower()
    
        #logic for executing tasks
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            # print(results)
            speak(results)
        

        elif "open youtube" in query:
            urL='https://www.youtube.com'
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            wb.register('chrome', None,wb.BackgroundBrowser(chrome_path))
            wb.get('chrome').open_new_tab(urL)

        elif "open gmail" in query:
            urL='https://www.mail.google.com'
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            wb.register('chrome', None,wb.BackgroundBrowser(chrome_path))
            wb.get('chrome').open_new_tab(urL)

        elif "open upstox" in query:
            urL='https://www.pro.upstox.com'
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            wb.register('chrome', None,wb.BackgroundBrowser(chrome_path))
            wb.get('chrome').open_new_tab(urL)

        elif "open whatsapp" in query:
            urL='https://web.whatsapp.com'
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            wb.register('chrome', None,wb.BackgroundBrowser(chrome_path))
            wb.get('chrome').open_new_tab(urL)

        elif 'play music' in query:
            music_dir = 'M:\\old songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "T:\\visual Studio Code\\Code.exe"
            os.startfile(codePath)