import cv2
import numpy as np 

img1 = cv2.imread("images\\1.jpg")
img2 = cv2.imread("images\\2.jpg")

height = 800
width = 800

img1 = cv2.resize(img1,(width, height))
img2 =cv2.resize(img2,(width, height))

cv2.imshow('one',img1)
cv2.imshow('two',img2)

result1 = cv2.add(img1,img2)
result2 = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow("result1==",result1)
cv2.imshow("result2==",result2)
cv2.waitKey(0)
cv2.destroyAllWindows()