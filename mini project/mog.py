import numpy as np 
import cv2 
  
frame=cv2.imread("aa.png")
bbb=cv2.imread("bb.png")
fgbg = cv2.createBackgroundSubtractorMOG2() 
  
while(1): 
  
    fgmask = fgbg.apply(frame) 
   
    cv2.imshow('fgmask', frame) 
    cv2.imshow('frame', fgmask) 
  
      
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
      
  
cv2.destroyAllWindows() 
