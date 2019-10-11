##-*-coding: UTF-8 -*-
import numpy as np
import cv2
import os
from matplotlib import pyplot as plt


# img = cv2.imread(r"./cat.jpg")
#print(img)
#大图片
#cv2.namedWindow('test_img', cv2.WINDOW_NORMAL)
# cv2.imshow('test_img', img)
#plt 显示rgb
# plt.imshow(img)
# plt.show()
# k = cv2.waitKey(0)
# cv2.destroyAllWindows()
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('cat111.jpg', img)
#     cv2.destroyAllWindows()

#Drawing Functions in OpenCV
#img = np.zeros((512, 512, 3), np.uint8)
# cv2.line(img, (0, 0), (511, 511), (0, 255, 0), 10)
# cv2.rectangle(img, (0, 0), (300, 300), (255, 0, 0), 5)
# cv2.circle(img, (250, 250), 50, (0, 0, 255))
# cv2.ellipse(img, (250, 250), (100, 50), 0, 0, 360, 255)
#画多边形时不能用np.uint8,只能是int32
# pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# #print(pts)
# pts = pts.reshape((-1, 1, 2))
# #print(pts)
# cv2.polylines(img, [pts], True, (0, 255, 255))
# font = cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 3, lineType=cv2.LINE_AA)
# cv2.imshow('black', img)
# cv2.waitKey(0)

#Mouse as a Paint-Brush
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
# def draw_circle(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img, (x, y), 100, 255, -1)
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('draw_circle')
# cv2.setMouseCallback('draw_circle', draw_circle)
# while True:
#     cv2.imshow('draw_circle', img)
#     if cv2.waitKey(20) == 27:
#         break
# cv2.destroyAllWindows()

# drawing = False # true if mouse is pressed
# mode = True # if True, draw rectangle. Press 'm' to toggle to curve
# ix,iy = -1,-1
#
# # mouse callback function
# def draw_circle(event,x,y,flags,param):
#     global ix,iy,drawing,mode
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix,iy = x,y
#
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing == True:
#             if mode == True:
#                 cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#             else:
#                 cv2.circle(img,(x,y),5,(0,0,255),-1)
#
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         # if mode == True:
#         #     cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#         # else:
#         #     cv2.circle(img,(x,y),5,(0,0,255),-1)
# img = np.zeros((512,512,3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)
#
# while True:
#     cv2.imshow('image',img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == 27:
#         break
#
# cv2.destroyAllWindows()

#Trackbar as the Color Palette
# def nothing(x):
#     pass
# img = np.zeros((300, 512,3), np.uint8)
# cv2.namedWindow('image')
# cv2.createTrackbar('R', 'image', 0, 255, nothing)
# cv2.createTrackbar('G', 'image', 0, 255, nothing)
# cv2.createTrackbar('B', 'image', 0, 255, nothing)
# switch = '0:OFF' \
#          '1:ON'
# cv2.createTrackbar(switch, 'image', 0, 1, nothing)
# while True:
#     cv2.imshow('image', img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#     r = cv2.getTrackbarPos('R', 'image')
#     g = cv2.getTrackbarPos('G', 'image')
#     b = cv2.getTrackbarPos('B', 'image')
#     s = cv2.getTrackbarPos(switch, 'image')
#     if s == 0:
#         img[:] = 0
#     else:
#         img[:] = [b, g, r]
# cv2.destroyAllWindows()

#Basic Operations on Images
img = cv2.imread('cat1.png')

#Accessing and Modifying pixel values
# px = img[100, 100]
# print(px)
# green = img[100, 100, 1]
# print(green)
#item不可以直接获得3个通道的值，
#只能获得一个通道的值
#print(img.item(100, 100))
# print(img.item(100, 100, 2))
# img.itemset((100, 100, 2), 88)
# print(img.item(100, 100, 2))

#Accessing Image Properties
# print(img.shape)
# #size三个通道的值都计算到一起
# print(img.size)
# print(img.dtype)

#ImageROI
#矩阵先行后列，对应先y后x
# eye = img[10:190, 150:330]
# img[0:180, 0:180] = eye

#Splitting and Merging Image Channels
#split消耗时间长
# b, g, r = cv2.split(img)
# img = cv2.merge((b, g, r))
# b = img[:, :, 0]
# print(b)
# b1 = img[:, 0, 0]
# print(b1)

#Marking Borders for Images(Padding)
# blue = [255, 255, 255]
# constant = cv2.copyMakeBorder(img, 20,
#                               20, 20, 20, cv2.BORDER_CONSTANT,
#                               value=blue)

#Arithmetic Operations on Images
#Image Addtion
# x = np.uint8([250])
# y = np.uint8([10])
# #260变成255
# print(cv2.add(x,y))
# #260%256=4
# print(x + y)

#Image Blending(两张图片形状一样，水印等等)
# img1 = cv2.imread('cat.png')
# dst = cv2.addWeighted(img, 0.7, img1, 0.3, 0)
# cv2.imshow('addweight', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Bitwise Operations（处理不规则形状）
# img1 = cv2.imread('opencv.jpg')
# rows, cols, channels = img1.shape
# # print(img.shape, img.shape)
# # print(img.dtype, img.dtype)
# roi = img[0:rows-50, 0:cols-50]
# print(img1)
# img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# print(img1gray)
# ret, mask = cv2.threshold(img1gray, 10, 255, cv2.THRESH_BINARY)
# print(ret)
# print(mask)
# mask_inv = cv2.bitwise_not(mask)
#
# # Now black-out the area of logo in ROI
# img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
#
# # Take only region of logo from logo image.
# img2_fg = cv2.bitwise_and(img1,img1,mask = mask)
#
# # Put logo in ROI and modify the main image
# dst = cv2.add(img1_bg,img2_fg)
# img1[0:rows, 0:cols ] = dst
#
# cv2.imshow('res',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
img1 = cv2.imread('jiantou.jpg')
#print(img1[150:200, 150:200])
rows,cols,channels = img1.shape
roi = img[0:rows, 0:cols]
img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


ret, mask = cv2.threshold(img2gray, 230, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
img1_fg = cv2.bitwise_and(img1, img1, mask=mask)
img2_fg = cv2.bitwise_and(roi,roi,mask = mask_inv)
dst = cv2.add(img1_fg,img2_fg)
img1[0:rows, 0:cols ] = dst










cv2.imshow('cat', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()



