import cv2
a=cv2.imread("o3.jpg",0)
a=cv2.GaussianBlur(a,(45,45),0)
b=cv2.imread("o3.jpg")
b=cv2.GaussianBlur(b,(5,5),0)
_, cc=cv2.threshold(a,235,255, cv2.THRESH_BINARY)
cv2.imshow("K",a)
cv2.imshow("KK",cc)
d=cv2.bitwise_not(cc)
cv2.imshow("KKhg",d)
blue=b[:,:,0]
green=b[:,:,1]
red=b[:,:,2]
#x=cv2.bitwise_and(blue,d,mask=None)
#cv2.imread("xxx",xx)
g1=cv2.bitwise_and(blue,d,mask=None)
g2=cv2.bitwise_and(green,d,mask=None)
g3=cv2.bitwise_and(red,d,mask=None)
x=cv2.merge((g1,g2,g3))
cv2.imshow("x",x)
