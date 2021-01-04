import cv2
import numpy as np

img=cv2.imread("D:\\Python\\py projects\\ironman.jpg")    # Please mention the correct dirrectory of an image with extension
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge=cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
cv2.imshow("img",img)
cv2.imshow("edge",edge)
