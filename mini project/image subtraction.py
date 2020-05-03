import cv2
from matplotlib import pyplot as plt
a=cv2.imread("aa.png",0)
a=cv2.GaussianBlur(a,(5,5),0)
b=cv2.imread("bb.png",0)
b=cv2.GaussianBlur(b,(5,5),0)
#ga=cv2.cvtColour(a, cv2.COLOUR_BGR2GRAY)

c=cv2.absdiff(a,b)
_, c=cv2.threshold(c, 55,255, cv2.THRESH_BINARY)


cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.imshow("c",c)
#cv2.waitkey(10000)
#cv2.destroyAllWindows()
plt.show()
