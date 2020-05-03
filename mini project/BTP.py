import cv2
import numpy as np
a=cv2.imread("f0.png",cv2.IMREAD_GRAYSCALE)
a=cv2.GaussianBlur(a,(5,5),0)
n=cv2.imread("f1.png",cv2.IMREAD_GRAYSCALE)
n=cv2.GaussianBlur(n,(5,5),0)
s=cv2.imread("f3.png",cv2.IMREAD_GRAYSCALE)
s=cv2.GaussianBlur(s,(5,5),0)
e=cv2.imread("f8.png",cv2.IMREAD_GRAYSCALE)
e=cv2.GaussianBlur(e,(5,5),0)
w=cv2.imread("f11.png",cv2.IMREAD_GRAYSCALE)
w=cv2.GaussianBlur(w,(5,5),0)

cn=cv2.absdiff(a,n)
_, cn=cv2.threshold(cn, 55,255, cv2.THRESH_BINARY)
cnw=np.sum(cn==255)
cnb=np.sum(cn==0)
cnr=(cnw/cnb)*307.71
print("north",cnw,cnb,cnr)
cv2.imshow("NORTH",cn)
cs=cv2.absdiff(a,s)
_, cs=cv2.threshold(cs, 55,255, cv2.THRESH_BINARY)
csw=np.sum(cs==255)
csb=np.sum(cs==0)
csr=(csw/csb)*307.71
print("south",csw,csb,csr)
cv2.imshow("SOUTH",cs)
ce=cv2.absdiff(a,e)
_, ce=cv2.threshold(ce, 55,255, cv2.THRESH_BINARY)
cew=np.sum(ce==255)
ceb=np.sum(ce==0)
cer=(cew/ceb)*307.71
print("east",cew,ceb,cer)
cv2.imshow("EAST",ce)
cw=cv2.absdiff(a,w)
_, cw=cv2.threshold(cw, 55,255, cv2.THRESH_BINARY)
cww=np.sum(cw==255)
cwb=np.sum(cw==0)
cwr=(cww/cwb)*307.71
print("west",cww,cwb,cwr)
cv2.imshow("WEST",cw)
xx=[cnr,csr,cer,cwr]
yy=["NORTH","SOUTH","EAST","WEST"]
print(xx)
print("TIME ALLOTED ")
for i in range(0,4):
    aa=xx.index(max(xx))
    t=round((.0049*xx[aa]*xx[aa]+0.714*xx[aa]+2.01)/2)
    if t<10:
        t=10
    if t>60:
        t=60
    print(yy[aa],t)
    xx[aa]=0
    




