import time 
import datetime 
from voice_output import Say
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