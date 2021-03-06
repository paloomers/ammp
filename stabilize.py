import numpy as np 
import cv2
import time
import imutils # pip install imutils

import crop_img

# just flips a video for testing right now
def process_frame(frame):
    return cv2.flip(frame,0)

# Plays input video, creates and saves new video
def process_video(INPUT, OUTPUT, casPath, output_scale):

    faceCascade = cv2.CascadeClassifier(casPath)
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
    
    # Ignore this (used to avoid errors if nothing found)
    x_1,y_1,w_1,h_1 = (100,100,input_width/4,input_height/4)

    i = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret==True:

            # FACE RECOGNITION CODE
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            # TODO: Deal w/ multiple faces found + no face found in current frame
            #if faces are detected:
            if(len(faces) != 0):
                #if this is the first frame or there's only one face, return the first face
                if(i==0 or len(faces) == 1):
                    x_1,y_1,w_1,h_1 = faces[0]
                    x_0, y_0 = x_1,y_1
                
                # otherwise return the face closest to the previous face
                else:
                    min_dist = 10000
                    for (x, y, w, h) in faces:
                        #calculates distance between previous face and current face
                        dist = np.linalg.norm(np.array((x ,y)) - np.array((x_0,y_0)))
                        #if min distance, saves this face
                        if(dist < min_dist):
                           x_1, y_1, w_1, h_1 =  x, y, w, h
                           min_dist = dist
            #saves current face as previous face
            x_0, y_0 = x_1, y_1
            i = 1

            
            # Processes a new frame for the output video
            # new_frame = process_frame(frame)
            new_frame = crop_img.crop_around_bounding_box(
                frame, x_1, y_1, w_1, h_1 ,output_width,output_height
            )

            # Draw a rectangle around the face
            cv2.rectangle(frame, (x_1, y_1), (x_1+w_1, y_1+h_1), (0, 255, 0), 2)
                
            # write the new frame
            out.write(new_frame)

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