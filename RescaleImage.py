import cv2 as cv #pip install opencv-contribute

img = cv.imread('images/3.jpg') #reading image and putting into img @var

def rescalefream(frame,scale=0.75) :
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    demination = (width,height)
    return cv.resize(frame, demination , interpolation=cv.INTER_AREA)

frame_resied = rescalefream(img,scale=.1)
cv.imshow('Title' , frame_resied)
cv.waitKey(0) #wating for infinite Time 
