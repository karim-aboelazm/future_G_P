import pyttsx3 as ptts
def Say(text): 
    engine = ptts.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', 'MSTTS_V110_enCA_LindaM')
    engine.setProperty('rate',180) #100-200
    print(f"Python : {text}\n")
    engine.say(text=text)
    engine.runAndWait()
    # for i in range(len(voices)):
    #     print(f"Voice [{i}] id : {voices[i].id}")
    # print(len(voices))



