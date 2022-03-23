import random
import json
import torch
import time
from brain import NeuralNetwork
from neural_network import *
from voice_output import Say
from voice_input import Listen
from functions import *


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('contents.json','r') as f:
    contents = json.load(f)

File = 'TrainingData.pth'
data = torch.load(File)

input_size = data['input_size']
hiddin_size = data['hiddin_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNetwork(input_size,hiddin_size,output_size).to(device=device)

model.load_state_dict(model_state)

model.eval()

def assistant(): 
    stm = Listen()
    result = str(stm)
    if stm == "funny":
        Say("How Are You Sir , Tell Me How Can I Help .... \n")
        assistant()
    elif stm == None: #
        time.sleep(2)
        exit()
    elif stm == "bye" or stm == "exit":
        exit()
    
    stm = tokenize(stm)
    w = bag_of_words(stm, all_words)
    w = w.reshape(1,w.shape[0])
    w = torch.from_numpy(w).to(device)
    output = model(w)

    _ , predicted = torch.max(output,dim=1)
    itm = predicted.item()
    tag = tags[itm]

    probs = torch.softmax(output,dim=1)
    prob = probs[0][itm]

    if prob.item() > 0.75:
        for conn in contents["content"]:
            if tag == conn['tag']:
                replay = random.choice(conn['responses'])
                
                if 'time' in replay:
                    get_command(replay)
                elif 'date' in replay:
                    get_command(replay)
                elif 'day' in replay:
                    get_command(replay)

                elif "wikipedia" in replay:
                    get_input_command(replay,result)
                elif "google" in replay:
                     get_input_command(replay,result)
                elif "website" in replay:
                     get_input_command(replay,result)
                elif "playmusic" in replay:
                     get_input_command(replay,result)
                elif "calculate" in replay:
                     get_input_command(replay,result)
                elif "how" in replay:
                     get_input_command(replay,result)
                elif "temperature" in replay:
                     get_input_command(replay,result)    
                else:
                    Say(replay)


while True:   
    assistant()



    