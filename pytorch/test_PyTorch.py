#-*-coding: UTF-8 -*-
#volatile 不稳定的
#momentum 动量


import torch
from torch.autograd import Variable
import torchvision
from torch import nn
from torch import optim

# x = Variable(torch.randn(5, 5))
# print(x)
# y = Variable(torch.randn(5, 5))
# z = Variable(torch.randn(5, 5), requires_grad=True)
# a = x + y
# b = x + z
# print(a.requires_grad)
# print(b.requires_grad)

# model = torchvision.models.resnet18(pretrained=True)
# #print(model)
# for param in model.parameters():
#     param.requires_grad = False
# model.fc = nn.Linear(521, 100)
# print(model.fc)
# optimizer = optim.SGD(model.fc.parameters(),
#                        lr=1e-2, momentum=0.9)
#


#维度对不上
# regular_input = Variable(torch.randn(5, 5))
# volatile_input = Variable(torch.randn(5, 5),
#                          volatile=True)
# model = torchvision.models.resnet18(pretrained=True)
# print(model(regular_input).requires_grad)
# print(model(volatile_input).requires_grad)
# print(model(volatile_input).volatile)
# print(model(volatile_input).creator is None)
#


#本电脑无显卡
# x = torch.cuda.FloatTensor(1)
# print(x)

#没跑通
from torch.autograd import Function
from torch.autograd import gradcheck

# class Linear(Function):
#     def forward(self, input, weight, bias=None):
#         self.save_for_backward(input, weight, bias)
#         output = input.mm(weight.t())
#         if bias:
#             output += bias.unsqueeze(0).expand_as(output)
#         return output
#
#     def backward(self, grad_output):
#         input , weight, bias = self.saved_tensors
#         grad_input = grad_weight = grad_bias = None
#         if self.needs_input_grad[0]:
#             grad_input = grad_output.mm(weight)
#         if self.needs_input_grad[1]:
#             grad_weight = grad_output.t().mm(input)
#         if bias and self.needs_input_grad[2]:
#             grad_bias = grad_output.sum(0).squeeze(0)
#         return grad_input , grad_weight, grad_bias
#
# def linear(input, weight, bias=None):
#     return Linear()(input, weight, bias)
#
# input = Variable(torch.randn(5, 5).double(),
#                   requires_grad=True)
# #print(input)
# test = gradcheck(Linear(), input, 1e-6, atol=1e-4)
#
# print(test)

#重写Linear
# class Linear(nn.Module):
#     def __init__(self, input_features,
#                    output_features,
#                    bias=True):
#         self.input_features = input_features
#         self.onput_features = output_features
#         self.weight = nn.Parameter(torch.Tensor(input_features,
#                                                  output_features))
#         if bias:
#             self.bias = nn.Parameter(torch.output_features)
#         else:
#             self.register_parameter('bias', None)
#         self.weight.data.unoform_(-0.1, 0.1)
#         if bias is not None:
#             self.bias.data.uniform_(-0.1, 0.1)
#
#     def forward(self, input):
#         return Linear()(input, self.weight, self.bias)
#
import torch.nn as nn
import torch.autograd as autograd
# model = nn.Sequential(
#     nn.Conv2d(1, 20, 2),
#     nn.ReLU(),
#     nn.Conv2d(20, 1, ),
#     nn.ReLU()
# )
# m = nn.MaxPool2d(2)
# input = autograd.Variable(torch.Tensor([[[10, 20, 30, 40],
#                            [50, 60, 70, 80],
#                            [90, 100, 110, 120],
#                            [130, 140, 150, 160]],
#                            [[10, 20, 30, 40],
#                            [50, 60, 70, 80],
#                            [90, 100, 110, 120],
#                            [130, 140, 150, 160]],
#                            [[10, 20, 30, 40],
#                            [50, 60, 70, 80],
#                            [90, 100, 110, 120],
#                            [130, 140, 150, 160]]]))
# print(input)
# print(input.size())
# # maxpool = m(input)
# # print(maxpool)
#
# m = nn.Conv2d(3, 3, 2)
# conv2d = m(input)
# print(conv2d)
import cv2
a = cv2.imread('./cat.jpg')
print(a.shape)

print(a[0])
cv2.imshow('cat', a)
m = nn.Conv2d(1, 3, (2, 2))
b = m(torch.from_numpy(a[0]))
# cv2.imshow('catm', b)
cv2.waitKey(0)









