import cv2 as cv #pip install opencv-contribute

img = cv.imread('images/4.jpg') #reading image and putting into img @var
cv.imshow('Read Image No Resize',img) #imgShow SetTitel And Loading Image Here
cv.waitKey(0) #wating for infinite Time 
