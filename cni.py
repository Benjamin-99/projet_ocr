# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:06:42 2021

@author: Viann_prems
"""
from PIL import Image
from cv2 import cv2
import numpy as np
import easyocr
import time
import matplotlib
import matplotlib.pyplot as plt

cni_recto_path = 'Images/cnirecto.png'
cni_verso_path = 'Images/cniverso.png'


# decouper les zones utiles
# thersholding otsu et après les dilatations
# otsu et après binairisation

def permirecto(cni_recto_path):
    def perfection(file_name, new_file_name):
        img = Image.open(file_name)
        largeur_image, hauteur_image = img.size
        for y in range(hauteur_image):
            for x in range(largeur_image):
                t, r, v, b = img.getpixel((x, y))
                if (145 < t < 220) or (145 < r < 220) or (150 < v < 255):
                    img.putpixel((x, y), (255, 255, 255, 255))
        img.save(new_file_name)

    perfection(cni_recto_path, 'Images/rectotraite.png')

    # Read Image Recto
    imageRecto = cv2.imread('Images/rectotraite.png')

    """
    Pré-traitement classique
    """

    # Echalonage
    imageRecto = cv2.resize(imageRecto, (506, 322), fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

    # Recadrage de la zone de texte
    yRecto = 0
    xRecto = 50
    hRecto = 55
    wRecto = 450
    recto = []

    def threshold(xRecto, yRecto, hRecto, wRecto):
        champRecto = imageRecto[yRecto:hRecto, xRecto:wRecto]
        img = cv2.cvtColor(champRecto, cv2.COLOR_BGR2GRAY)
        recto.append(easyocr.Reader(['fr'], gpu=True).readtext(img, detail=0))

    # Pays
    threshold(xRecto, yRecto, hRecto, wRecto)

    # Nom
    xRecto = 200
    yRecto = 76
    hRecto = 90

    threshold(xRecto, yRecto, hRecto, wRecto)

    # Prenom
    yRecto = 118
    hRecto = 130
    threshold(xRecto, yRecto, hRecto, wRecto)

    # Zone correspondant au sexe
    xRecto = 200
    yRecto = 158
    hRecto = 178
    wRecto = 500
    threshold(xRecto, yRecto, hRecto, wRecto)

    # Lieu de naissance
    yRecto = 184
    hRecto = 202
    wRecto = 400
    threshold(xRecto, yRecto, hRecto, wRecto)

    # Nom d'usage
    yRecto = 208
    hRecto = 220
    wRecto = 500
    threshold(xRecto, yRecto, hRecto, wRecto)

    # Numéro document
    yRecto = 234
    hRecto = 255
    wRecto = 380
    threshold(xRecto, yRecto, hRecto, wRecto)

    # Date d'expiration
    xRecto = 360
    yRecto = 232
    hRecto = 260
    wRecto = 500
    threshold(xRecto, yRecto, hRecto, wRecto)

    # Traitement du verso
    print(recto)
    return recto


def permiverso(cni_verso_path):
    imageVerso = cv2.imread(cni_verso_path)
    imageVerso = cv2.resize(imageVerso, (506, 322), fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    # Taille
    yRecto = 26
    xRecto = 136
    hRecto = 55
    wRecto = 200
    verso = []
    def thresholdverso(xRecto, yRecto, hRecto, wRecto):
        champVerso = imageVerso[yRecto:hRecto, xRecto:wRecto]
        img = cv2.cvtColor(champVerso, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('Images/versotraite.png', img)
        verso.append(easyocr.Reader(['fr'], gpu=True).readtext(champVerso, detail=0))

    thresholdverso(xRecto, yRecto, hRecto, wRecto)
    # Date de délivrance
    yRecto = 26
    xRecto = 211
    hRecto = 55
    wRecto = 500
    thresholdverso(xRecto, yRecto, hRecto, wRecto)

    # Adresse
    xRecto = 135
    yRecto = 58
    hRecto = 140
    wRecto = 500
    thresholdverso(xRecto, yRecto, hRecto, wRecto)
    print(verso)
    return verso


permiverso(cni_verso_path)

