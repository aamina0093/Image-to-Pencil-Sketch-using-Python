#program to convert image to sketch
import cv2
#reading image
image = cv2.imread("bird.jfif")
#cv2.imshow("test image", image)
#cv2.waitKey(0)

#convert the RGB image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("test image", gray_image)
#cv2.waitKey(0)

#convert the grayscale image to create negative image to enhance details.
inverted_image = 255 - gray_image
#cv2.imshow("test image", inverted_image)
#cv2.waitKey(0)

#to blur the negative image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
#cv2.imshow("test image", blurred)
#cv2.waitKey(0)

inverted_blurred = 255 - blurred
#cv2.imshow("test image", inverted_blurred)
#cv2.waitKey(0)

#mix grayscale with the inverted image by dividing grayscale by inverted image
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)
