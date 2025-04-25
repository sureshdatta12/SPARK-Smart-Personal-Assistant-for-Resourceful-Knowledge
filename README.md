# SPARK-Smart-Personal-Assistant-for-Resourceful-Knowledge

SPARK (Smart Personal Assistant for Resourceful Knowledge) is a versatile, AI-powered virtual
assistant built to automate and simplify daily tasks through intelligent voice command processing.
Developed in Python, SPARK leverages libraries like pyttsx3 for text-to-speech, speech_recognition for
voice command interpretation, and smtplib for automating emails. This combination provides a
seamless and interactive user experience.SPARK handles a variety of productivity tasks, such as
sending emails, conducting web searches, providing real-time information, and interacting with
applications like WhatsApp. For added security, it requests confirmation before sending WhatsApp
messages, giving users control over their communication. SPARK's natural language input capability
ensures intuitive interactions, making it highly user-friendly.In addition to these productivity functions,
SPARK offers entertainment and utility features like telling jokes, managing notes, flipping coins,
rolling dice, and monitoring system performance (e.g., CPU and memory usage). It also includes more
advanced features such as real-time translation, Wikipedia queries, and media control for music and
video playback.With this comprehensive set of tools, SPARK effectively blends functionality, utility,
and entertainment, positioning it as a robust and adaptable virtual assistant for a wide range of user
needs

## Software Requirements 

* Windows Operating System: Designed specifically for the Windows platform.
* Python: Version 3.6 or higher installed on the system.
* Python Libraries to be Installed Manually:
  1. pyttsx3: For text-to-speech conversion.
  2. speech_recognition: For speech-to-text processing.
  3. smtplib: For sending emails (built-in, no manual installation needed).
  4. pyautogui: For automation of mouse and keyboard.
  5. webbrowser: For opening web pages (built-in, no manual installation needed).
  6. wikipedia: For fetching Wikipedia summaries.
  7. requests: For making HTTP requests.
  8. clipboard: For clipboard management.
  9. pywhatkit: For playing YouTube videos and sending WhatsApp messages.
  10. pyjokes: For generating random jokes.
  11. psutil: For system monitoring.
  12. googletrans: For language translation using Google Translate.
  13. translate: For additional language translation capabilities.
  
## Hardware Requirements

* Processor: Any modern processor (Intel Core i3 or equivalent).
* RAM: Minimum 4GB, recommended 8GB.
* Storage: Solid State Drive (SSD) recommended for faster performance.
* Internet Connection: Stable internet access for API communications.

## Project Structure 
```
Spark_Virtual_Assistant/
├── engine/
│   ├── init.py
│   ├── command.py
│   ├── features.py
│   └── web.py
├── www/
│   ├── assets/
│   │   └── img/
│   │       ├── logo.ico
│   │       └── start_sound.mp3
│   │   └── imgscr{timestamp}.png
│   │   └── vendore/
│   │       └── texllate/
│   │           ├── animate.css
│   ├── controller.js
│   ├── index.html
│   ├── main.js
│   ├── script.js
│   └── style.css
├── main.py
├── PyWhatKit_DB.txt
├── notes.txt
└── README.md
```

## How TO Run

1. Clone
```
git clone [repository URL]
cd Spark_Virtual_Assistant
```

2. Install
```
python3 -m venv venv (Optional but recommended)
source venv/bin/activate (or venv\Scripts\activate)
pip install -r requirements.txt
```

3. Run
```
python main.py
```
