import cv2
image = cv2.imread("poster.jpg")
rocket = image[120:360,400:500]
image[0:240,500:600] = rocket
cv2.putText(image,"I am Nihar",(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))
cv2.imshow("nihar",image)
cv2.waitKey(0)