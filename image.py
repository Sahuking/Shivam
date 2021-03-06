from PIL import Image

im = Image.open('10000619.jpg')
im.show()
####################################################################
import cv2
import numpy as np
from matplotlib import pyplot as plt

im = cv2.imread('10000619.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('GoldenGate',im)
hist = cv2.calcHist([im],[0],None,[256],[0,256])
plt.hist(im.ravel(),256,[0,256])
plt.title('Histogram for gray scale picture')
plt.show()

####################################################################
img = cv2.imread('10000619.jpg',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
#####################################################################

cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]
plt.plot(cdf_m, color = 'b')
plt.hist(img2.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
#####################################################################

img = cv2.imread('10000619.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.jpg',res)

#####################################################################

img = cv2.imread('10000619.jpg',0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imwrite('clahe_2.jpg',cl1)
