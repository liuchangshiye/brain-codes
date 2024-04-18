import os
import nibabel as nib
import numpy as np
from PIL import Image
import json
path_1 ="/hdd1/changshuo/PRECISE_PROSPECTIVE_PROCESSED_20231212"
path_2="/hdd8/zhulei/brain-data/PRECISE_PROCESSED"
path_3="/hdd8/zhulei/brain-data/PRECISE_PROCESSED_CONTROLS"

synthstrip_dict={}

for pid in os.listdir(path_1):
    if pid.startswith("PRECISE"):
    # if pid.startswith("2191_"):
        print('process: ', pid)
        for folder in os.listdir(os.path.join(path_1, pid)):
            if 'ct_nii' in folder:
                file_size = []
                for file in os.listdir(os.path.join(path_1, pid, folder)):
                    if '.nii' in file:
                        file_size.append((file, os.path.getsize(os.path.join(path_1, pid, folder, file))))
                if(len(file_size)==0):
                    continue
                file_size.sort(key=lambda x: x[1], reverse=True)
                ct_nii_filename = os.path.join(path_1, pid, folder, file_size[0][0])
                synthstrip_dict[os.path.join(path_1, pid)]=ct_nii_filename

for pid in os.listdir(path_2):
    # if pid.startswith("PRECISE"):
    if pid.startswith("2191_"):
        print('process: ', pid)
        for folder in os.listdir(os.path.join(path_2, pid)):
            if 'ct_nii' in folder:
                file_size = []
                for file in os.listdir(os.path.join(path_2, pid, folder)):
                    if '.nii' in file:
                        file_size.append((file, os.path.getsize(os.path.join(path_2, pid, folder, file))))
                if(len(file_size)==0):
                    continue
                file_size.sort(key=lambda x: x[1], reverse=True)
                ct_nii_filename = os.path.join(path_2, pid, folder, file_size[0][0])
                synthstrip_dict[os.path.join(path_2, pid)]=ct_nii_filename

for pid in os.listdir(path_3):
    # if pid.startswith("PRECISE"):
    if pid.startswith("2191_"):
        print('process: ', pid)
        for folder in os.listdir(os.path.join(path_3, pid)):
            if 'ct_nii' in folder:
                file_size = []
                for file in os.listdir(os.path.join(path_3, pid, folder)):
                    if '.nii' in file:
                        file_size.append((file, os.path.getsize(os.path.join(path_3, pid, folder, file))))
                if(len(file_size)==0):
                    continue
                file_size.sort(key=lambda x: x[1], reverse=True)
                ct_nii_filename = os.path.join(path_3, pid, folder, file_size[0][0])
                synthstrip_dict[os.path.join(path_3, pid)]=ct_nii_filename

with open("./synthstrip_dict.json", "w") as json_file:
    json.dump(synthstrip_dict, json_file, indent=4) 