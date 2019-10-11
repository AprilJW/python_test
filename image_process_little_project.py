#-*-coding: UTF-8 -*-
import cv2

def selectLedZone(img_rgb,flag):
    '''
    function: 选出led显示区域
    参数：
        img_rgb是输入的原图
        flag 是进行交通检测时使用,如果为0表示的交通灯，其他都为1
    返回：
        led区域的roi图片
    '''
    print(img_rgb<255)
    the1 = cv2.adaptiveThreshold(img_rgb, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,5,10)
    # hsv = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2HSV)
    # h,s,v = cv2.split(hsv)
    # v_bin = binImg(v) # 二值化
    cv2.imshow('h', the1)
    cv2.waitKey(0)
    #_, v_bin = cv2.threshold(v, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # if flag==1:
    #     v_bin = cv2.dilate(v_bin,None,iterations=2) #膨胀操作
    # else:
    #     v_bin = ~cv2.dilate(v_bin,None,iterations=2) #膨胀操作
    #     # 得到二值图的轮廓
    #_, cnts, h = cv2.findContours(v_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.imshow('h', v_bin)
    # cv2.waitKey(0)


    #print('cnts: ', len(cnts), cnts[0])
    # # print(h)
    # cs = sorted(cnts, key=cv2.contourArea, reverse=True)[:6]
    # # print('cs:', cs)
    # result = []
    # for ind, c in enumerate(cs):
    #     rect = cv2.minAreaRect(c)
    #     peri = cv2.arcLength(c, True)
    #     approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    #     length = len(approx)
    #     print(length)
    #     x, y, w, h = cv2.boundingRect(c)
    #     if length == 4 and w > h:
    #         src_img_rot = img_rgb[y:y + h, x:x + w]
    #         result.append(src_img_rot)
    #     if len(result) != 0:
    #         cv2.imshow('h', result[0])
    #         cv2.waitKey(0)
    #         return result[0]
    #     else:
    #         return "noL"
img = cv2.imread(r'/Users/jw/PycharmProjects/python_test/car.jpg', 0)

#img = cv2.imread(r'/Users/jw/PycharmProjects/python_test/lvsejiantou.jpg', 0)

#img = cv2.imread(r'/Users/jw/PycharmProjects/python_test/yansetuban.jpg', 0)
# print(img.shape)
#
# selectLedZone(img, 1)
#cv2.imwrite('yansetuban.jpg', img)
import numpy as np
# a = np.array([[1,2,3],
#      [0,0,0],
#      [4,5,6]])
# d = np.array([1,2,3])
# #print(type(a))
# b = a[np.where(a<1)]
# #print(a[np.where(a<1)])
# m_0 = np.mean(b) if len(b)>0 else 0
# print(m_0, type(m_0))
# print('len(d):', len(d))
"""
#池化
import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg")

# Average Pooling
out = img.copy()

H, W, C = img.shape
G = 8
Nh = int(H / G)
Nw = int(W / G)

for y in range(Nh):
    for x in range(Nw):
        for c in range(C):
            out[G*y:G*(y+1), G*x:G*(x+1), c] = np.mean(out[G*y:G*(y+1), G*x:G*(x+1), c]).astype(np.int)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
# import cv2
# # import numpy as np
# # a = cv2.imread(r'/Users/jw/PycharmProjects/python_test/car.jpg')
# # h, w, c = a.shape
# # #print(h,w,c)
# # g = 8
# # nh = int(h/g)
# # nw = int(w/g)
# # for i in range(nh):
# #     for j in range(nw):
# #         for k in range(c):
# #             #a[i*g:(i+1)*g, j*g:(j+1)*g, k] = np.mean(a[i*g:(i+1)*g, j*g:(j+1)*g, k])
# #             a[i * g:(i + 1) * g, j * g:(j + 1) * g, k] = np.max(a[i * g:(i + 1) * g, j * g:(j + 1) * g, k])
# # print(a.shape)
# # cv2.imshow('test_mean_pooling', a)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# import cv2
# import numpy as np
# 高斯滤波
# # Read image
# img = cv2.imread(r'/Users/jw/PycharmProjects/python_test/lvsejiantou.jpg')
# H, W, C = img.shape
#
# # Gaussian Filter
# K_size = 3
# sigma = 1.3
# #
# # ## Zero padding
# pad = K_size // 2
# # out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float)
# # out[pad:pad + H, pad:pad + W] = img.copy().astype(np.float)
# #
# ## Kernel
# K = np.zeros((K_size, K_size), dtype=np.float)
# for x in range(-pad, -pad + K_size):
#
#     for y in range(-pad, -pad + K_size):
#         K[y + pad, x + pad] = np.exp(-(x ** 2 + y ** 2) / (2 * (sigma ** 2)))
# # print(K.shape)
# K /= (sigma * np.sqrt(2 * np.pi))
# # print('k2:', K.shape)
# K /= K.sum()
# print('k3', K.shape)
# print('K.sum()', K.sum())
#print(K)
#
# tmp = out.copy()
#
# for y in range(H):
#     for x in range(W):
#         for c in range(C):
#             out[pad + y, pad + x, c] = np.sum(K * tmp[y:y + K_size, x:x + K_size, c])
#
# out = out[pad:pad + H, pad:pad + W].astype(np.uint8)
#
# # Save result
# #cv2.imwrite("out.jpg", out)
# #cv2.imshow("result", out)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread(r'/Users/jw/PycharmProjects/python_test/lvsejiantou.jpg')
# #cv2.imshow('org_img', img)
# # print('img.shape:', img.shape)
# h, w, c = img.shape
# pad = 2
# zeros = np.zeros([h+2*pad, w+2*pad, 3], dtype=np.float)
# print('img.shape:', zeros.shape)
# pad_zero = zeros.copy()
# pad_zero[pad:pad+h, pad:pad+w] = img.copy()
# #print(zeros)
# # cv2.imshow('zeros', zeros)
# # cv2.imshow('pad', pad_zero)
#
# K = np.zeros((3,3), dtype=np.float)
# ksize = 3
# sigma = 1.3
# for x in range(ksize):
#     for y in range(ksize):
#         K[x:y] = np.exp(-(x**2 + y**2)/2*(sigma**2))
# K /= (sigma*np.sqrt(2*np.pi))
# K /= np.sum(K)
# print(np.sum(K))
# print(K)
# for i in range(h):
#     for j in range(w):
#         for h in range(c):
#             pad_zero[pad+i, pad+j, h] = np.sum(K*pad_zero[i: i+ksize, j: j+ksize, h])
#
# pad_zero = pad_zero[pad:pad+h, pad:pad+w]
# print('gaosi_shape', pad_zero.shape)
# cv2.imshow('gaosi', pad_zero)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#中值滤波
import cv2
import numpy as np

# Read image
# img = cv2.imread("imori_noise.jpg")
img = cv2.imread(r'/Users/jw/PycharmProjects/python_test/lvsejiantou.jpg')
H, W, C = img.shape


# Median Filter
K_size = 3

## Zero padding
pad = K_size // 2
out = np.zeros((H + pad*2, W + pad*2, C), dtype=np.float)
out[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)

tmp = out.copy()

for y in range(H):
    for x in range(W):
        for c in range(C):
            out[pad+y, pad+x, c] = np.median(tmp[y:y+K_size, x:x+K_size, c])

out = out[pad:pad+H, pad:pad+W].astype(np.uint8)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()


