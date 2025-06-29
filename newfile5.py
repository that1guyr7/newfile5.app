import cv2
import numpy as np

blobs = cv2.imread("Assets/blobs.jpeg")
grey = cv2.cvtColor(blobs,cv2.COLOR_BGR2GRAY)
#cv2.imshow("bobby7", grey)
#cv2.waitKey(0)

greyblur = cv2.medianBlur(grey,7)
# cv2.imshow("bobby+",greyblur)
# cv2.waitKey(0)

#Detect circles

# circles = cv2.HoughCircles(greyblur,cv2.HOUGH_GRADIENT,dp=1,minDist=20
#     ,param1=100
                                                                
                                                                
#                                                                 ,param2=30
                                                                
                                                                
#                                                                                                             ,
                                                                                                            











                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
#                                                                                                             minRadius=10
                                                                
                                                                
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
 
 
 
 
 
# ,maxRadius=100)

# print(circles)
# circles = np.uint16(np.around(circles))
# for i in circles[0,:]:
#     cv2.circle(blobs,(i[0],i[1]),i[2],(255,0,111),3)
# cv2.imshow("bobby777",blobs)
# cv2.waitKey(0)

#Detect blobs

params = cv2.SimpleBlobDetector_Params()
params.filterByCircularity = True
params.minCircularity = 0.7
params.filterByInertia = True
params.minInertiaRatio = 0.1
detector = cv2.SimpleBlobDetector_create(params)
keyPoints= detector.detect(blobs)
print(keyPoints)
