import cv2 as cv
path = "Image/"
img = cv.imread(path+"chess-8348280_1920.png")
type(img)
cv.namedWindow("colored_test", cv.WINDOW_AUTOSIZE)
cv.imshow("colored_test", img)
cv.waitKey(1)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1)
cv.imwrite(path+"gray_opencv.png", gray)

cv.destroyAllWindows()

img = cv.imread(path + "chess-8348280_1920.png", cv.IMREAD_GRAYSCALE)
cv.namedWindow("gray", cv.WINDOW_AUTOSIZE)
cv.imshow("gray",img)
cv.waitKey(0)