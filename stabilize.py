import numpy as np 
import cv2
import time
import imutils # pip install imutils

# TODO: 
# May use this to playback videos at the end after all is done:
# https://stackoverflow.com/questions/7227162/way-to-play-video-files-in-tkinter

# Not sure if video codec for writing/creating video also works on MAC right now

# Processes frame from orig video to create frame for new video
def process_frame(frame):
    # TODO: Centering Window Based on coords
    return cv2.flip(frame,0)

# Plays input video, creates and saves new video
def process_video(INPUT, OUTPUT):
    cap = cv2.VideoCapture(INPUT)
    if(cap.isOpened() == False):
        print("Error opening video")
    
    print("Playing Input Video, and Creating Output")

    input_width = int(cap.get(3))
    input_height = int(cap.get(4))
    frame_rate = cap.get(5)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    out = cv2.VideoWriter(OUTPUT,fourcc,frame_rate, (input_width,input_height))

    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret==True:
            # frame = imutils.resize(frame,height=640)

            new_frame = process_frame(frame)
            # write the flipped frame
            out.write(new_frame)

            # Display frame
            cv2.imshow('input-video',frame)

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

# Plays Output File
def play_output(OUTPUT):
    cap = cv2.VideoCapture(OUTPUT)
    if(cap.isOpened() == False):
        print("Error opening output video")
    
    print("Playing " + OUTPUT)
    frame_rate = cap.get(5)

    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret == False:
            break

        # Display frame
        cv2.imshow('output-video',frame)
            
        if cv2.waitKey(2) & 0xFF == ord('q'):
            print("Exited using 'q'")
            break

    # Release everything if job is finished
    cap.release()
    
    cv2.destroyAllWindows()

def main():
    # File Path for saved videos, Ints for camera index (0 for 1st camera)
    INPUT_FILE_NAME = "./videos/bball-dribble.mp4"
    # INPUT_FILE_NAME = 0 
    OUTPUT_FILE_NAME = "output.avi"
    
    process_video(INPUT_FILE_NAME,OUTPUT_FILE_NAME)
    play_output(OUTPUT_FILE_NAME)

if __name__ == '__main__':
    main()