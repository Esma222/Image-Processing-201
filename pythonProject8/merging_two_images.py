import cv2 as cv
import numpy as np

path = "Image/"
img1 = cv.imread(path + "first.jpg")
img2 = cv.imread(path + "second.jpg")
cv.imshow("jim", img1)
cv.waitKey(1)
cv.imshow("dwight", img2)
cv.waitKey(1)

horizontal = np.hstack((img1,img2))
cv.imshow("office",horizontal)
cv.waitKey(0)
cv.destroyAllWindows()