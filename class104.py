import cv2
#from google.colab.patches import cv2_imshow
image = cv2.imread("butterfly.jpg")
#cv2.imshow("Displaying the image",image)
gray_img = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow("grayimage",gray_img)
print(gray_img)
cv2.waitKey(0)
