import cv2
import numpy as np
from hand_detector.detector import YOLO

hand_detector_model = YOLO(weights = 'weights/yolo.h5', threshold = 0.8)

camera = cv2.VideoCapture(1)

while True:
    ret, image = camera.read()
    if ret is False:
        break
    
    left_coordinate, right_coordinate = hand_detector_model.detect(image)
    if left_coordinate and right_coordinate is not None:
        image = cv2.rectangle(image, (left_coordinate[0], left_coordinate[1]), (right_coordinate[0], right_coordinate[1]), (255,255,255), 3)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

    # display image
    cv2.imshow('Hand Detection', image)

camera.release()
cv2.destroyAllWindows()
