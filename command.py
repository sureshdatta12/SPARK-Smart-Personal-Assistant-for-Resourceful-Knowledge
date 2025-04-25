import pyttsx3
import speech_recognition as sr
import eel
import pywhatkit
import webbrowser
from datetime import datetime
import time
import os
import pyjokes
import eel
import playsound


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    print(voices)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)
    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)

    except Exception as e:
        return "not found"

    return query.lower()


def set_timer(seconds, message="Time's up!"):
    """Sets a timer for the specified number of seconds."""
    try:
        if seconds < 0:
            return "Timer duration must be a positive number."
        
        print(f"Timer started for {seconds} seconds...")
        time.sleep(seconds)
        response = ("Times up buddy")
        print(response)
        speak(response)
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"


@eel.expose
def allCommands():
    try:
        query = takecommand()
        print(query)
        if "time" in query:
            from engine.features import tell_time
            response = tell_time()
            speak(response)
            eel.ShowHood()
        elif "flip" in query:
            from engine.features import flip
            response = flip()
            speak(response)
            eel.ShowHood()
        elif "roll" in query:
            from engine.features import roll
            response = roll()
            speak(response)
            eel.ShowHood()
        elif "cpu" in query:
            from engine.features import cpu
            response = cpu()
            speak(response)
            eel.ShowHood()
        elif "date" in query:
            from engine.features import date
            response = date()
            speak(response)
            eel.ShowHood()
        elif "greeting" in query:
            from engine.features import greeting
            response = greeting()
            speak(response)
            eel.ShowHood()
        elif "recommend" in query:
            from engine.features import recommend_song
            s2 = query.split("for")[1].strip().split()[0]        
            recommend_song(s2)
        elif "quote" in query:
            from engine.features import random_fact
            random_fact()
            eel.ShowHood()
        elif "search" in query:
            from engine.features import searchgoo
            response = searchgoo(query)
            speak(response)
            eel.ShowHood()
        elif 'youtube' in query:
            speak("What can i search for you?")
            query = takecommand()
            print(query)
            pywhatkit.playonyt(query)
            eel.ShowHood()
        elif 'joke' in query:
            My_joke = pyjokes.get_joke(language="en", category="neutral") 
            print(My_joke)
            speak(My_joke)
            eel.ShowHood()
    # Add additional command handling as needed
        elif 'message' in query:
            from engine.features import whas
            whas()
            time.sleep(3)
            response="Message sent successfully sir!!!"
            speak(response)
            eel.ShowHood()
        elif 'made you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Jai Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
            eel.ShowHood()
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am SPARK an AI based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)
            eel.ShowHood()
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! SPARK"  
            print(na_me)
            speak(na_me)
            eel.ShowHood()
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()
            eel.ShowHood()
            exit()
        elif 'take notes' in query:
            note = takecommand()
            note='\n'+note+' '+"{:%B %d, %Y}".format(datetime.now())
            file=open('notes.txt','a')
            file.write(note)
        elif 'tell notes' in query:
            speak(' sir for what date you want the note for ?')
            date = takecommand()
            file = open('notes.txt','r')
            notetoken=0
            for i in file:
                if date in i:
                    notetoken = 1
                    speak(i)
                    break
            if notetoken == 0:
                speak('sorry sir , no notes found for the given date')
        elif "screenshot" in query:
            from engine.features import screenshot
            screenshot()
            eel.ShowHood()
        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("Opening Facebook")
            eel.ShowHood()
        elif 'open yt' in query:
            webbrowser.open("http://www.youtube.com/")
            speak("Opening Youtube")
            eel.ShowHood()
        elif 'open instagram' in query:
            webbrowser.open_new("http://www.instagram.com")
            speak("opening instagram")   
            eel.ShowHood() 
        elif 'open google' in query:
            webbrowser.open_new("http://www.google.com/")
            speak("opening google")
            eel.ShowHood()         
        elif 'open yahoo' in query:
            webbrowser.open_new("http://www.yahoo.com")
            speak("opening yahoo")        
            eel.ShowHood()
        elif 'open gmail' in query:
            webbrowser.open_new("http://mail.google.com")
            speak("opening google mail")  
            eel.ShowHood()          
        elif 'open snapdeal' in query:
            webbrowser.open_new("http://www.snapdeal.com") 
            speak("opening snapdeal")     
            eel.ShowHood()       
        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open_new("http://www.amazon.com")
            eel.ShowHood()
        elif 'open flipkart' in query:
            webbrowser.open_new("http://www.flipkart.com")
            speak("opening flipkart")  
            eel.ShowHood()
        elif 'open ebay' in query:
            webbrowser.open_new("http://www.ebay.com")
            speak("opening ebay")
            eel.ShowHood()
        elif 'music from pc' in query or "music" in query:
            speak("ok i am playing music")
            music_dir = './music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,musics[0]))
            eel.ShowHood()
        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = './video'
            videos = os.listdir(music_dir)
            os.startfile(os.path.join(video_dir,videos[0])) 
            eel.ShowHood()
        elif "alarm" in query:
            seconds = int(query.split("for")[1].strip().split()[0])  # e.g., "set alarm for 30 seconds"
            message = " ".join(query.split("for")[1].strip().split()[1:]) if "seconds" in query else "Time's up!"
            eel.ShowHood()
            return set_timer(seconds, message)
        elif 'good bye' in query:
            speak("good bye")
            exit()
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')
        elif "meditate" in query:
            from engine.features import meditation_timer
            seconds = int(query.split("for")[1].strip().split()[0])  # e.g., "set timer for 30 seconds"
            meditation_timer(seconds)
            eel.ShowHood()
        elif "fitness" in query:
            from engine.features import fitness_summary
            fitness_summary()
            eel.ShowHood()
        else:
            response = "I'm sorry, I can't help with that request."
            print(response)
            speak(response)
            return response
        eel.ShowHood()
    except:
        print("error")


