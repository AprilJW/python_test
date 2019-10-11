import math
import torch.nn as nn
import torch.nn.init as init

__all__ = ['VGG', 'vgg11']

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
    return nn.Sequential(*layers)

cfg = {
    #'A': [64, 'M', 128, 'M', 128, 128, 'M', 256, 256, 'M', 512, 512, 'M'],
    'A': [64, 'M', 128, 128, 'M', 256, 256, 'M', 256, 256],
    #'A': [64, 'M', 128, 128, 'M', 256, 256],# , 'M', 128,128, 'M', 128,128],
}

def vgg11():
    return VGG(make_layers(cfg['A']))
