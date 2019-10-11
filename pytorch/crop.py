# -*- coding: UTF-8 -*- 
import sys,os
import numpy as np
import struct
from PIL import Image, ImageEnhance, ImageDraw

import cv2, shutil

def checkvalidate(bbox, w = 100000, h = 100000):
    bbox = list(map(int, bbox))
    if not bbox[0] < bbox[2]:
        print(bbox, 'bbox[0] < bbox[2]')
        return 1
    if not bbox[1] < bbox[7]:
        print(bbox, 'bbox[1] < bbox[7]')
        return 1
    if not bbox[3] < bbox[5]:
        print(bbox, 'bbox[3] < bbox[5]')
        return 1
    if not bbox[4] > bbox[6]:
        print(bbox, 'bbox[4] < bbox[6]')
        return 1
    if not bbox[0] >= 0:
        print(bbox, 'bbox[0] >= 0')
        return 1
    if not bbox[1] >= 0:
        print(bbox, 'bbox[1] >= 0')
        return 1
    if not bbox[6] >= 0:
        print(bbox, 'bbox[6] >= 0')
        return 1
    if not bbox[3] >= 0:
        print(bbox, 'bbox[3] >= 0')
        return 1
    if not bbox[2] <= w:
        print(bbox, 'not bbox[2] <= w')
        return 1
    if not bbox[4] <= w:
        print(bbox, 'not bbox[4] <= w')
        return 1
    if not bbox[5] <= h:
        print(bbox, 'not bbox[5] <= h')
        return 1
    if not bbox[7] <= h:
        print(bbox, 'not bbox[7] <= h')
        return 1
    return 0

def crop(typename):
    setwidth = 600

    filelist = os.listdir(typename+"_label")
    filelist.sort()
    for filename in filelist:
        if filename == '.DS_Store':
            continue
        print(typename+"_label/"+filename)
        f = open(typename+"_label/"+filename, "r").read()
        locs = list(map(float,f.split()))
        # print loc
        im = cv2.imread(typename+'/'+filename[:-4])

        pts1 = np.float32([[locs[0], locs[1]], [locs[2], locs[3]], [locs[4], locs[5]], [locs[6], locs[7]]])
        # im = Image.open(typename+'/'+filename[:-4])
        h,w,c = im.shape
        if checkvalidate(locs, w, h):
            print(typename+'/'+filename[:-4])
            
            

            # print w,h
            # print np.array(locs)
            # shutil.move(typename+'/'+filename[:-4], 'new/'+filename[:-4])
            # shutil.move(typename+"_label/"+filename, 'new/'+filename)
            # cv2.polylines(im, [np.array([[w-locs[4], h-locs[5]], [w-locs[6], h-locs[7]], [w-locs[0], h-locs[1]], [w-locs[2], h-locs[3]]], np.int32)],True,(0,255,255),3)
            # cv2.polylines(im, [np.array([[locs[0], locs[1]], [locs[2], locs[3]], [locs[4], locs[5]], [locs[6], locs[7]]], np.int32)],True,(0,255,255),3)
            
            # im = cv2.resize(im, (500,500))
            # cv2.imshow(filename[:-4], im)
            # break
        # continue
        # pts2 = np.float32([[0,0],[512,0],[512,512],[0,512]])
        # M = cv2.getPerspectiveTransform(pts1,pts2)
        # res = cv2.warpPerspective(im,M,(512,512))
        pts2 = np.float32([[0,0],[800,0],[800,500],[0,500]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        res = cv2.warpPerspective(im,M,(800,500))
        cv2.imwrite('crop/'+filename[:-4],res)
        # break
        # break



# filelist = os.listdir('crop')

# for filename in filelist:
#     try:
#         print filename
#     # if 1:
#         # shutil.move('MTPHKnew_face/'+filename, 'new/')
#         # shutil.move('MTPHKnew_face_label/'+filename+'.txt', 'new/')

#         shutil.move('hk_face0/'+filename, 'hk_face/')
#         shutil.move('hk_face_label0/'+filename+'.txt', 'hk_face_label/')
#     except:
#         pass

{"requests": [{"image": {"content": "/9j/7QBEUGhvdG9zaG9...base64-encoded-image-content...fXNWzvDEeYxxxzj/Coa6Bax//Z"},"features": [{"type": "TEXT_DETECTION"}]}]}


# crop('hk_face')
# crop('MTPHKold_face')
crop('jiuzheng')
# crop('laissez_passer_face')
# crop('MTPTW_face')
# crop('MTPTW_back')
# crop('driver_back')
# crop('driver_face')
# crop('vehile_back')
# crop('vehile_face')
# crop('dana_driver_license')
# crop('dana_driver_license_back')
# crop('mac_idcardnew_back')
# crop('ktp')
# crop('new')
# crop('mynt_umid_right_face')
# crop('mynt_umid_right0_back')
# # crop('mynt_umid_right1_back')
# crop('mynt_umid_left_face')
# crop('mynt_umid_left_back')
# crop('mynt_tin_face')


# cv2.waitKey(1000000)

