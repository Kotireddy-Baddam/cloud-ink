import cv2
from own_hand_detector import HandDetector
import numpy as np

board = np.zeros((480,640,3),np.uint8)
detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)

video.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

state = "working"

values = np.array([0,0,0])

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if hand:
        lmlist = hand[0]
        coords = lmlist['lmList']
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 1, 0, 0, 0]:
                state = "write"
                board = cv2.circle(board, (coords[8][0],coords[8][1]),5, (250,160,90),-1)
            if fingerup == [0, 1, 1, 0, 0]:
                state = "erase"
                board = cv2.circle(board, (coords[8][0],coords[8][1]),5, (250,160,90),-1)
            if fingerup == [1, 1, 0, 0, 0]:
                state = "move"
                values = board[coords[8][0],coords[8][1],0]
                print(values)
                board = cv2.circle(board, (coords[8][0],coords[8][1]),5, (250,160,90),-1)
            if fingerup == [1, 1, 1, 1, 1]:
                state = "clean"
                board[:,:,:] = 0
            print(coords[8])
    
    cv2.imshow("Video", img)
    cv2.imshow("board",board)
    
    if state == "write":
        board = cv2.circle(board,(coords[8][0],coords[8][1]),5,(255,255,255),-1)
    if state == "erase":
        board = cv2.circle(board,(coords[8][0],coords[8][1]),5,(0,0,0),-1)
    if state == "move":
        if values!=0:
            board = cv2.circle(board,(coords[8][0],coords[8][1]),5,(255,255,255),-1)
            print("YES")
        else:
            board = cv2.circle(board,(coords[8][0],coords[8][1]),5,(0,0,0),-1)
            
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(state)
video.release()
cv2.destroyAllWindows()