import cv2
import numpy as np


def get_max_blob(bin_image, thre=0):
    """
        find max len contours blob in bin_image, paint on a new image
        Args:
            bin_image: binary image for picking blob
        Returns:
            max_contour: the max len contour point array
    """
    _, bin_img = cv2.threshold(bin_image, thre, 255, cv2.THRESH_BINARY)
    contours = cv2.findContours(bin_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    max_len = 0
    max_contour = np.array([])
    for contour in contours[1]:
        if len(contour) > max_len:
            max_len = len(contour)
            max_contour = contour

    return max_contour

def crop_image_roi(image, roi):
    """
    :param image: 1-channel image
    :param roi: in x,y,w,h
    :return: croped image
    """
    return image[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]]