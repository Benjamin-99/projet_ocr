#!/usr/bin/env python
# coding: utf-8

# In[1]:



# In[2]:


import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plt


# In[3]:


im_1_path = '/Users/abrahamkom/Groupe 3IL 📖/Test/folder/permis4.jpg'
im_2_path = '/Users/abrahamkom/Groupe 3IL 📖/Test/folder/PERMIS.jpg'
print(im_1_path)


# <h1 class="alert alert-success">Fonction de reconnaissance </h>

# In[4]:


def recognize_text(img_path):
    '''loads an image and recognizes text.'''
    
    reader = easyocr.Reader(['fr'], gpu = True)
    return reader.readtext(img_path,detail=0)


# In[ ]:





# In[5]:


result = recognize_text(im_1_path)


# In[6]:


print(result)


# In[46]:


import json


# In[53]:

# In[54]:


#print(data)


# In[60]:


personne = {"Contry" : result[1],
            "firstName" : result[3],
            "laastName" : result[4],
            "birthDate" : result[5],
            "birthPlace" : result[5],
            "issueDate" : result[6],
            "expiryDate" : result[8],
            "deliveredAutority" : "",
            "licenceNumlber" : result[9],
            "licenceCategory" : result[10],
            "mrzBand" : ""
           }

#personne


# In[ ]:




