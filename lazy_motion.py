import cv2
import math
import numpy as np

def find_center(x, y, w, h):
    center_x = x + w/2
    center_y = y + h/2
    return center_x, center_y

# this is really janky and is probably gonna look bad
def calc_center_linear(prev_x, prev_y, latest_x, latest_y):
    x_diff = latest_x - prev_x
    y_diff = latest_y - prev_y
    predict_x = latest_x + x_diff
    predict_y = latest_y + y_diff
    return predict_x, predict_y

def top_left_from_center(center_x, center_y, w, h):
    x_top = center_x - math.floor(w/2)
    y_top = center_y - math.floor(h/2)
    return x_top, y_top, w, h