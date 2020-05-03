import cv2
import numpy as np
a=cv2.imread("f0.png",cv2.IMREAD_GRAYSCALE)
a=cv2.GaussianBlur(a,(5,5),0)
b=cv2.imread("f9.png",cv2.IMREAD_GRAYSCALE)
b=cv2.GaussianBlur(b,(5,5),0)


c=cv2.absdiff(a,b)
_, c=cv2.threshold(c, 55,255, cv2.THRESH_BINARY)


n_white_pix=np.sum(c==255)
n_black_pix=np.sum(c==0)

print(n_white_pix)
print(n_black_pix)
print(n_white_pix/n_black_pix)
cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.imshow("c",c)


