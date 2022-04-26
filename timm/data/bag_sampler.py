import torch
import random
from torch.utils.data.sampler import Sampler

##TODO: Ensure that all videos are covered. Make a copy of indices and remove the indices that were already picked.
class BagSampler(Sampler):
    def __init__(self, dataset):
        halfway_point = int(len(dataset)/2)
        self.first_half_indices = list(range(halfway_point))
        self.second_half_indices = list(range(halfway_point, len(dataset)))
        self.final_indices = []
        
    def __iter__(self):
        random.shuffle(self.first_half_indices)
        random.shuffle(self.second_half_indices)
        
        for i in range(len(self.first_half_indices)//32):
            self.final_indices.extend(self.first_half_indices[i*32:i*32+32])
            self.final_indices.extend(self.second_half_indices[i*32:i*32+32])
        
        print(self.final_indices)
        print(len(self.final_indices))
        return iter(self.final_indices)
        #return iter(self.first_half_indices + self.second_half_indices)
    
    def __len__(self):
        return len(self.first_half_indices) + len(self.second_half_indices)