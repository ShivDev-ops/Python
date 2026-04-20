import cv2 as cv
img_read = cv.imread('lena.jpg')
cv.imshow('lena',img_read)
cv.waitKey(0)
