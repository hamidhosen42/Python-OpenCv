import cv2

cap=cv2.VideoCapture(0)

tracker=cv2.TrackerCSRT_create()
success,img=cap.read()
bounding_box=cv2.selectROI('Tracker Frequency',img,False)
tracker.init(img,bounding_box)

def drawbox(img,bounding_box):
    x,y,w,h=int(bounding_box[0]),int(bounding_box[1]),int(bounding_box[2]),int(bounding_box[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),2,1)
    cv2.putText(img,"Tracker",(40,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0.255,255),2)


while True:
    time=cv2.getTickCount()
    success,img=cap.read()

    success,bounding_box=tracker.update(img)
    print(bounding_box)

    if success:
        drawbox(img, bounding_box)

    frequency=cv2.getTickFrequency()/(cv2.getTickCount()-time)
    cv2.putText(img, str(int(frequency)), (70,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255,255),2)

    cv2.imshow("Tracking img",img)

    if cv2.waitKey(1) & 0xff == ord('x'): # x press them VideoCapture off
        break
