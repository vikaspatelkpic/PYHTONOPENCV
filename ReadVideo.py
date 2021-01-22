import cv2 as cv #pip install opencv-contribute
capture = cv.VideoCapture('video/1.mp4') #(-215:Assertion failed) File Not Found
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#cv.waitKey(0) #wating for infinite Time 
capture.release()
cv.destroyAllWindows()
