import cv2
import sys
import logging as log
import datetime as dt
from time import sleep

#Take arguments from the command line
def facial_recognition(imageP, cascP):
    faceCascade = cv2.CascadeClassifier(cascP)

# Read the image
    image = cv2.imread(imageP)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print("Found " + str(len(faces))+ " faces!")

    # #Draw a rectangle around the faces
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # cv2.imshow("Faces found", image)
    # cv2.waitKey(0)

    return faces

def video_facial_recognition(videoP, cascP):
    faceCascade = cv2.CascadeClassifier(cascP)

    video_capture = cv2.VideoCapture(int(videoP))

    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass

    # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

    # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
        cv2.imshow('Video', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Display the resulting frame
        cv2.imshow('Video', frame)

# When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

    return faces

