import pyttsx3 as ptts
def Say(text): 
    engine = ptts.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate',180) #100-200
    print(f"Python : {text}\n")
    engine.say(text=text)
    engine.runAndWait()
# Say("Welcome To The Future Graduation Project")