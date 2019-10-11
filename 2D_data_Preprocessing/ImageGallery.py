import numpy as np
import cv2
import sys
import os
from src.Item2D import Item2D
from utils import util, img_process_util
from src.pascal_voc_io import PascalVocReader
from pathlib import Path
from collections import defaultdict

sys.path.append(os.path.abspath('../../../python_test/2D_data_Preprocessing/utils'))
sys.path.append(os.path.abspath('../../../python_test/2D_data_Preprocessing/src'))

class ImageGallery:
    def __init__(self):
        self.label_to_items = defaultdict(list)

    def _add_item_to_label_items(self, item2d):
        name = item2d.name
        self.label_to_items[name].append(item2d)


    def _load_item_from_points(self, image, points, label, roi=None):
        mask = np.zeros([image.shape[0], image.shape[1]], np.uint8)
        points = np.array(util.float_points_to_int(points))
        cv2.drawContours(mask, [points], 0, 255, cv2.FILLED)
        contour = img_process_util.get_max_blob(mask)
        if roi is None:
            item_roi = cv2.boundingRect(contour)
        else:
            item_roi = roi

        b, g, r = cv2.split(image)
        b_roi = img_process_util.crop_image_roi(b, item_roi)
        g_roi = img_process_util.crop_image_roi(g, item_roi)
        r_roi = img_process_util.crop_image_roi(r, item_roi)
        mask_roi = img_process_util.crop_image_roi(mask, item_roi)
        item_image = cv2.merge([b_roi, g_roi, r_roi, mask_roi])
        return Item2D(item_img=item_image, name=label), item_roi

    def _load_items_from_item(self, xmlFilePath):

        image = cv2.imread(str(Path(xmlFilePath).with_suffix('.jpg')))
        pascal_voc_reader = PascalVocReader(xmlFilePath)
        for name, lineWidth, vertex, *k in pascal_voc_reader.shapes:
            item2d, _ = self._load_item_from_points(image, util.tuple_points_to_list(vertex), name)
            self._add_item_to_label_items(item2d)


    def load_multi_items(self, seed_path):
        seed_path = Path(seed_path)
        xml_image_dir = os.listdir(seed_path)
        for i in xml_image_dir:
            file_path = seed_path / i
            #print(file_path.suffix)
            if file_path.suffix == '.xml':
                self._load_items_from_item(file_path)


if __name__ == '__main__':
    imageGallery = ImageGallery()
    imageGallery.load_multi_items('/Users/jw/Projects/0920test_2D/data')
    print(imageGallery.label_to_items)