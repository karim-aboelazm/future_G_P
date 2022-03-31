import pyttsx3 as ptts
def Say(text): 
    engine = ptts.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[4].id)
    engine.setProperty('rate',180) #100-200
    print(f"Python : {text}\n")
    engine.say(text=text)
    engine.runAndWait()
 


