import cv2
import numpy as np

img = cv2.imread('images\\5.jpg')
height = 600
width = 500
img = cv2.resize(img, (width, height))
#cv2.imshow('res',img)
print('shape =' , img.shape)
print('no. of pixels= ',img.size)
print("datatype==",img.dtype) 
print("Imagetype==",type(img))
#print(img)

#splitting the image 
b,g,r = cv2.split(img)
"""""
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
cv2.imshow('res',img)

mr1 = cv2.merge((r,g,b))
cv2.imshow("rgb",mr1)
mr2 = cv2.merge((g,b,r))
cv2.imshow("gbr",mr2)
cv2.imshow('og', img)
 """

img = cv2.imread('images\\3.jpg')

blue = img[520,580,0]
print("the pixel having blue color==",blue)

grn = img[520,580,1] #for green pass 1
print("the pixel having grn color==",grn)
red = img[520,580,2] #for red pass 2
print("the pixel having red color==",red)

cv2.waitKey(0)
cv2.destroyAllWindows()