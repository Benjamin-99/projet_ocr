# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:06:42 2021

@author: Viann_prems
"""

from cv2 import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# decouper les zones utiles
# thersholding otsu et après les dilatations
# otsu et après binairisation


# Read Image
img = cv2.imread('Images/permis4.jpg')

# Display Image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Pré-traitement classique
"""

# Echalonage
img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist, 'r-')
plt.show()

# Recadrage de la zone de texte
y = 75
x = 172
h = 145
w = 200
crop = img[y:y + h, x:x + w]
cv2.imshow('Image', crop)
cv2.waitKey(0)

# Applying Grayscale filter to image
gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

histc = cv2.calcHist([crop], [0], None, [256], [0, 256])
histi = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histc, 'g-', histi, 'b-')
plt.show()

# Application de flou à travers un filtre
# cv2.threshold(cv2.GaussianBlur(img, (3, 3), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

# cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

# cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

otsu_threshold, image_result = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("Obtained threshold: ", otsu_threshold)

ret, th = cv2.threshold(gray, (otsu_threshold - 66), 255, cv2.THRESH_BINARY)

taille = (2,2)

# Dilatation et erosion
kernel = np.ones(taille, np.uint8)
dilate = cv2.dilate(th, kernel, iterations=1)
erode = cv2.erode(th, kernel, iterations=1)
close = cv2.erode(dilate, kernel, iterations=1)

# inverser l'image - dilatation - érosion
imginv = cv2.bitwise_not(th)
kernel = np.ones(taille, np.uint8)
dilateinv = cv2.dilate(imginv, kernel, iterations=1)
erodeinv = cv2.erode(imginv, kernel, iterations=1)
closeinv = cv2.erode(dilateinv, kernel, iterations=1)

cv2.imshow('gray', gray)

cv2.imshow('Threshold OTSU', image_result)

cv2.imshow('Threshold Seuil (OTSU-66)', th)
cv2.imwrite('Images/Filtre1-OTSU-66.jpg', th)

cv2.imshow('Après dilatation', dilate)
cv2.imwrite('Images/Filtre2-Dilat.jpg', dilate)

cv2.imshow('Après érosion', erode)
cv2.imwrite('Images/Filtre3-Eros.jpg', erode)

cv2.imshow('Closing', close)
cv2.imwrite('Images/Filtre4-Close.jpg', close)

cv2.imshow('Inversion', imginv)

cv2.imshow('Dilatation Inv', dilateinv)
# dilateinv = cv2.bitwise_not(dilateinv)
cv2.imwrite('Images/Filtre5-DIlatInv.jpg', dilateinv)

cv2.imshow('Erosion Inv', erodeinv)
# erodeinv = cv2.bitwise_not(erodeinv)
cv2.imwrite('Images/Filtre6-EroseInv.jpg', erodeinv)

cv2.imshow('Closing Inv', closeinv)
# closeinv = cv2.bitwise_not(closeinv)
cv2.imwrite('Images/Filtre7-CloseInv.jpg', closeinv)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imshow('end', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Saving filtered image to new file
# cv2.imwrite('graytest.jpg',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()