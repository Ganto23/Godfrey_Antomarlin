import os, time, pyaudio, playsound, openai
import gtts
import speech_recognition as sr

#api_key = "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"
api_key = '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'

lang = 'en'

openai.api_key = api_key

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""
            
            try:
                said = r.recognize_google(audio)
                print(said)
                
                if "Friday" in said:
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user", "content": said}])
                    text = completion.choices[0].message.content
                    speech = gtts(text=text, lang=lang, slow=False, tld="com.au")
                    speech.save("welcome1.mp3")
                    playsound.playsound("welcome1.mp3")
                    
            except Exception as error:
                print(error)
                
        return said
    
    get_audio()
    
