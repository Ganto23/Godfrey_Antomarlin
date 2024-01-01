import os, time, pyaudio, playsound
import gtts
import speech_recognition as sr

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""
            
        print(said)
        return
    
    get_audio()
    
