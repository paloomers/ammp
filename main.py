import argparse
import os
from skimage import io
import numpy as np
import cv2

import stabilize
import code
import time

def parse_args():
    """ Perform command-line argument parsing. """

    parser = argparse.ArgumentParser(
        description="Project 6 Final Project!")
    parser.add_argument(
        '--video',
        required=True,
        help='Which video to use')
    parser.add_argument(
        '--cascade',
        required=True,
        help='Cascade used to find object')

    return parser.parse_args()

def record_video(cam_number):
    print("Recording Video From Camera")
    recorded_video_name = "./videos/recorded.avi"

    # video length in seconds
    video_length = 2

    cap = cv2.VideoCapture(cam_number)

    # Changing camera capture resolution from default
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

    cam_width = int(cap.get(3))
    cam_height = int(cap.get(4))
    frame_rate = cap.get(5)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    out = cv2.VideoWriter(recorded_video_name,fourcc,frame_rate,(cam_width,cam_height))

    video_started = False
    start_time = None

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:   

            cv2.namedWindow('camera-input', cv2.WINDOW_NORMAL)
            cv2.imshow('camera-input', frame)

            if (cv2.waitKey(1) & 0xFF == ord('s')) and (not video_started):
                print("Recording Started")
                video_started = True
                start_time = time.time()
            
            if(video_started):
                # write the frame
                out.write(frame)
                elapsed_time = time.time() - start_time
                if(elapsed_time > video_length):
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
    # faces = code.video_facial_recognition(args.video, args.cascade)

    # INPUT_FILE_NAME = "./videos/bball-dribble.mp4"
    INPUT_FILE_NAME = "0" # Use Integers for Camera (ex. Webcam)
    OUTPUT_FILE_NAME = "output.avi"
    # Scale for size of output video relative to input video
    output_scale = 0.6

    # Check if INPUT_FILE_NAME is int
    try:
        camera_number = int(INPUT_FILE_NAME)
        # Record Webcam Video
        # Press 's' to start recording
        INPUT_FILE_NAME = record_video(camera_number)
    except ValueError:
        INPUT_FILE_NAME = INPUT_FILE_NAME

    # Plays Input Video
    stabilize.play_video(INPUT_FILE_NAME)
    # Processes Video, and Generates Output Video
    stabilize.process_video(INPUT_FILE_NAME,OUTPUT_FILE_NAME,casPath,output_scale)
    # Plays Output Video
    stabilize.play_video(OUTPUT_FILE_NAME)

if __name__ == '__main__':
    main()