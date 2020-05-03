import cv2
a=cv2.imread("IMG_1208.jpg")
ga=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
(thresh, bw) = cv2.threshold(ga, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("a",a)
cv2.imshow("b",ga)
cv2.imshow("c",bw)


