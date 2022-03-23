import time 
import datetime
import webbrowser 
import wikipedia
import pywhatkit
import pywikihow
import wolframalpha
from voice_output import Say

# Functions with single command

def get_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    Say(f"Time Now Is  {time}")

def get_date():
    date = datetime.date.today()
    Say(f"Today's Date Is  {date}")

def get_day():
    today = datetime.datetime.now().strftime("%A")
    Say(f"Today Is  {today}")


def get_command(query): 
    query = str(query)
    if 'time' in query:
        get_time()
    elif 'date' in query:
        get_date()
    elif 'day' in query:
        get_day()






def wolframalpha_settings(query):
    api_key = 'WY8246-ERXY7J3P5Y'
    request = wolframalpha.Client(api_key)
    response = request.query(query)
    try:
        return next(response.results).text
    except:
        Say('This query Is Not Defined')
# Functions with query command
def wikipedia_search(query):
    search = str(query).replace("who is","").replace("what is","").replace("about","").replace("which is","")
    result = wikipedia.summary(search)
    Say(f"The wikipedia result is :\n {result}")

def google_search(query):
    search = str(query).replace("google","").replace("search","").replace("googling","").replace("search for","").replace("search about","")
    result = pywhatkit.search(search)

def open_any_website(query):
    site = str(query).replace("open","").replace(" ","")
    web = "https://www."+str(site)+".com/"
    webbrowser.open(web)

def play_music_on_youtube(query):
    sound = str(query).replace("play","").replace("play music","").replace("music", "").replace("play video","").replace("youtube","").replace(" ","")
    pywhatkit.playonyt(sound)

def sample_calculator(query):
    operation = str(query).replace("plus","+")
    operation = str(query).replace("in","*")
    operation = str(query).replace("multiply","*")
    operation = str(query).replace("into","*")
    operation = str(query).replace("power","**")
    operation = str(query).replace("to the power","**")
    operation = str(query).replace("minus","-")
    operation = str(query).replace("from","-")
    operation = str(query).replace("div","/")
    operation = str(query).replace("divide","/")
    operation = str(query).replace("divide","/")
    operation = str(query).replace("over","/")
    Say(f"The Result is {wolframalpha_settings(operation)}")

def how_to(query):
    how = str(query)
    max_result = 1
    search = pywikihow.search_wikihow(how,max_result)
    assert len(search) == max_result
    Say(search[0].summary)


def get_tempreture(query):
    temp = str(query).replace("What is the tempreture","tempreture in")
    temp = str(query).replace("tempreture for","tempreture in")
    Say(wolframalpha_settings(temp))



def get_input_command(tag,query):
    
    if "wikipedia" in tag:
        wikipedia_search(query)
    elif "google" in tag:
        google_search(query)
    elif "website" in tag:
        open_any_website(query)
    elif "playmusic" in tag:
        play_music_on_youtube(query)
    elif "calculate" in tag:
        sample_calculator(query)
    elif "how" in tag:
        how_to(query)
    elif "temperature" in tag:
        get_tempreture(query)
    
    





