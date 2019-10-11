import pandas as pd
import os
from skimage import io, transform
from torch.utils.data import Dataset, DataLoader
from PIL import Image, ImageEnhance
from torch.autograd import Variable
import torch.nn.functional as F
from torch import nn
import torch
import torchvision.transforms as transforms
import numpy as np
import random



class AllDataset(Dataset):
    def __init__(self, label_file, root_dir):
        self.label = open(label_file,'r').read()[:-1].split('\n')
        self.root_dir = root_dir
    def __len__(self):
        return len(self.label)

    def randomprocess(self,image):
        enh_bri = ImageEnhance.Brightness(image)  
          
        image = enh_bri.enhance(random.uniform(0.5,1.5))  
     
        enh_col = ImageEnhance.Color(image)  
        image = enh_col.enhance(random.uniform(0.5,2))  
    
        enh_con = ImageEnhance.Contrast(image)  
        image = enh_con.enhance(random.uniform(0.5,2))  
      
        enh_sha = ImageEnhance.Sharpness(image)   
        image = enh_sha.enhance(random.uniform(0.5,2))  
        return image

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, self.label[idx].split('\t')[0])
        #image = io.imread(img_name)/float(255.)
        src = Image.open(img_name)

        bbox = self.label[idx].split('\t')[1:11]
        bbox = list(map(float,bbox))
        
        # simple
        if 1:
            image = src.resize((256,256))
            image = self.randomprocess(image)
            image = np.array(image)/255.
            #bbox = bbox / 500.

            label = torch.FloatTensor(bbox) * 256 / 500.
            image = np.transpose(image,(2,1,0))
            sample = [torch.FloatTensor(image), label]
            return sample

        idx = int(self.label[idx].split('\t')[-1])
        label = torch.zeros(9)
        label[-1] = idx

        if bbox[0] < bbox[6]:
            x0 = int(bbox[0])
        else:
            x0 = int(bbox[6])
    
        if bbox[1] < bbox[3]:
            y0 = int(bbox[1])
        else:
            y0 = int(bbox[3])
    
        if bbox[4] > bbox[2]:
            x1 = int(bbox[4])
        else:
            x1 = int(bbox[2])
    
        if bbox[5] > bbox[7]:
            y1 = int(bbox[5])
        else:
            y1 = int(bbox[7])
    
        if x0 < 0:
            x0 = 0
        if y0 < 0:
            y0 = 0
        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0


        x0_ = random.randint(0,x0)
        y0_ = random.randint(0,y0)
        x1_ = random.randint(0,500-x1)
        y1_ = random.randint(0,500-y1)



        newsrc = src.crop((x0_, y0_, 500-x1_, 500-y1_))
        w,h = newsrc.size

        bbox[0] = float(bbox[0]-x0_)/w
        bbox[1] = float(bbox[1]-y0_)/h
        bbox[2] = float(bbox[2]-x0_)/w
        bbox[3] = float(bbox[3]-y0_)/h
        bbox[4] = float(bbox[4]-x0_)/w
        bbox[5] = float(bbox[5]-y0_)/h
        bbox[6] = float(bbox[6]-x0_)/w
        bbox[7] = float(bbox[7]-y0_)/h
        image = newsrc.resize((256,256))

        image = self.randomprocess(image)
        image = np.array(image)/255.

        label[:-1] = torch.FloatTensor(bbox)
        image = np.transpose(image,(2,1,0))
        sample = [torch.FloatTensor(image), torch.FloatTensor(label)]
        return sample
