import argparse
import os
from skimage import io
import numpy as np
import cv2

import stabilize
import optical
import cascade
import code
import time

# def parse_args():
#     """ Perform command-line argument parsing. """

#     parser = argparse.ArgumentParser(
#         description="Project 6 Final Project!")
#     parser.add_argument(
#         '--video',
#         required=True,
#         lp='Which video to use')
#     parser.add_argument(
#         '--cascade',
#         required=True,
#         help='Cascade used to find object')

#     return parser.parse_args()

def record_video(cam_number):
    print("Recording Video From Camera")
    recorded_video_name = "./videos/recorded.mp4"

    # video length in seconds
    video_length = 3

    cap = cv2.VideoCapture(cam_number)

    # Changing camera capture resolution from default
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

    cam_width = int(cap.get(3))
    cam_height = int(cap.get(4))
    frame_rate = cap.get(5)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(recorded_video_name,fourcc,frame_rate,(cam_width,cam_height))

    video_started = False
    max_num_frames = video_length * int(frame_rate)
    num_frames_captured = 0

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:   

            cv2.namedWindow('camera-input', cv2.WINDOW_NORMAL)
            cv2.imshow('camera-input', frame)

            if (cv2.waitKey(1) & 0xFF == ord('s')) and (not video_started):
                print("Recording Started")
                video_started = True
            
            if(video_started):
                if (num_frames_captured < max_num_frames):
                    # write the frame
                    out.write(frame)
                    num_frames_captured += 1
                else:
                    break
        else:
            break


    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    return recorded_video_name

def main():
    # args = parse_args()
    # imagePath = args.video

    casPath = "haarcascade_frontalface_default.xml"
    # casPath = "./gatheringCascade/cascadecopy.xml"
    
    # INPUT_FILE_NAME = "./videos/v1-airpod.mp4"
    INPUT_FILE_NAME = "0" # Use Integers for Camera (ex. Webcam)
    
    OUTPUT_FILE_NAME = "output.avi"

    # Scale for size of output video relative to input video
    output_scale = 0.7

    # method = "optical"
    method = "cascade"

    # Check if INPUT_FILE_NAME is int
    try:
        camera_number = int(INPUT_FILE_NAME)
        # Record Webcam Video
        # Press 's' to start recording
        INPUT_FILE_NAME = record_video(camera_number)
    except ValueError:
        INPUT_FILE_NAME = INPUT_FILE_NAME

    if (method == "optical"):
        # Plays Input Video
        # optical.play_video(INPUT_FILE_NAME)
        # Processes Video, and Generates Output Video
        optical.process_video(INPUT_FILE_NAME,OUTPUT_FILE_NAME,output_scale)
        # Plays Output Video
        optical.play_video(OUTPUT_FILE_NAME)

    elif (method == "cascade"):
        # Plays Input Video
        cascade.play_video(INPUT_FILE_NAME)
        # Processes Video, and Generates Output Video
        cascade.process_video(INPUT_FILE_NAME,OUTPUT_FILE_NAME,casPath,output_scale)
        # Plays Output Video
        cascade.play_video(OUTPUT_FILE_NAME)
    else:
        print("method not supported")

    

if __name__ == '__main__':
    main()