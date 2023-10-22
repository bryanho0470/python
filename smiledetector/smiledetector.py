import cv2

face_detector = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

webcam = cv2.VideoCapture(0)


while True:
    successful_frame_read, frame = webcam.read()

    if not successful_frame_read:
        break

    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(grayscaled_frame)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        the_face = frame[y:y+h, x:x+w]
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

        smiles = smile_detector.detectMultiScale(
            face_grayscale, scaleFactor=2.0, minNeighbors=40)

        if len(smiles) > 0:
            cv2.putText(frame, 'smiling', (x, y+h+40), fontScale=3,
                        fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))

        # for (x_, y_, w_, h_) in smiles:
        #     cv2.rectangle(the_face, (x_, y_), (x_+w_, y_+h_), (0, 255, 255), 3)

    cv2.imshow("Good smile", frame)

    key = cv2.waitKey(1)

    if key == 13 or key == 113:
        break

webcam.release()
