# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:33:23 2022

@author: Viann_prems
"""

import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plt
import json
import Classes
import database_connection as db

im_1_path = 'Images/permis4.jpg'
print(im_1_path)


def recognize_text(img_path):
    '''loads an image and recognizes text.'''

    reader = easyocr.Reader(['fr'])
    return reader.readtext(img_path,detail=0)


result = recognize_text(im_1_path)

print("Obtained result:", result)

personne = {"Country" : result[1],
            "firstName" : result[3],
            "lastName" : result[4],
            "birthDate" : result[5],
            "birthPlace" : result[5],
            "issueDate" : result[6],
            "expiryDate" : result[8],
            "deliveredAutority" : "",
            "mrzBand" : ""
           }

print(personne['Country'])

permis = Classes.PermisClass("Vanessa","MAPA",
                             "1585-10-12","Baganté",
                             "2020-10-15","2025-10-15",
                             "Limoges", "B", "123456789", "9876543210")

db.save_permis(permis)

print("Fini ! ")