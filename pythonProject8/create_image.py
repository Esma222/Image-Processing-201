import cv2 as cv
import numpy as np

path = "Image/"
img = cv.imread(path+"img.png")
cv.namedWindow("colWin", cv.WINDOW_AUTOSIZE)
cv.imshow("colWin", img)
cv.waitKey(1)

cp = np.copy(img)
m2 = img
type(img)

img[100:200, 200:300, :] = 100
cv.imshow("m2", m2)
cv.waitKey(1)

m3 = np.zeros(img.shape, img.dtype)
cv.imshow("m3", m3)
cv.waitKey(1)

m4 = np.zeros([512, 512], np.uint8)
cv.imshow("m4", m4)
cv.waitKey(1)

m5 = np.zeros([512, 512], np.uint8)
m5[:, :] = 127
cv.imshow("m5", m5)
cv.waitKey(1)

img = np.ones((550, 770, 3))
black = (0, 0, 0)
red = (0, 0, 255)
green = (0, 255, 0)


cv.rectangle(img, (480,250), (100,450), black, 8)
cv.rectangle(img, (580,150), (200,350), black, 8)
cv.line(img, (100,450), (200,350), black, 8)
cv.line(img, (480,250), (580,150), black, 8)
cv.line(img, (100,250), (200,150), black, 8)
cv.line(img, (480,450), (580,350), black, 8)

start_point = (150,100)
font_thinkness = 2
font_size = 1
font = cv.FONT_HERSHEY_DUPLEX

cv.putText(img,"www.cizim.com.tr", start_point, font, font_size, black, font_thinkness)
cv.imshow("dikdörtgen", img)
cv.waitKey(0)
cv.destroyAllWindows()


