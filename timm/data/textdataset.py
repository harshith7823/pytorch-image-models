from torch.utils.data import Dataset, DataLoader
import os
from os import listdir
from os.path import isfile, join
import torch

class TextDataset(Dataset):

    def __init__(self, dir_path, split):
        
        self.split = split
        self.path = dir_path
        self.len = 0
        self.filesize =[]

        onlyfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]       
        for file in onlyfiles:
            with open(self.path+"/"+file, 'r') as fp:   
                c = fp.readlines()  
                self.len += len(c)
                self.filesize.append((self.len, file))

    def __len__(self):
        return self.len

    def __getitem__(self, idx):

        t = 0 
        interested_file = ""
        
        for file in self.filesize:
            if file[0] < (idx + 1):             
                continue
            else:
                t = file[0]
                interested_file = file[1]
                break

        if len(interested_file) and t != 0:
            with open(self.path+"/"+interested_file, 'r') as fp:
                content = fp.readlines()
                ans = content[idx - (t - len(content))]
            features =  list(map(float, (ans.strip("\n").split())))
            return torch.tensor(features), torch.tensor(0 if "Normal" in interested_file else 1)
        else:
            return "Error"

# t = TextDataset("/Users/harshithg/Desktop/DL/Avg/")
# print(t.__len__())
# print(t.__getitem__(25+179))
# print(t.__getitem__(525))









