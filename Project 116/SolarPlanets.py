import cv2
img=cv2.imread("solar-system.jpg")
cv2.putText(img,"sun",(60,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,500))
cv2.putText(img,"mercury",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,100,100))
cv2.putText(img,"venus",(190,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,50,80))
cv2.putText(img,"earth",(285,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
cv2.putText(img,"mars",(380,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,50,500))
cv2.putText(img,"jupiter",(540,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"saturn",(740,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"uranus",(970,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"neptune",(1110,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.imshow("output",img)
cv2.waitKey(0)