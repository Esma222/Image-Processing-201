import cv2 as cv
import numpy as np

path = "Image/"
img = cv.imread(path + "opencv.png")
# uzunluk genişlik kanal sayısı/boyut sayısı
print(img.shape)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1)
print(gray.shape)#now one dimensional

gray = np.float32(gray)#standartlaşma işlemleri için floata çevirdik
print(gray)

minv, maxv, minl, maxl = cv.minMaxLoc(gray)
print("min_value: % .2f, max_value : % .2f" % (minv, maxv))
print("min_loc: " , minl ," max_loc : " ,maxl)
mean, std_dev = cv.meanStdDev(gray)
print("mean: " , mean ," stddev : " ,std_dev)

arrZ = np.zeros(gray.shape, dtype= np.float32)
#                 çıktı       0 ile 1 arasında sonuç dönsün
cv.normalize(gray, dst= arrZ , alpha=0, beta=1.0, norm_type= cv.NORM_MINMAX)
print(arrZ)
# intergra döndürünce küsüratlı olanlar 0 ya da 1 e dönmesin diye tüm görsel siyah olmasın diye
print(np.uint8(arrZ*255))
cv.imshow("norm",arrZ)
cv.waitKey(0)

means, std = cv.meanStdDev(np.uint8(arrZ*255))
print("mean: " , means ," stddev : " ,std)

minV, maxV, minL, maxL = cv.minMaxLoc(arrZ)
print("min_value: % .2f, max_value : % .2f" % (minV, maxV))
print("min_loc: " , minL ," max_loc : " ,maxL)



#Norm inf#bir projede normalizasyonu standartlaştırmak için kullanılıyor

arrZ = np.zeros(gray.shape, dtype= np.float32)
cv.normalize(gray, dst= arrZ, alpha=1.0, beta=0, norm_type= cv.NORM_INF)
print(arrZ)
cv.imshow("norm inf", np.uint8(arrZ*255))
cv.waitKey(0)


#norm l1

arrZ = np.zeros(gray.shape, dtype= np.float32)
cv.normalize(gray, dst= arrZ, alpha=1.0, beta=0, norm_type= cv.NORM_L1)
print(arrZ)
cv.imshow("norm L1", np.uint8(arrZ*10000000))
cv.waitKey(0)

#norm l2

arrZ = np.zeros(gray.shape, dtype= np.float32)
cv.normalize(gray, dst= arrZ, alpha=1.0, beta=0, norm_type= cv.NORM_L2)
print(arrZ)
cv.imshow("norm L2" ,np.uint8(arrZ*10000))
cv.waitKey(0)














