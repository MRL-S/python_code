import cv2
import numpy as np

img = cv2.imread("building.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray,50,100)
lines = cv2.HoughLinesP(canny,1.0,np.pi/180,200,minLineLength=50,maxLineGap=30)
lines1 = lines[:,0,:]
for x1, y1, x2, y2 in lines1[:]:
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 2)
cv2.imshow("line",img)
cv2.waitKey(0)
cv2.destroyAllWindows()