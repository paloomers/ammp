# AMMP Final Project README

tbd python main.py --video 0 --cascade haarcascade_frontalface_default.xml

## Running Code

### Optical flow

TODO: someone write how we're running it (i.e. uncommenting the line in main??)

What happens when you run:

After running the code to do optical flow, the video you ran as input will display first. You can press q to quit if you do not want to watch. From there, the first frame of the video will display. You have 10 seconds to click on a point to track/crop around before the code just picks a random point to track. This is because openCV click inputs are weird :(. After you click, the window will disappear until the 10 seconds have ended. Then, a window will display showing the point being tracked from frame to frame. If you press q, the code will stop tracking it. After the point being tracked ends, the video cropped around the tracked point will play and be written to output.py. 


### Haar Cascade



## Some Results
Our other result gifs were too big to upload to github (but can be observed in our presentation recording!)

### Optical Flow
The OpenCV optical flow vector outputs compared to our optical flow function outputs 

<img src='https://github.com/paloomers/ammp/blob/main/Figure_1.png' title='Optical Flow results compared to OpenCV' width='' alt='Video Walkthrough' />

### AirPod Haar Cascade of Classifiers

Our AirPod cascade being used on a webcam clip

<img src='https://github.com/paloomers/ammp/blob/main/shortclipAIrpod.gif' title='clip of our airpod cascade working' width='' alt='Video Walkthrough' />
