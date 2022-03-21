import numpy as np
import json
import torch
import torch.nn as nn
from torch.utils.data import Dataset , DataLoader
from brain import NeuralNetwork
from neural_network import tokenize,stem,bag_of_words

with open('contents.json','r') as f:
    data = json.load(f)

all_words = []
tags      = []
xy        = []

for content in data['content']:
    tag = content['tag']
    tags.append(tag)
    for patern in content['patterns']:
        w = tokenize(patern)
        all_words.extend(w)
        xy.append((w,tag))

ignore_words = ['/',',','?','.','$','!','#','@']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

x_train = []  # input

y_train = []  # output

for (patern_stm, tag) in xy:
    bag = bag_of_words(patern_stm,all_words)
    x_train.append(bag)
    label = tags.index(tag)
    y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)

number_epochs = 2000
batch_size = 8
lr = 0.001
input_size = len(x_train[0])
hiddin_size = 8
output_size = len(tags)

print("Training The Model ..... ")

class ChatDataSet(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    def __getitem__(self,index):
        return self.x_data[index],self.y_data[index]
    
    def __len__(self):
        return self.n_samples

ds = ChatDataSet()

train_loader = DataLoader(dataset=ds,
                          batch_size=batch_size,
                          shuffle=True, 
                          num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# --------------------------------------------------------------------
model = NeuralNetwork(input_size,hiddin_size,output_size).to(device=device)

criterion = nn.CrossEntropyLoss() # getting error < Activation Function > 

optimizer = torch.optim.Adam(model.parameters(),lr=lr)


for epoch in range(number_epochs):
    for (words,labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype = torch.long).to(device)

        outputs = model(words) 

        loss = criterion(outputs,labels)

        optimizer.zero_grad() 

        loss.backward()

        optimizer.step()

    if (epoch+1) % 100 == 0:
        print(f"Epoch [{epoch+1} of {number_epochs}] , loss[{loss.item():.8f}]")

print(f"Final Loss = [{loss.item():.8f}]")



new_data = {
    "model_state":model.state_dict(),
    "input_size":input_size,
    "hiddin_size":hiddin_size,
    "output_size":output_size,
    "all_words":all_words,
    "tags":tags
}

File = "TrainingData.pth"
torch.save(new_data,File)

print(f"Training Data Is Completely Saved In {File}")
