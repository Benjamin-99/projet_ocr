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

def extractCNI(cni_recto_path, cni_verso_path):
    result1 = permirecto(cni_recto_path)
    result2 = permiverso(cni_verso_path)
    return [result1, result2]


def permirecto(cni_recto_path):
    def perfection(file_name):
        img = Image.open(file_name)
        largeur_image, hauteur_image = img.size
        for y in range(hauteur_image):
            for x in range(largeur_image):
                t, r, v, b = img.getpixel((x, y))
                if (145 < t < 220) or (145 < r < 220) or (150 < v < 255):
                    img.putpixel((x, y), (255, 255, 255, 255))
        return img

    # Read Image Recto
    imageRecto = perfection(cni_recto_path)

    """
    Pré-traitement classique
    """

    # Echalonage
    newsize = (506, 322)
    imageRecto = imageRecto.resize(newsize)

    # Recadrage de la zone de texte
    yRecto = 0
    xRecto = 50
    hRecto = 55
    wRecto = 450
    recto = []

    def threshold(xRecto, yRecto, hRecto, wRecto):
        champRecto = imageRecto.crop((xRecto, yRecto, wRecto, hRecto))
        champRectoResult = np.array(champRecto)
        recto.append(easyocr.Reader(['fr'], gpu=True).readtext(champRectoResult, detail=0))

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
    imageVerso = Image.open(cni_verso_path)
    newsize = (506, 322)
    imageVerso = imageVerso.resize(newsize)

    # Taille
    yRecto = 26
    xRecto = 136
    hRecto = 55
    wRecto = 200
    verso = []

    def thresholdverso(xRecto, yRecto, hRecto, wRecto):
        champRecto = imageVerso.crop((xRecto, yRecto, wRecto, hRecto))
        champRectoResult = np.array(champRecto)
        verso.append(easyocr.Reader(['fr'], gpu=True).readtext(champRectoResult, detail=0))

    thresholdverso(xRecto, yRecto, hRecto, wRecto)
    # Date de délivrance
    yRecto = 26
    xRecto = 211
    hRecto = 55
    wRecto = 500
    thresholdverso(xRecto, yRecto, hRecto, wRecto)

    # Adresse
    xRecto = 130
    yRecto = 54
    hRecto = 150
    wRecto = 400
    thresholdverso(xRecto, yRecto, hRecto, wRecto)

    print(verso)
    return verso


#print(extractCNI(cni_recto_path, cni_verso_path))
# permirecto(cni_recto_path)
# permiverso(cni_verso_path)
