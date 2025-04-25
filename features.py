import os
import re
from playsound import playsound
import eel
import webbrowser
from datetime import datetime
import wikipedia
import random
import pyautogui
import webbrowser 
import time as tt
import psutil
import pywhatkit
import pyautogui
import time 
import time
import pyjokes 
from engine.command import speak


@eel.expose
def playAssistantSound():
    music_dir = r"C://Users//Akhil//OneDrive//Desktop//anurag//anurag//engine//start_sound.mp3"
    playsound(music_dir)

# Function to tell the current time
def tell_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return f"The current time is {current_time}."
    
# Function to fetch summary from Wikipedia
def get_wikipedia_summary(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.PageError:
        return "I couldn't find any information on that topic."

# Function to Flip a coin
def flip():
    coin = ['Heads', 'Tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    return f"I Flipped the Coin and you got {toss}"

# Function to take a screenshot
def screenshot():
    name_img = tt.time()
    name_img = f'C:\\Users\\Akhil\\OneDrive\\Desktop\\anurag\\anurag\\www\\assets\\imgscr{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

# Function to roll a die
def roll():
    die = ['1', '2', '3', '4', '5', '6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    print("I Rolled A Die and you got\n"+roll)
    return f"I Rolled A Die and you got {roll}"

# Function to expose CPU Stats 
def cpu():
    usage = str(psutil.cpu_percent())
    battery = psutil.sensors_battery()
    bat=battery.percent
    return f"CPU is at {usage} percent and Battery is at {bat}"

# Function to fetch date 
def date():
    year = int(datetime.now().year)
    month = int(datetime.now().month)
    date = int(datetime.now().day)
    return f"The current date is: {date} {month} {year} "

# Function to Greet the user
def greeting():
    hour = datetime.datetime.now().hour()
    if hour >= 0 and hour<12:
        return "good morning sir i am virtual assistent Spark"
    elif hour>=12 and hour<18:
        return "good afternoon sir i am virtual assistent Spark"
    elif hour>=18 and hour<22:
        return "good evening sir i am virtual assistent Spark"
    else:
        return "good night sir i am virtual assistent Spark"

# Function to wish the User 
def wishme():
    gre = greeting()
    t= tell_time()
    d= date()
    return f"Hello Sir {gre} {t} {d} I am ready sir!!!"

def openCommand(query):
    query = query.replace("S.P.A.R.K", "")
    query = query.replace("open", "")
    query.lower()

    if query!="":
        speak("Opening "+query)
        os.system('start '+query)
    else:
         speak("not found")

# Function to send whatsapp messages
def whas():
    phone_number = "+918897911214"
    message = "Hello, this is a test message!"
    if phone_number != 0:
        pywhatkit.sendwhatmsg_instantly(phone_number, message)
        time.sleep(15)
        pyautogui.press('enter')
    else:
        print("Sorry")

def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None

#Fuction to tell a Joke 
def jokessss():
    My_joke = pyjokes.get_joke(language="en", category="neutral") 
    return My_joke


def recommend_song(mood):
    song_library = {
        "happy": ["Happy by Pharrell Williams", "Walking on Sunshine by Katrina and the Waves"],
        "sad": ["Someone Like You by Adele", "Fix You by Coldplay"],
        "energetic": ["Eye of the Tiger by Survivor", "Don't Stop Me Now by Queen"]
    }
    song = random.choice(song_library.get(mood, ["No recommendations available."]))
    s= print(song)
    v=speak(song)
    return s,v

def random_fact():
    facts = [
        "Honey never spoils.",
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries are not.",
        "A day on Venus is longer than a year on Venus.",
        "Sharks existed before trees."
    ]
    fact = random.choice(facts)
    s=print(fact)
    v=speak(fact)
    return s,v

def meditation_timer(minutes):
    import time
    print("Start meditating...")
    speak("Start meditating...")
    time.sleep(minutes * 60)
    spee = "Meditation session complete. Great job!"
    s=print(spee)
    v=speak(spee)
    return s,v

fitness_data = {"steps": 10000, "calories": 500}

def update_fitness(steps=None, calories=None):
    if steps:
        fitness_data["steps"] += steps
    if calories:
        fitness_data["calories"] += calories
    return f"Updated fitness data: {fitness_data['steps']} steps, {fitness_data['calories']} calories burned."

def fitness_summary():
    spe = f"You have walked {fitness_data['steps']} steps and burned {fitness_data['calories']} calories today."
    v= print(spe)
    s= speak(spe)
    return v,s





