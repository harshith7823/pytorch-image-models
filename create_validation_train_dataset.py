
import os
from os.path import isfile, join
import shutil 

def reduce_file_size_to_10k(path):	
	onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f))]
	t = 0
	for file in onlyfiles:
            with open(path+"/"+file, 'r') as fp:   
                c = fp.readlines()  
                t += len(c)
                if t > 10000:
                	print(file)
                	os.remove(path+"/"+file)

def split_files_to_validation(src, dest, percent):
	onlyfiles = [f for f in os.listdir(src) if isfile(join(src, f))]
	to_move = onlyfiles[int(percent*len(onlyfiles)):]
	normal = []
	anomalous = []
	for file in onlyfiles:
		if "Normal" in file:
			normal.append(file)
		else:
			anomalous.append(file)
	move_normal = normal[:int(percent*len(normal))]
	move_anomalous = anomalous[:int(percent*len(anomalous))]
	print(len(anomalous), len(move_anomalous), len(normal), len(move_normal))
	for file in move_normal:
		shutil.move(src+"/"+file, dest) 
	for file in move_anomalous:
		shutil.move(src+"/"+file, dest) 

# path = "/Users/harshithg/Desktop/DL/Avg 2"
# reduce_file_size_to_10k(path)
# src = "/Users/harshithg/Desktop/DL/Avg 2/train"
# dest = "/Users/harshithg/Desktop/DL/Avg 2/validation"
# src = "train"
# dest = "validation"
# split_files_to_validation(src, dest, 0.1)


