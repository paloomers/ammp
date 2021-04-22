# AMMP Final Project README



## Running Code

To run our project run python main.py from the appropriate directory.

For our project, we have implemented locked-on object stabilization using two approaches. To use the "optical flow" based approach, uncomment the line in main.py that says method = "optical". To use the detection based approach with a cascade classifier, uncomment the line in main that says method="cascade"

INPUT_FILE_NAME and OUTPUT_FILE_NAME both represent the name and directory of the respective input and output files for the program. Using an integer string for INPUT_FILE_NAME uses a camera input to your computer (use "0" for your webcam). 

Note: If using a camera input, press "s" to start recording your video. The video is recorded by default for 3 seconds, but can be changed in record_video().

output_scale is a hyper-paramter for the scale of your output video relative to the scale of the input video. Lower ratios produce lower resolution videos, but tend to have less black boxes around the final output.

### Optical flow

What happens when you run:

After running the code to do optical flow, the video you ran as input will display first. You can press q to quit if you do not want to watch. From there, the first frame of the video will display. You have 10 seconds to click on a point to track/crop around before the code just picks a random point to track. This is because openCV click inputs are weird :(. After you click, the window will disappear until the 10 seconds have ended. Then, a window will display showing the point being tracked from frame to frame. If you press q, the code will stop tracking it. After the point being tracked ends, the video cropped around the tracked point will play and be written to output.py. 

To switch between OpenCV optical flow implementaton and our implementation, go to optical.py and uncomment the respective line that stores the points inside the variable new_points.

The window size hyper-parameter for the local window of points that is used to estimate optical flow can also be found in optical.py in the variable window_size for our implementation, and lk_params for for OpenCV's implementation.

### Haar Cascade

What happens when you run:

To run the stabilization with the AirPod cascade, in main.py uncomment the line that says method="cascade" and change the variable, cascPath, to be the relative path of the file, "cascadecopycopy.xml". Make sure INPUT_FILE_NAME = "0". Run main.py. From there, a window should display and click "s" to start recording. The video cropped around the object will play and be written to output.py

To test the cascade without stabilization, cd into the gatheringCascade folder and run test.py. This will use web cam footage as the video input which the cascade will be applied to. Boxes should encase the recognized AirPod.

## Some Results
Our other result gifs were too big to upload to github (but can be observed in our presentation recording!)

### Optical Flow
The OpenCV optical flow vector outputs compared to our optical flow function outputs 

<img src='https://github.com/paloomers/ammp/blob/main/Figure_1.png' title='Optical Flow results compared to OpenCV' width='' alt='Video Walkthrough' />

### AirPod Haar Cascade of Classifiers

Our AirPod cascade being used on a webcam clip

<img src='https://github.com/paloomers/ammp/blob/main/shortclipAIrpod.gif' title='clip of our airpod cascade working' width='' alt='Video Walkthrough' />
