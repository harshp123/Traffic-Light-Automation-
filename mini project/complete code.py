import cv2
a=cv2.imread("a2.png",0)
a=cv2.GaussianBlur(a,(5,5),0)
b=cv2.imread("f1.png",0)
b=cv2.GaussianBlur(b,(5,5),0)


c=cv2.absdiff(a,b)
_, cc=cv2.threshold(c, 50,255, cv2.THRESH_BINARY)
count=cv2.findContours(a,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]
s1=800
s2=5000
j=0
for i in count:
    if s1<cv2.contourArea(i)<s2:
        j=j+1
print(j)
cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.imshow("c",c)
cv2.imshow("cc",cc)

