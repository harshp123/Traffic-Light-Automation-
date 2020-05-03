import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('o3.jpg',0)
edges = cv2.Canny(img,100,200)
edges=cv2.GaussianBlur(edges,(5,5),0)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
count=cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]
print(len(count))
j=0
for i in count:
    if 100<cv2.contourArea(i)<500:
        j=j+1
print(j)
plt.show()
