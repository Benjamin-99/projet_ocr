from fastapi import FastAPI

import uvicorn
import cv2
import numpy as np
import easyocr


"""
carte grise
"""
chemin = 'Images/cartegrise.jpg'

def extractCarteGrise(chemin_recto):
    # Read Image Recto
    imageRecto = cv2.imread(chemin)

    """
    Pré-traitement classique
    """
    # Echalonage
    imageRecto = cv2.resize(imageRecto, (346, 664), fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

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
    xRecto = 34
    yRecto = 72
    hRecto = 75
    wRecto = 32

    threshold(xRecto, yRecto, hRecto, wRecto)

    # Prenom
    xRecto = 31
    yRecto = 67
    hRecto = 65
    wRecto = 28
    threshold(xRecto, yRecto, hRecto, wRecto)

    # numero immatriculation
    xRecto = 27
    yRecto = 31
    hRecto = 82

    threshold(xRecto, yRecto, hRecto, wRecto)

    # Lieu de naissance
    yRecto = 184
    hRecto = 202
    wRecto = 400
    threshold(xRecto, yRecto, hRecto, wRecto)

    # adress
    xRecto = 30
    yRecto = 187
    hRecto = 32
    wRecto = 208
    threshold(xRecto, yRecto, hRecto, wRecto)

    # marque
    xRecto = 31
    yRecto = 79
    hRecto = 33
    wRecto = 87
    threshold(xRecto, yRecto, hRecto, wRecto)

    # code identification
    xRecto = 223
    yRecto = 301
    hRecto = 222
    wRecto = 297
    threshold(xRecto, yRecto, hRecto, wRecto)

    # version
    xRecto = 32
    yRecto = 83
    hRecto = 33
    wRecto = 82
    threshold(xRecto, yRecto, hRecto, wRecto)

    # date imatriculation
    xRecto = 32
    yRecto = 101
    hRecto = 31
    wRecto = 96
    threshold(xRecto, yRecto, hRecto, wRecto)

    # Numéro document
    yRecto = 234
    hRecto = 255
    wRecto = 380
    threshold(xRecto, yRecto, hRecto, wRecto)

    # Date visite
    xRecto = 120
    yRecto = 176
    hRecto = 122
    wRecto = 182
    threshold(xRecto, yRecto, hRecto, wRecto)

    # Traitement du verso
    print(recto)
    return recto



    """
    Traitement 
    """
    for elt in recto:
        for i in elt:
            lt = i.split(' ')
            for l in lt:
                if l.__contains__("("):
                    result.append(l[1:])
                elif l.__contains__(")"):
                    result.append(l[:3])
                elif not (l.__contains__("4c")):
                    result.append(l)
    print(result)