def takeCommandCmd():
    query = input("Pls tell Me How Can I Help You\n")
    return query

# For chat box

@eel.expose
def callCommands(query):
    if "time" in query:
        from engine.features import tell_time
        response = tell_time()
        speak(response)
        eel.ShowHood()
    elif "flip" in query:
        from engine.features import flip
        response = flip()
        speak(response)
        eel.ShowHood()
    elif "roll" in query:
        from engine.features import roll
        response = roll()
        speak(response)
        eel.ShowHood()
    elif "cpu" in query:
        from engine.features import cpu
        response = cpu()
        speak(response)
        eel.ShowHood()
    elif "date" in query:
        from engine.features import date
        response = date()
        speak(response)
        eel.ShowHood()
    elif "greeting" in query:
        from engine.features import greeting
        response = greeting()
        speak(response)
        eel.ShowHood()
    elif "search" in query:
        from engine.features import searchgoo
        response = searchgoo(query)
        speak(response)
        eel.ShowHood()
    elif "recommend" in query:
        from engine.features import recommend_song
        s2 = query.split("for")[1].strip().split()[0]        
        recommend_song(s2)
    elif 'youtube' in query:
        speak("What can i search for you?")
        query = takecommand()
        print(query)
        pywhatkit.playonyt(query)
        eel.ShowHood()
    elif 'joke' in query:
        My_joke = pyjokes.get_joke(language="en", category="neutral") 
        print(My_joke)
        speak(My_joke)
        eel.ShowHood()
    elif "quote" in query:
        from engine.features import random_fact
        random_fact()
        eel.ShowHood()
    # Add additional command handling as needed
    elif 'message' in query:
        from engine.features import whas
        whas()
        time.sleep(3)
        response="Message sent successfully sir!!!"
        speak(response)
        eel.ShowHood()
    elif 'made you' in query or 'created you' in query or 'develop you' in query:
        ans_m = " For your information Jai Created me ! I give Lot of Thannks to Him "
        print(ans_m)
        speak(ans_m)
        eel.ShowHood()
    elif "who are you" in query or "about you" in query or "your details" in query:
        about = "I am Spark an AI based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
        print(about)
        speak(about)
        eel.ShowHood()
    elif "your name" in query or "sweat name" in query:
        na_me = "Thanks for Asking my name my self ! Spark"  
        print(na_me)
        speak(na_me)
        eel.ShowHood()
    elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
        ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
        speak(ex_exit)
        exit()
        eel.ShowHood()
        exit()
    elif 'take notes' in query:
        note = takecommand()
        note='\n'+note+' '+"{:%B %d, %Y}".format(datetime.now())
        file=open('notes.txt','a')
        file.write(note)
    elif 'tell notes' in query:
        speak(' sir for what date you want the note for ?')
        date = takecommand()
        file = open('notes.txt','r')
        notetoken=0
        for i in file:
            if date in i:
                notetoken = 1
                speak(i)
                break
        if notetoken == 0:
            speak('sorry sir , no notes found for the given date')
    elif "screenshot" in query:
        from engine.features import screenshot
        screenshot()
    elif 'facebook' in query:
        webbrowser.open("https://www.facebook.com")
        speak("opening facebook")
        eel.ShowHood()
    elif 'open yt' in query:
        webbrowser.open("http://www.youtube.com/")
        speak("Opening Youtube")
        eel.ShowHood()
    elif 'open instagram' in query:
        webbrowser.open_new("http://www.instagram.com")
        speak("opening instagram")    
        eel.ShowHood()
    elif 'open google' in query:
        webbrowser.open_new("http://www.google.com/")
        speak("opening google")
        eel.ShowHood()           
    elif 'open yahoo' in query:
        webbrowser.open_new("http://www.yahoo.com")
        speak("opening yahoo")    
        eel.ShowHood()    
    elif 'open gmail' in query:
        webbrowser.open_new("http://mail.google.com")
        speak("opening google mail")  
        eel.ShowHood()          
    elif 'open snapdeal' in query:
        webbrowser.open_new("http://www.snapdeal.com") 
        speak("opening snapdeal")
        eel.ShowHood()            
    elif 'open amazon' in query or 'shop online' in query:
        webbrowser.open_new("http://www.amazon.com")
        eel.ShowHood()
    elif 'open flipkart' in query:
        webbrowser.open_new("http://www.flipkart.com")
        speak("opening flipkart")  
        eel.ShowHood()
    elif 'open ebay' in query:
        webbrowser.open_new("http://www.ebay.com")
        speak("opening ebay")
        eel.ShowHood()
    elif 'music from pc' in query or "music" in query:
        speak("ok i am playing music")
        music_dir = './music'
        musics = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,musics[0]))

    elif 'video from pc' in query or "video" in query:
        speak("ok i am playing videos")
        video_dir = './video'
        videos = os.listdir(music_dir)
        os.startfile(os.path.join(video_dir,videos[0])) 
    elif 'good bye' in query:
        speak("good bye")
        exit()
    elif "shutdown" in query:
        speak("shutting down")
        os.system('shutdown -s')
    elif "alarm" in query:
        seconds = int(query.split("for")[1].strip().split()[0])  # e.g., "set timer for 30 seconds"
        message = " ".join(query.split("for")[1].strip().split()[1:]) if "seconds" in query else "Time's up!"
        print("Started the Alarm")
        eel.ShowHood()
        return set_timer(seconds, message)
    elif "meditate" in query:
        from engine.features import meditation_timer
        seconds = int(query.split("for")[1].strip().split()[0])  # e.g., "set timer for 30 seconds"
        meditation_timer(seconds)
        eel.ShowHood()
    elif "fitness" in query:
            from engine.features import fitness_summary
            fitness_summary()
            eel.ShowHood()
    else:
        response = "I'm sorry, I can't help with that request."
        print(response)
        speak(response)
        return response
    eel.ShowHood()
        
    
