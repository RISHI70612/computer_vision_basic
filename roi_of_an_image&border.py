import cv2
import numpy as np

#read image
img = cv2.imread("images\\cap.jpg")

height= 800
width = 800
img = cv2.resize(img,(width, height))

cv2.imshow("img",img)


#creating image border 
brdr = cv2.copyMakeBorder(img,10,10,10,5,cv2.BORDER_CONSTANT,value = [255,0,125])

cv2.imshow("res",brdr)


#Now extract  area of interest from an image

#now pass like [y1:y2,x1:x2]
#roi = img[250:500,320:440]
#cv2.imshow("roi image==",roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
