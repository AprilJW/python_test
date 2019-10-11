import argparse
import torch.nn as nn
import math
import torch
from PIL import Image, ImageEnhance
import numpy as np
import random
#
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print(args)
# #print(args.accumulate(args.integers))
"""
def make_layers(cfg, batch_norm=False):
    layers = []
    in_channels = 3
    for v in cfg:
        if v == 'M':
            layers += [nn.MaxPool2d(kernel_size=2, stride=2)]
        else:
            conv2d = nn.Conv2d(in_channels, v, kernel_size=3, padding=1)
            if batch_norm:
                layers += [conv2d, nn.BatchNorm2d(v), nn.ReLU(inplace=True)]
            else:
                layers += [conv2d, nn.ReLU(inplace=True)]
            in_channels = v
    #以元组方式传入
    a = nn.Sequential(*layers)
    #print(nn.Sequential(*layers))
    return nn.Sequential(*layers)


make_layers([64, 'M', 128, 128, 'M', 256, 256, 'M', 256, 256])

class VGG(nn.Module):
    def __init__(self, features):
        super(VGG, self).__init__()
        self.features = features
        self.classifier = nn.Sequential(
                            #nn.Dropout(),
                            nn.Linear(262144, 1024),
                            nn.ReLU(True),
                            nn.Linear(1024, 10),
                        )


         # Initialize weights
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2. / n))
                m.bias.data.zero_()

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        #print(x.size(1))
        #classifier = nn.Sequential(
        #                nn.Dropout(),
        #                nn.Linear(x.size(1), 256),
        #                nn.ReLU(True),
        #                nn.Linear(256, 18),
        #            )

        x = self.classifier(x)

        return x
VGG(make_layers([64, 'M', 128, 128, 'M', 256, 256, 'M', 256, 256]))

"""

import os
#http://30.24.145.7:8080/boundary/_
# z-oss-paper_encrypted-000077cae126106ed8a56d68f22263e7.jpg

#root_dir='/alps-security-storage/zoloz/yufei.gyf/boundary/src_img/'

class AllDataset(Dataset):
    def __init__(self, label_file, root_dir):
        self.label = open(label_file, 'r').read()[:-1].split('\n')
        self.root_dir = root_dir

    def __len__(self):
        return len(self.label)

    def randomprocess(self, image):
        enh_bri = ImageEnhance.Brightness(image)

        image = enh_bri.enhance(random.uniform(0.5, 1.5))

        enh_col = ImageEnhance.Color(image)
        image = enh_col.enhance(random.uniform(0.5, 2))

        enh_con = ImageEnhance.Contrast(image)
        image = enh_con.enhance(random.uniform(0.5, 2))

        enh_sha = ImageEnhance.Sharpness(image)
        image = enh_sha.enhance(random.uniform(0.5, 2))
        return image

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, self.label[idx].split('\t')[0])
        # image = io.imread(img_name)/float(255.)
        src = Image.open(img_name)

        bbox = self.label[idx].split('\t')[1:11]
        bbox = list(map(float, bbox))

        # simple
        if 1:
            image = src.resize((256, 256))
            image = self.randomprocess(image)
            image = np.array(image) / 255.
            # bbox = bbox / 500.

            label = torch.FloatTensor(bbox) * 256 / 500.
            image = np.transpose(image, (2, 1, 0))
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

        x0_ = random.randint(0, x0)
        y0_ = random.randint(0, y0)
        x1_ = random.randint(0, 500 - x1)
        y1_ = random.randint(0, 500 - y1)

        newsrc = src.crop((x0_, y0_, 500 - x1_, 500 - y1_))
        w, h = newsrc.size

        bbox[0] = float(bbox[0] - x0_) / w
        bbox[1] = float(bbox[1] - y0_) / h
        bbox[2] = float(bbox[2] - x0_) / w
        bbox[3] = float(bbox[3] - y0_) / h
        bbox[4] = float(bbox[4] - x0_) / w
        bbox[5] = float(bbox[5] - y0_) / h
        bbox[6] = float(bbox[6] - x0_) / w
        bbox[7] = float(bbox[7] - y0_) / h
        image = newsrc.resize((256, 256))

        image = self.randomprocess(image)
        image = np.array(image) / 255.

        label[:-1] = torch.FloatTensor(bbox)
        image = np.transpose(image, (2, 1, 0))
        sample = [torch.FloatTensor(image), torch.FloatTensor(label)]
        return sample
train_loader = torch.utils.data.DataLoader(AllDataset(label_file='./train5.txt', root_dir='/alps-security-storage/zoloz/yufei.gyf/boundary/src_img/'), batch_size=batch_size, shuffle=True, num_workers=workers, pin_memory=True)

