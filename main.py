import argparse
import os
from skimage import io
import numpy as np

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
    args = parse_args()

    imagePath = args.video
    casPath = "haarcascade_frontalface_default.xml"


    faces = code.video_facial_recognition(args.video, args.cascade)



if __name__ == '__main__':
    main()
