# Voice-assistant-project-python-based-
This repository contains a Python-based voice assistant project. The assistant can recognize speech commands, perform web searches, tell jokes, and provide the current time. The project leverages libraries such as pyttsx3, speech_recognition, webbrowser, datetime, pyjokes, and gTTS.

Features
Speech Recognition: Uses speech_recognition to convert speech to text.
Text-to-Speech: Utilizes gTTS and mpg123 to convert text responses to speech.
Web Browsing: Opens web pages based on voice commands.
Time Inquiry: Provides the current time upon request.
Jokes: Tells a random joke from the pyjokes library.
Custom Commands: Responds to specific questions and phrases.

Install the required libraries:
pip install pyttsx3 SpeechRecognition webbrowser pyjokes gtts

Ensure mpg123 is installed for playing audio:
sudo apt-get install mpg123
Usage

Run the main.py script to start the voice assistant:
python main.py

Code Overview
sptext(): Listens for and recognizes speech input.
speechtx(x): Converts text to speech and plays it.
Main Loop: Continuously listens for commands and responds accordingly.

Example Commands
"Hey Rani, how are you?"
"What is your name?"
"How old are you?"
"What time is it?"
"Open YouTube"
"Tell me a joke"
"Exit"

Contributions
Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License.

