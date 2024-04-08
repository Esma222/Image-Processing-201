import cv2 as cv
import numpy as np

path = "Image/"
src = cv.imread(path + "opencv.png", cv.IMREAD_GRAYSCALE)
cv.imshow("ilk", src)
cv.waitKey(1)

#minmaxLocation
#we will access to basic statistics of pictures then normalize them

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(src)
print("min_value: % .2f, max_value : % .2f" % (min_value, max_value))
print("min_loc: " , min_loc ," max_loc : " ,max_loc)

#meanStdDev

mean, std_dev = cv.meanStdDev(src)
#print("mean: % .2f, std_dev : % .2f" % (mean, std_dev))
print("mean: " , mean ," stddev : " ,std_dev)
src[np.where(src<mean)] = 0
src[np.where(src>mean)] = 255

cv.imshow("binary", src)
cv.waitKey(0)