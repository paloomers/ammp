import numpy as np 
import cv2
import time
import imutils # pip install imutils

import crop_img

x_0 = 900
y_0 = 500

# just flips a video for testing right now
def process_frame(frame):
    return cv2.flip(frame,0)

# when clicking a point on the screen, set it to be the tracked point
# i should add a boolean to make sure this is during being clicked later
def select_point(event, x, y, flags, params):
    global x_0, y_0
    if event == cv2.EVENT_LBUTTONDOWN:
        x_0 = x
        y_0 = y
        # cv2.circle(frame, point, 5, (0, 0, 255), 2)
        cv2.destroyWindow('point_selector')



# Plays input video, creates and saves new video
def process_video(INPUT, OUTPUT, output_scale):
    global x_0, y_0

    cap = cv2.VideoCapture(INPUT)

    if(cap.isOpened() == False):
        print("Error opening video")
    
    print("Processing Video and Creating Output")

    input_width = int(cap.get(3))
    input_height = int(cap.get(4))
    frame_rate = cap.get(5)
    
    output_width = int(input_width * output_scale)
    output_height = int(input_height * output_scale)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    out = cv2.VideoWriter(OUTPUT,fourcc,frame_rate, (output_width,output_height))

    # config for opencv optical flow
    lk_params = dict(winSize=(15,15), maxLevel=4, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    
    # starting coords TODO: replace w/ click on video

    i = 0
    ret, prev_frame = cap.read()

    # show the first frame
    cv2.namedWindow('point_selector')
    cv2.setMouseCallback('point_selector', select_point)
    cv2.imshow('point_selector', prev_frame)
    key = cv2.waitKey(10000) #change to your own waiting time 1000 = 1 second 


    old_coords = np.array([[x_0, y_0]], dtype=np.float32)

    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    while(cap.isOpened()):
        # TODO: display first frame and ask user to pick a point

        ret, frame = cap.read()
        gray_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
        
        if ret==True:

            new_points, status, error = cv2.calcOpticalFlowPyrLK(prev_gray, gray_frame, old_coords, None, **lk_params)
            x_0, y_0 = new_points.ravel()
            old_coords = new_points

            # Processes a new frame for the output video
            # new_frame = process_frame(frame)
            new_frame = crop_img.crop_around_point(
                frame, x_0, y_0,output_width,output_height
            )

            # TODO: draw a dot on the point being tracked
            cv2.circle(frame, (x_0, y_0), 5, (0, 255, 0), -1)
                
            # write the new frame
            out.write(new_frame)

            prev_frame = frame
            prev_gray = gray_frame

            # Display tracking info frame
            cv2.namedWindow('tracking', cv2.WINDOW_NORMAL)
            cv2.imshow('tracking', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                # May add a separate key for starting real-time video capture
                print("Exited using 'q'")
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Plays Video File
def play_video(FILENAME):
    cap = cv2.VideoCapture(FILENAME)
    if(cap.isOpened() == False):
        print("Error opening output video")
    
    print("Playing " + FILENAME)
    frame_rate = cap.get(5)

    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret == False:
            break

        # Display frame
        cv2.namedWindow(FILENAME, cv2.WINDOW_NORMAL)
        cv2.imshow(FILENAME, frame)
            
        if cv2.waitKey(10) & 0xFF == ord('q'):
            print("Exited using 'q'")
            break

    # Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()