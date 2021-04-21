from scipy import signal
import numpy as np
import cv2
from skimage import filters
from matplotlib import pyplot as plt
from PIL import Image
from pylab import *
import random

# Pass in old and new frame (both gray) and x and y coordinate of point to optical flow on, odd single integer for window size
def my_optical_flow(old_frame,new_frame,row,col,window_size):
    # Written for 1 point not multiple

    # Optionally blur images for better estimation
    k =  3 # gauss kernel size
    image_1 = cv2.GaussianBlur(old_frame.copy(),(k,k),0)
    image_2 = cv2.GaussianBlur(new_frame.copy(),(k,k),0)

    row = int(np.rint(row))
    col = int(np.rint(col))

    # kernel_x = np.array([[-1., 1.], [-1., 1.]])
    # kernel_y = np.array([[-1., -1.], [1., 1.]])
    # kernel_t = np.array([[1., 1.], [1., 1.]])
    kernel_x = np.array([[-1., 1.], [-1., 1.]]) * 0.25
    kernel_y = np.array([[-1., -1.], [1., 1.]]) * 0.25
    kernel_t = np.array([[1., 1.], [1., 1.]]) * 0.25
    
    # Optionally normalize pixels
    # image_1 = image_1 / 255.
    # image_2 = image_2 / 255.

    # Calculate I_x, I_y, I_t
    mode = 'same'
    fx = signal.convolve2d(image_1, kernel_x, mode=mode)
    fy = signal.convolve2d(image_1, kernel_y, mode=mode)
    ft = np.add(
        signal.convolve2d(image_2, kernel_t, mode=mode),
        signal.convolve2d(image_1, (-1 * kernel_t), mode=mode)
    )  
    
    # window_size is odd, all the pixels with offset in between [-w, w] are inside the window
    w = int(window_size/2)

    # Finding values within window
    Ix = fx[row-w:row+w+1, col-w:col+w+1].flatten()
    Iy = fy[row-w:row+w+1, col-w:col+w+1].flatten()
    It = ft[row-w:row+w+1, col-w:col+w+1].flatten()

    A_T = np.array((Ix,Iy))
    A = np.transpose(A_T)
    b = np.expand_dims(np.array(It),axis=1)

    u,v = np.linalg.pinv(A_T @ A) @ (A_T @ b)

    # Use optical flow comps (u,v) to calc new points + returns 1x2 array
    return np.float32(np.array([[row+v,col+u]]))


def main():

    # CODE TO SHOW OPTICAL FLOW DIAGRAMS FOR 2 FRAMES
    w = 7 # Window size
    Image1 = Image.open('basketball1.png').convert('L')
    Image2 = Image.open('basketball2.png').convert('L')

    Image1 = np.array(Image1)
    Image2 = np.array(Image2)

    # finding the good features
    features = cv2.goodFeaturesToTrack(Image1,100,0.01,5)	
    features = np.int0(features)

    c = "r" # color for plot

    plt.subplot(1,2,1) # Plot 1 for open cv implementation
    plt.title("Optical Flow Vectors (OpenCV)")
    plt.imshow(Image1,cmap = cm.gray)

    # Parameters for lucas kanade optical flow
    lk_params = dict( winSize  = (w,w), maxLevel = 0, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    for f in features:
        # Compute flow
        feature = np.float32(np.expand_dims(f,axis=0))
        new_p, st, er = cv2.calcOpticalFlowPyrLK(Image1, Image2, feature, None, **lk_params)
        
        new_row, new_col = new_p.ravel()

        u = new_col - f[0,1] # dx, change in col
        v = new_row - f[0,0] # dy, change in row

        # Plot Arrow
        plt.arrow(f[0,0],f[0,1],u,v,head_width =5, head_length =5, color = c)

    plt.subplot(1,2,2) # Plot 2 for open cv implementation
    plt.title("Optical Flow Vectors (Our implementation)")
    plt.imshow(Image1,cmap = cm.gray)

    for f in features:        
        row = f[0,0]
        col = f[0,1]

        new_p = my_optical_flow(Image1,Image2,row,col,w)
        new_row, new_col = new_p.ravel()

        u = new_col - col # dx, change in col
        v = new_row - row # dy, change in row

        # Plot Arrow
        plt.arrow(row,col,u,v,head_width =5, head_length =5, color = c)

    plt.show()


if __name__ == '__main__':
    main()