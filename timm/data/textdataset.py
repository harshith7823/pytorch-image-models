from torch.utils.data import Dataset, DataLoader
import os
import torch
import glob
import numpy as np


class TextDataset(Dataset):
    def __init__(self, dir_path, split):
        self.path = dir_path
        self.split = split
        def listdir_nohidden(AllVideos_Path):  # To ignore hidden files
            file_dir_extension = os.path.join(AllVideos_Path, '*.txt')
            for f in glob.glob(file_dir_extension):
                if not f.startswith('.'):
                    yield os.path.basename(f)

        self.All_Videos = sorted(listdir_nohidden(self.path))
        #print(self.path)
        #print("len=", len(All_Videos))
        self.All_Videos.sort()


    def __len__(self):
        count = 0
        for root_dir, cur_dir, files in os.walk(self.path):
            count += len(files)
        #print('file count:', count)
        count = count*32
        return count

    def __getitem__(self, idx):
        # index sequentially as per file list

        # Go to file idx//32
        # Get label(1x1) based on file name
        # Get vector(1x4096) at idx%32 in the file
        #return a tensor x*y (x*y = 4096) and target tensor (1,) //Use x,y = 16,256

        #print("index=",idx)
        
        #print(All_Videos)
        VideoPath = os.path.join(self.path, self.All_Videos[idx//32])
        print("idx=", idx, "video=",VideoPath)
        f = open(VideoPath, "r")
        feat = idx%32
        words = f.read().split()
        features = np.float32(words[feat * 4096:feat * 4096 + 4096])
        features = torch.tensor(features)
        #print(features.shape)
        if len(features) == 0:
            print(idx)
            print(VideoPath)
        #features = torch.reshape(features, (16, 256))
        # features = torch.reshape(features, (196, 768))
        features = torch.reshape(features, (1, 4096))
        #features = torch.rand((196, 768))
        #print(VideoPath)
        #if VideoPath.find('Normal') == -1:
        if 'Normal' in VideoPath:
            label = 0
        else:
            label = 1

        label = torch.tensor(label)
        #print(label.size())
        label = label.unsqueeze(0)
        #label = torch.reshape(label, (1, 1))
        #print(features.shape)
        #print(features)
        #print(label.shape)
        #print(label)

        return features, label
