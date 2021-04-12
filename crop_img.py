import cv2
import math
import numpy as np


def main():
    img = cv2.imread("basketballdude.png")
    crop_img = crop_around_bounding_box(img, 0, 0, 100, 100, 300, 300)
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)


def crop_around_bounding_box(to_crop, x, y, box_width, box_height, output_width, output_height):
    # calculate center of box
    center_x = math.ceil(x + box_width/2)
    center_y = math.ceil(y + box_height/2)
    # calculate edges
    # height stays the same
    start_y = math.floor(center_y - output_height / 2)
    end_y = math.floor(center_y + output_height / 2)

    start_x = math.floor(center_x - output_width / 2)
    end_x = math.floor(center_x + output_width / 2)
    # if around any edges, fill in w/ black
    if start_x < 0 or end_x > to_crop.shape[1] or start_y < 0 or end_y > to_crop.shape[0]:
        pad_left_x = 0 - start_x 
        if(pad_left_x < 0):
            pad_left_x = 0
        pad_right_x = end_x - to_crop.shape[1]
        if(pad_right_x < 0):
            pad_right_x = 0
        pad_left_y = 0 - start_y
        if(pad_left_y < 0):
            pad_left_y = 0
        pad_right_y = end_y - to_crop.shape[0]
        if(pad_right_y < 0):
            pad_right_y = 0
        
        padded = np.pad(to_crop, ((pad_left_y,pad_right_y),(pad_left_x, pad_right_x), (0,0)))
        return padded[start_y + pad_left_y:end_y + pad_left_y, start_x + pad_left_x:end_x + pad_left_x]





    return to_crop[start_y:end_y, start_x:end_x]
    

if __name__ == '__main__':
    main()
