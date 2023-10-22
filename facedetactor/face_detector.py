import cv2
from random import randrange
# load some pre-trainted data on face frontals feom opencv (haar cascade algotirthm)
trained_face_data = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')

# choose an image to detect faces in
# img = cv2.imread('6.png')
webcam = cv2.VideoCapture(0)


# Iterate forever over frames
while True:

    # Read the current frame
    successful_frame_read, frame = webcam.read()

    # must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces every Scale of photo - making ractangle
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # display images
    cv2.imshow('Clever Programmer Face Detector', frame)

    # terminate program
    key = cv2.waitKey(1)

    # Stop if q key is pressed
    if key == 13 or key == 113:
        break

# clean up webcam data
webcam.release()

"""



print("Code completed")
"""
