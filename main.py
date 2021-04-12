import argparse
import os
from skimage import io
import numpy as np

import stabilize
import code


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


def main():
    # args = parse_args()
    # imagePath = args.video
    casPath = "haarcascade_frontalface_default.xml"
    # faces = code.video_facial_recognition(args.video, args.cascade)

    INPUT_FILE_NAME = "./videos/bball-dribble.mp4"
    OUTPUT_FILE_NAME = "output.avi"
    # Scale for size of output video relative to input video
    output_scale = 0.75

    # TODO: Handle webcam w different function that records and saves as a file, can also use keys to start and stop
    
    # Plays Input Video
    stabilize.play_video(INPUT_FILE_NAME)
    # Processes Video, and Generates Output Video
    stabilize.process_video(INPUT_FILE_NAME,OUTPUT_FILE_NAME,casPath,output_scale)
    # Plays Output Video
    stabilize.play_video(OUTPUT_FILE_NAME)

if __name__ == '__main__':
    main()