import cv2 as cv
import numpy as np
path = "Image/"
img = cv.imread(path+ "opencv.png")
cv.namedWindow("testW", cv.WINDOW_AUTOSIZE)
cv.imshow("testW", img)
cv.waitKey(1)

#our goal is to turn every white area to black

h, w, rgb = img.shape
print(h, w, rgb)

for row in range(h):
    for column in range(w):
        b, g, r = img[row, column]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        #if b == 0 and g == 0 and r == 0:
        img[row, column] = [b, g, r]

cv.imshow("black", img)
cv.waitKey(0)

cv.destroyAllWindows()

# we look all elements of the array then we said that " took the elements rgb values and we reassign them after substracting the rgb values from 255.