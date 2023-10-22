import cv2

#our image
# img_file = 'car.jpeg'
webcam = cv2.VideoCapture('C0013.MP4')

# create opencv image
#img = cv2.imread(video)

#create car classifier
car_tracker = cv2.CascadeClassifier('cars.xml')
pedestrian_tracker = cv2.CascadeClassifier('haarcascade_fullbody.xml')

  
while True:
  # read just single frame
  read_successful, frame = webcam.read();

  #safe coding
  if read_successful:
    #Must convert to grayscale
    # convert to grayscale (needed for haar cascade)
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  else:
    break

  # detect cars
  cars = car_tracker.detectMultiScale(grayscale_frame)
  pedestrians = pedestrian_tracker.detectMultiScale(grayscale_frame)

  #draw rectangles around the car
  for (x,y,w,h) in pedestrians:
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

  #draw rectangles around the car
  for (x,y,w,h) in cars:
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
    
  #Display the image with the faces spotted
  cv2.imshow('Clever Programmer Car Detector', frame)
  
  key = cv2.waitKey(1)
  
  if key == 13 or key == 113:
    break

webcam.release()