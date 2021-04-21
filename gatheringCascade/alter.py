import os
import cv2
import numpy as np
from PIL import Image, ImageOps


def rename():
    printnum = 1
    for i in os.listdir('/Users/Paloma/Desktop/CV/ammp/gatheringCascade/neg'):
        print(printnum)
        print(i)
        os.rename('/Users/Paloma/Desktop/CV/ammp/gatheringCascade/neg/'+i, str(printnum)+".jpg")
        print(i)
        printnum += 1

    
def alter():
    os.chdir(r"/Users/Paloma/Desktop/CV/ammp/gatheringCascade/neg")
    for i in os.listdir('/Users/Paloma/Desktop/CV/ammp/gatheringCascade/neg'):
            print(i)
            im = Image.open(i)
            im = im.resize((100, 100), Image.ANTIALIAS)
            im = ImageOps.grayscale(im)
            im.save(i)

def create_pos_n_neg():
    for img in os.listdir('/Users/Paloma/Desktop/CV/ammp/gatheringCascade/neg'):
        print(img)
        line = 'neg'+'/'+img+'\n'
        with open('bg.txt','a') as f:
            f.write(line)

#rename()
#alter()
create_pos_n_neg()
