from datetime import time

import cv2
import easyocr
from fastapi import FastAPI

import unicorn

app = FastAPI()


"""
Permis de conduire
"""
chemin_recto = 'Images/permis-recto.jpg'
chemin_verso = 'Images/permis-verso.jpg'

def extractPermis(chemin_recto, chemin_verso):
    # Read Image Recto
    imageRecto = cv2.imread(chemin_recto)
    imageVerso = cv2.imread(chemin_verso)

    """
    Pré-traitement classique
    """
    # Echalonage
    imageRecto = cv2.resize(imageRecto, (506, 316), fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    imageVerso = cv2.resize(imageVerso, (506, 316), fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

    # Recadrage de la zone de texte
    yRecto = 65
    xRecto = 164
    hRecto = 80
    wRecto = 310
    recto = []
    result = []

    """
    Extraction recto
    """
    print("Recto")
    for i in range(5):
        champRecto = imageRecto[yRecto:hRecto, xRecto:wRecto]
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

    """
    Extraction verso
    """
    yVerso = 30
    xVerso = 223
    hVerso = 43
    wVerso = 338
    verso = []
    categories = ['AM', 'A1', 'A2', 'A', 'B1', 'B', 'C1', 'C', 'D1', 'D', 'BE', 'C1E', 'CE', 'D1E', 'DE']

    print("Verso")
    for i in range(15):
        champVerso = imageVerso[yVerso:hVerso, xVerso:wVerso]
        img = cv2.cvtColor(champVerso, cv2.COLOR_BGR2GRAY)
        verso.append(easyocr.Reader(['fr'], gpu=True).readtext(champVerso, detail=0))
        time.sleep(0.2)
        yVerso = yVerso + 15
        hVerso = hVerso + 15

    for i in range(15):
        if verso[i]:
            result.append(categories[i])
    print(result)


extractPermis(chemin_recto, chemin_verso)

@app.get("/")
async def hello_world():
 return {extractPermis(chemin_recto, chemin_verso)}

if __name__== "__main__":
    unicorn.run(app, host="127.0.0.1", port=8000)