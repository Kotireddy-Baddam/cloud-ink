import cv2
from own_hand_detector import HandDetector


detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)
import numpy as np

while True:
    _, img = video.read()
    hand = detector.findHands(img, draw=False)
    
    if hand:
        lmlist = hand[0]
        if lmlist:
            coords = lmlist['lmList']
            fingerup = detector.fingersUp(lmlist)
            
            for i in range(1,6):
                if fingerup[i-1] == 1:
                    img = cv2.circle(img, (coords[i*4][0],coords[i*4][1]), 6, (250,160,90), -2)
            
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
video.release()
cv2.destroyAllWindows()
