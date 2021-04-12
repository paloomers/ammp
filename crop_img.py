import cv2
import math
import numpy as np

aspect_ratio = 4/3

def main():
    img = cv2.imread("basketballdude.png")
    crop_img = crop_around_bounding_box(img, 0, 0, 100, 100)
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)


def crop_around_bounding_box(to_crop, x, y, box_width, box_height):
    max_padding = math.floor(box_height * aspect_ratio / 2)
    # calculate center of box
    center_x = math.ceil(x + box_width/2)
    # center_y = y + box_height/2
    # calculate edges
    # height stays the same
    start_y = y
    end_y = y + box_height

    half_crop_width = math.ceil(box_height * aspect_ratio / 2)
    start_x = center_x - half_crop_width
    end_x = center_x + half_crop_width
    # if around any edges, fill in w/ black
    if start_x < 0 or end_x > to_crop.shape[1]:
        pad_left = 0 - start_x 
        if(pad_left < 0):
            pad_left = 0
        pad_right = end_x - to_crop.shape[1]
        if(pad_right < 0):
            pad_right = 0
        padded = np.pad(to_crop, ((0,0),(pad_left, pad_right), (0,0)))
        return padded[start_y:end_y, start_x + pad_left:end_x + pad_left]





    return to_crop[start_y:end_y, start_x:end_x]
    

if __name__ == '__main__':
    main()
