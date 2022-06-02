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
imageRecto = cv2.resize(imageRecto, (506, 316), fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
imageVerso = cv2.resize(imageVerso, (506, 316), fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
"""
cv2.imshow('imageVerso', imageVerso)
img = cv2.cvtColor(imageVerso, cv2.COLOR_BGR2GRAY)
otsu_threshold, image_result = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('image Thresh_OTSU', image_result)
cv2.imshow('image I', img)
print(easyocr.Reader(['fr'], gpu=True).readtext(image_result, detail=0))
"""
# Recadrage de la zone de texte
yRecto = 65
xRecto = 164
hRecto = 80
wRecto = 310
recto = []
"""
#65:80,163:310 img
#85:100,163:310 img
#105:120,163:310
#125:140,163;310 img
#145:160 img
#160:175 img
champRecto = imageRecto[yRecto:hRecto, xRecto:wRecto]
# cv2.waitKey(0)
cv2.imshow('Image', champRecto)
cv2.waitKey(0)
img = cv2.cvtColor(champRecto, cv2.COLOR_BGR2GRAY)
otsu_threshold, image_result = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
ret, th = cv2.threshold(img, (otsu_threshold - 69), 255, cv2.THRESH_BINARY)
imginv = cv2.bitwise_not(th)
taille = (2, 2)
kernel = np.ones(taille, np.uint8)
dilateinv = cv2.dilate(imginv, kernel, iterations=1)
cv2.imshow('Image', image_result)
cv2.waitKey(0)
print(easyocr.Reader(['fr'], gpu=True).readtext(img, detail=0))
"""
"""
Extraction recto
"""

for i in range(5):
    champRecto= imageRecto[yRecto:hRecto, xRecto:wRecto]
    img = cv2.cvtColor(champRecto, cv2.COLOR_BGR2GRAY)
    recto.append(easyocr.Reader(['fr'], gpu=True).readtext(img, detail=0))
    time.sleep(0.2)
    yRecto = yRecto + 20
    hRecto = hRecto + 20

img = cv2.cvtColor(imageRecto[160:175, xRecto:wRecto], cv2.COLOR_BGR2GRAY)
recto.append(easyocr.Reader(['fr'], gpu=True).readtext(img, detail=0))
time.sleep(0.2)
print(recto)

"""
Traitement du recto
"""

lt = [i.split(' ', 1) for i in recto[2]]
print(lt)

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

yVerso = 30
xVerso = 223
hVerso = 43
wVerso = 338
deltaY = 29
verso = []
categories = ['AM','A1','A2','A','B1','B','C1','C','D1','D','BE','C1E','CE','D1E','DE']
"""
Extraction verso
"""
"""
for i in range(15):
    champVerso = imageVerso[yVerso:hVerso, xVerso:wVerso]
    img = cv2.cvtColor(champVerso, cv2.COLOR_BGR2GRAY)
    verso.append(easyocr.Reader(['fr'], gpu=True).readtext(img, detail=0))
    time.sleep(0.2)
    yVerso = yVerso + 15
    hVerso = hVerso + 15

for i in range(15):
    if verso[i]:
        print(categories[i])
"""

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
