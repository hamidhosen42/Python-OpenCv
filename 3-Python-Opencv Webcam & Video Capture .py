# import the opencv library
import cv2

# # define a video capture object
# vid = cv2.VideoCapture("vedio1.mp4")
# 
# while (True):
#     ret, frame = vid.read()
#     imagesize=cv2.resize(frame,(400,400))
#     cv2.imshow('frame', imagesize)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

vid2=cv2.VideoCapture(0)

while (True):
    ret1, frame1 = vid2.read()
    imagesize1=cv2.resize(frame1,(400,400))
    cv2.imshow('frame', imagesize1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
