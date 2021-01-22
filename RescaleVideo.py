import cv2 as cv #pip install opencv-contribute

capture = cv.VideoCapture('video/1.mp4') #reading video and putting into img @var

def rescalefream(frame,scale=0.5) :
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    demination = (width,height)
    return cv.resize(frame, demination , interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()
    frame_resied = rescalefream(frame)
    # cv.imshow('Video',frame)
    cv.imshow('Video',frame_resied)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()