import numpy as np
import cv2

black = np.zeros([600,600])
# row = black[1:2]
# print(row)
black[279:449,200:400] = 255
cv2.imshow("black",black)
cv2.waitKey(0)
