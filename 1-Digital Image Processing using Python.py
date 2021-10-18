import cv2

img=cv2.imread('img1.jpg')
imgSize=cv2.resize(img,(400,400))
cv2.imshow("Output",imgSize)
cv2.waitKey(0)
