import cv2

img=cv2.imread('img1.jpg')

width,height=300,300

imagesize=cv2.resize(img,(width,height))
cv2.imshow("Orginal color",imagesize)

color=cv2.cvtColor(imagesize,cv2.COLOR_RGB2HLS)
blurColor=cv2.GaussianBlur(imagesize,(5,5),0)

cv2.imshow("Image Color",color)
cv2.imshow('Image clurColor',blurColor)

colors=cv2.cvtColor(imagesize,cv2.COLOR_Luv2RGB)
cv2.imshow("Image Colors",colors)

color1=cv2.cvtColor(imagesize,cv2.COLOR_BGR2LAB)
cv2.imshow("Image Color1",color1)

colors2=cv2.cvtColor(imagesize,cv2.COLOR_HSV2BGR)
cv2.imshow("Image Colors2",colors2)

colors3=cv2.cvtColor(imagesize,cv2.COLOR_Lab2RGB)
cv2.imshow("Image Colors3",colors3)

cv2.waitKey(0)
