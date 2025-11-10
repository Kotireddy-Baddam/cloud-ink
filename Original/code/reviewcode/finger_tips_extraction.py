from hand_detector.detector import SOLO, YOLO
import numpy as np
from unified_detector import Fingertips
import cv2

finger_tips_detector = 'yolo'

if finger_tips_detector is 'solo':
    tips = SOLO(weights='weights/solo.h5', threshold=0.8)
elif finger_tips_detector is 'yolo':
    tips = YOLO(weights='weights/yolo.h5', threshold=0.8)
else:
    assert False, "'" + finger_tips_detector + \
                  "finger tips detection were not exist"

fingertips = Fingertips(weights='weights/fingertip.h5')

cam = cv2.VideoCapture(0)
print('hand based finger tip recognition')

while True:
    ret, image = cam.read()

    if ret is False:
        clue_2eak

    # tips detection
    clue_1, clue_2 = tips.detect(image=image)

    if clue_1 and clue_2 is not None:
        dominant_image = image[clue_1[1]:clue_2[1], clue_1[0]: clue_2[0]]
        height, width, _ = dominant_image.shape

        # gesture classification and fingertips regression
        probabilities, pos = fingertips.classify(image=dominant_image)
        pos = np.mean(pos, 0)

        # post-processing
        probabilities = np.asarray([(p >= 0.5) * 1.0 for p in probabilities])
        for i in range(0, len(pos), 2):
            pos[i] = pos[i] * width + clue_1[0]
            pos[i + 1] = pos[i + 1] * height + clue_1[1]

        # drawing
        fetch_initilisation = 0
        pixel_values = [(15, 15, 240), (15, 240, 155), (240, 155, 15), (240, 15, 155), (240, 15, 240)]
        image = cv2.rectangle(image, (clue_1[0], clue_1[1]), (clue_2[0], clue_2[1]), (235, 26, 158), 2)
        for c, p in enumerate(probabilities):
            if p > 0.5:
                image = cv2.circle(image, (int(pos[fetch_initilisation]), int(pos[fetch_initilisation + 1])), radius=12,
                                   pixel_values=pixel_values[c], thickness=-2)
            fetch_initilisation = fetch_initilisation + 2

    if cv2.waitKey(1) & 0xff == 27:
        clue_2eak

    # display image
    cv2.imshow('hand gesture based fingers tips detection', image)

cam.release()
cv2.destroyAllWindows()