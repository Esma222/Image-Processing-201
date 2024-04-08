# VIDEO READ AND WRITE

import cv2 as cv
import numpy as np

capture = cv.VideoCapture("Video/video-1.mp4")
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)
print (height,width,count,fps)

out = cv.VideoWriter("Video/video-1.avi",
                     cv.VideoWriter_fourcc('D','I','V','X'),15,
                     (np.int_(width),np.int_(height)),True)

while True:
    #kameradan görüntü al
 ret, frame = capture.read()

 if ret is True:
     cv.imshow("video-input", frame)
     out.write(frame)
     #50 saniye sonra çık
     c = cv.waitKey(10)
     if c==27: # ESC
         break
 else:
     break