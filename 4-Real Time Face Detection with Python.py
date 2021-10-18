import cv2

face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# cap=cv2.VideoCapture("v3.mp4")
cap=cv2.VideoCapture(0)

while True:
    reg,img=cap.read()
    imagesize=cv2.resize(img,(400,400))
    color=cv2.cvtColor(imagesize,cv2.COLOR_RGB2HLS)
    faces=face.detectMultiScale(imagesize,1.1,2)
    for(x,y,w,h) in faces:
        cv2.rectangle(imagesize,(x,y),(x+w,y+h),(225,0,0),2)
        cv2.imshow("img",imagesize)
        k=cv2.waitKey(1) & 0xFF
        if k==27:
            break
