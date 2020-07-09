import cv2
import numpy as np

img = cv2.imread('test.jpg',0)
img1 = cv2.imread('pc.jpg',1)
cv2.imshow('image',img1)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.destroyAllWindows()