import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def warp_perspective(img,pts1, pts2):

    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, (400, 400))
    return dst

def main():


    image = cv2.imread("test1.jpg")
    
    pts2 = np.float32([[0,0], [400,0], [400,400], [0,400]])
    pts1 = np.float32([[113,34],[489, 38],[575, 528],[59, 535]])

    dst = warp_perspective(image, pts1,pts2)

    cv2.imshow("image", dst)
    cv2.waitKey(0)




if __name__ == "__main__":
   main()

# 113 34, 489 38, 575 528, 59 535 test1

#  111 54, 493 58 , 585 563, 58 576 test2

# 111 54, 493 58 , 585 563, 58 576 test3

# 111 54, 493 58 , 585 563, 58 576 test4