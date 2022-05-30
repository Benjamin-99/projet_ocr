# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:06:42 2021

@author: Viann_prems
"""

from cv2 import cv2
import numpy as np
import easyocr
import time
import matplotlib
import matplotlib.pyplot as plt

# decouper les zones utiles
# thersholding otsu et après les dilatations
# otsu et après binairisation


# Read Image Recto
imageRecto = cv2.imread('Images/permis-recto.jpg')
imageVerso = cv2.imread('Images/permis-verso.jpg')

# Display Image
# cv2.imshow('imageRecto', imageRecto)
# cv2.waitKey(0)
# cv2.imshow('imageVerso', imageVerso)
# cv2.waitKey(0)

# cv2.destroyAllWindows()

"""
Pré-traitement classique
"""

# Echalonage
imageRecto = cv2.resize(imageRecto, (506, 317), fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
imageVerso = cv2.resize(imageVerso, (506, 317), fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
"""
cv2.imshow('imageVerso', imageVerso)
img = cv2.cvtColor(imageVerso, cv2.COLOR_BGR2GRAY)
otsu_threshold, image_result = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('image Thresh_OTSU', image_result)
cv2.imshow('image I', img)
print(easyocr.Reader(['fr'], gpu=True).readtext(image_result, detail=0))
"""
# Recadrage de la zone de texte
yRecto = 60
x = 158
h = 25
w = 200
deltaY = 29
recto = []
verso = []

champVerso = imageVerso[28 + deltaY:28 + deltaY + 18, 160:160 + 200]
# cv2.waitKey(0)
cv2.imshow('Image', champVerso)
cv2.waitKey(0)
print(easyocr.Reader(['fr'], gpu=True).readtext(champVerso, detail=0))

"""
Extraction recto
"""
"""
for i in range(6):
    champRecto= imageRecto[yRecto + deltaY:yRecto + deltaY + h, x:x + w]
    #cv2.waitKey(0)
    cv2.imshow('Image', champRecto)
    cv2.waitKey(0)
    gray = cv2.cvtColor(champRecto, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(champRecto, cv2.COLOR_BGR2GRAY)
    otsu_threshold, image_result = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    cv2.imshow('image Thresh_OTSU', image_result)
    ret, th = cv2.threshold(img, (otsu_threshold - 69), 255, cv2.THRESH_BINARY)
    imginv = cv2.bitwise_not(th)
    taille = (2, 2)
    kernel = np.ones(taille, np.uint8)
    dilateinv = cv2.dilate(imginv, kernel, iterations=1)
    #cv2.imshow('Image', th)
    recto.append(easyocr.Reader(['fr'], gpu=True).readtext(img, detail=0))
    time.sleep(0.2)
    deltaY = deltaY+24
    print(i)

print(recto)
"""
yVerso = 28
xVerso = 200
hVerso = 18
wVerso = 200
deltaY = 29
verso = []
"""
Extraction verso
"""

for i in range(15):
    champVerso = imageVerso[yVerso + deltaY-1:yVerso + deltaY + hVerso, xVerso:xVerso + wVerso]
    print("Y :", yVerso + deltaY, " X: ", xVerso)
    # cv2.waitKey(0)
    cv2.imshow('Image', champVerso)
    cv2.waitKey(0)
    """
    gray = cv2.cvtColor(champVerso, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(champVerso, cv2.COLOR_BGR2GRAY)
    otsu_threshold, image_result = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    cv2.imshow('image Thresh_OTSU', image_result)
    ret, th = cv2.threshold(img, (otsu_threshold - 69), 255, cv2.THRESH_BINARY)
    imginv = cv2.bitwise_not(th)
    taille = (2, 2)
    kernel = np.ones(taille, np.uint8)
    dilateinv = cv2.dilate(imginv, kernel, iterations=1)
    # cv2.imshow('Image', th)
    verso.append(easyocr.Reader(['fr'], gpu=True).readtext(img, detail=0))
    time.sleep(0.2)
    """
    deltaY = deltaY + 17
    print(i)

print(verso)

nom = imageRecto[yRecto:yRecto + h, x:x + w]
prenom = imageRecto[yRecto + deltaY:yRecto + deltaY + h, x:x + w]
cv2.imshow('Image', prenom)
cv2.waitKey(0)

# Applying Grayscale filter to imageRecto
gray = cv2.cvtColor(nom, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(nom, cv2.COLOR_BGR2GRAY)

# Application de flou à travers un filtre
# cv2.threshold(cv2.GaussianBlur(img, (3, 3), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

# cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

# cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

otsu_threshold, image_result = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("Obtained threshold: ", otsu_threshold)

ret, th = cv2.threshold(gray, (otsu_threshold - 70), 255, cv2.THRESH_BINARY)

taille = (2, 2)

# Dilatation et erosion
kernel = np.ones(taille, np.uint8)
dilate = cv2.dilate(th, kernel, iterations=1)
erode = cv2.erode(th, kernel, iterations=1)
close = cv2.erode(dilate, kernel, iterations=1)

# inverser l'imageRecto - dilatation - érosion
imginv = cv2.bitwise_not(th)
kernel = np.ones(taille, np.uint8)
dilateinv = cv2.dilate(imginv, kernel, iterations=1)
erodeinv = cv2.erode(imginv, kernel, iterations=1)
closeinv = cv2.erode(dilateinv, kernel, iterations=1)

cv2.imshow('gray', gray)

cv2.imshow('Threshold OTSU', image_result)

cv2.imshow('Threshold Seuil (OTSU-66)', th)

cv2.imshow('Après dilatation', dilate)

cv2.imshow('Après érosion', erode)

cv2.imshow('Closing', close)

cv2.imshow('Inversion', imginv)

cv2.imshow('Dilatation Inv', dilateinv)
# dilateinv = cv2.bitwise_not(dilateinv)

cv2.imshow('Erosion Inv', erodeinv)
# erodeinv = cv2.bitwise_not(erodeinv)

cv2.imshow('Closing Inv', closeinv)
# closeinv = cv2.bitwise_not(closeinv)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imshow('end', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Saving filtered imageRecto to new file
# cv2.imwrite('graytest.jpg',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
