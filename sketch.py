import cv2
image = cv2.imread('r3.jpg')
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.bitwise_not(cv2.GaussianBlur(gray_img, (21,21), 0))
inverted_blur = cv2.bitwise_not(blur)

sketch = cv2.divide(gray_img, inverted_blur, scale=256)
cv2.imwrite('sketch.png', sketch)

#
# import cv2
# image = cv2.imread('t.jpg')
# gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur = cv2.bitwise_not(cv2.GaussianBlur(gray_img, (21,21), 0)
# invert = cv2.bitwise_not(blur)
# inverted_blur = cv2.bitwise_not(blur)
# sketch = cv2.divide(gray_img, inverted_blur, scale=256)
# cv2.imwrite('sketch.png', sketch)
#
