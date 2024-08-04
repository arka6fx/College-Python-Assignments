# install an external module [pip install pyttsx3]
import pyttsx3
engine = pyttsx3.init()
engine.say("I love to code")
engine.runAndWait()