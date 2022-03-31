import speech_recognition as sr

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  
        audio = r.listen(source,2,4)
        # listen(​source, timeout, phrase_time_limit​)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en')
        print(f'You said : {query}')
    except:
        return
    query = str(query)
    return query.lower()
