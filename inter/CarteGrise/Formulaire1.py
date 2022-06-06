#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 18, 2022 04:09:50 PM CEST  platform: Windows NT

import sys

import tkinter as tk
from tkinter import *
import inter.CarteGrise.CarteGrise1 as cg

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9'  # X11 color: 'gray85'
_ana1color = '#d9d9d9'  # X11 color: 'gray85'
_ana2color = '#ececec'  # Closest X11 color: 'gray92'


def return_cg(window, frame):
    frame.destroy()
    cg.frameCG(window)


def frameCGF(window):
    rootFCG = tk.Frame(window, height=2000, width=2000, border=2)
    rootFCG.place(relx=0, rely=0, relheight=1, relwidth=1)
    rootFCG.configure(relief='groove')
    rootFCG.configure(borderwidth="2")
    rootFCG.configure(relief="groove")
    rootFCG.configure(highlightcolor="#d9d9d9", background="#d9d9d9")

    TLabelImage = Label(rootFCG)
    TLabelImage.place(relx=-0.04, rely=0.02, height=210, width=307)
    TLabelImage.configure(foreground="#000000")
    TLabelImage.configure(font="TkDefaultFont")
    TLabelImage.configure(relief="flat")
    TLabelImage.configure(anchor='w')
    TLabelImage.configure(justify='left')
    photo_location = "background.png"
    global _img0
    _img0 = tk.PhotoImage(file=photo_location)
    TLabelImage.configure(image=_img0)
    TLabelImage.configure(compound='left')

######Civilité#####

    entryCivilite = tk.Entry(rootFCG)
    entryCivilite.place(relx=0.14, rely=0.439, height=26, relwidth=0.335)
    entryCivilite.configure(background="white")
    #EntryCivilite.configure(disabledforeground="#a3a3a3")
    entryCivilite.configure(font="TkFixedFont")
    entryCivilite.configure(foreground="#000000")
    #EntryCivilite.configure(highlightbackground="#d9d9d9")
    entryCivilite.configure(highlightcolor="black")
    entryCivilite.configure(insertbackground="black")
    #EntryCivilite.configure(selectbackground="blue")
    entryCivilite.configure(selectforeground="white")

    labelCivilite = tk.Label(rootFCG)
    labelCivilite.place(relx=0.02, rely=0.439, height=25, width=49)
    labelCivilite.configure(activebackground="#f9f9f9")
    labelCivilite.configure(activeforeground="black")
    labelCivilite.configure(anchor='w')
    labelCivilite.configure(background="#d9d9d9")
    labelCivilite.configure(compound='left')
    labelCivilite.configure(disabledforeground="#a3a3a3")
    labelCivilite.configure(foreground="#000000")
    labelCivilite.configure(highlightbackground="#d9d9d9")
    labelCivilite.configure(highlightcolor="black")
    labelCivilite.configure(text='''Civilité : ''')

######Nom######

    entryNom = tk.Entry(rootFCG)
    entryNom.place(relx=0.141, rely=0.515, height=26, relwidth=0.335)
    entryNom.configure(background="white")
    entryNom.configure(disabledforeground="#a3a3a3")
    entryNom.configure(font="TkFixedFont")
    entryNom.configure(foreground="#000000")
    entryNom.configure(highlightbackground="#d9d9d9")
    entryNom.configure(highlightcolor="black")
    entryNom.configure(insertbackground="black")
    entryNom.configure(selectbackground="blue")
    entryNom.configure(selectforeground="white")

    labelNom = tk.Label(rootFCG)
    labelNom.place(relx=0.022, rely=0.515, height=25, width=48)
    labelNom.configure(activebackground="#f9f9f9")
    labelNom.configure(activeforeground="black")
    labelNom.configure(background="#d9d9d9")
    labelNom.configure(compound='left')
    labelNom.configure(disabledforeground="#a3a3a3")
    labelNom.configure(foreground="#000000")
    labelNom.configure(highlightbackground="#d9d9d9")
    labelNom.configure(highlightcolor="black")
    labelNom.configure(text='''Nom(s) : ''')

#####Prénom#####

    entryPrenom = tk.Entry(rootFCG)
    entryPrenom.place(relx=0.141, rely=0.668, height=26, relwidth=0.335)
    entryPrenom.configure(background="white")
    entryPrenom.configure(disabledforeground="#a3a3a3")
    entryPrenom.configure(font="TkFixedFont")
    entryPrenom.configure(foreground="#000000")
    entryPrenom.configure(highlightbackground="#d9d9d9")
    entryPrenom.configure(highlightcolor="black")
    entryPrenom.configure(insertbackground="black")
    entryPrenom.configure(selectbackground="blue")
    entryPrenom.configure(selectforeground="white")

    labelPrenom = tk.Label(rootFCG)
    labelPrenom.place(relx=0.02, rely=0.677, height=25, width=63)
    labelPrenom.configure(activebackground="#f9f9f9")
    labelPrenom.configure(activeforeground="black")
    labelPrenom.configure(background="#d9d9d9")
    labelPrenom.configure(compound='left')
    labelPrenom.configure(disabledforeground="#a3a3a3")
    labelPrenom.configure(foreground="#000000")
    labelPrenom.configure(highlightbackground="#d9d9d9")
    labelPrenom.configure(highlightcolor="black")
    labelPrenom.configure(text='''Prénom(s) : ''')

#####Nom d'usage####"

    entryNomUsage = tk.Entry(rootFCG)
    entryNomUsage.place(relx=0.141, rely=0.591, height=26, relwidth=0.335)
    entryNomUsage.configure(background="white")
    entryNomUsage.configure(disabledforeground="#a3a3a3")
    entryNomUsage.configure(font="TkFixedFont")
    entryNomUsage.configure(foreground="#000000")
    entryNomUsage.configure(highlightbackground="#d9d9d9")
    entryNomUsage.configure(highlightcolor="black")
    entryNomUsage.configure(insertbackground="black")
    entryNomUsage.configure(selectbackground="blue")
    entryNomUsage.configure(selectforeground="white")

    labelNomUsage = tk.Label(rootFCG)
    labelNomUsage.place(relx=0.02, rely=0.589, height=25, width=88)
    labelNomUsage.configure(activebackground="#f9f9f9")
    labelNomUsage.configure(activeforeground="black")
    labelNomUsage.configure(background="#d9d9d9")
    labelNomUsage.configure(compound='left')
    labelNomUsage.configure(disabledforeground="#a3a3a3")
    labelNomUsage.configure(foreground="#000000")
    labelNomUsage.configure(highlightbackground="#d9d9d9")
    labelNomUsage.configure(highlightcolor="black")
    labelNomUsage.configure(text='''Nom(s) d'usage:''')

####Date de naissance

    labelDateNaiss = tk.Label(rootFCG)
    labelDateNaiss.place(relx=0.02, rely=0.742, height=36, width=51)
    labelDateNaiss.configure(activebackground="#f9f9f9")
    labelDateNaiss.configure(activeforeground="black")
    labelDateNaiss.configure(anchor='w')
    labelDateNaiss.configure(background="#d9d9d9")
    labelDateNaiss.configure(compound='left')
    labelDateNaiss.configure(disabledforeground="#a3a3a3")
    labelDateNaiss.configure(foreground="#000000")
    labelDateNaiss.configure(highlightbackground="#d9d9d9")
    labelDateNaiss.configure(highlightcolor="black")
    labelDateNaiss.configure(text='''Né(e) le : ''')

    entryDateNaiss = tk.Entry(rootFCG)
    entryDateNaiss.place(relx=0.14, rely=0.744, height=26, relwidth=0.145)
    entryDateNaiss.configure(background="white")
    entryDateNaiss.configure(disabledforeground="#a3a3a3")
    entryDateNaiss.configure(font="TkFixedFont")
    entryDateNaiss.configure(foreground="#000000")
    entryDateNaiss.configure(highlightbackground="#d9d9d9")
    entryDateNaiss.configure(highlightcolor="black")
    entryDateNaiss.configure(insertbackground="black")
    entryDateNaiss.configure(selectbackground="blue")
    entryDateNaiss.configure(selectforeground="white")

#### Lieu de naissance ####

    labelLieuNaiss = tk.Label(rootFCG)
    labelLieuNaiss.place(relx=0.288, rely=0.733, height=36, width=8)
    labelLieuNaiss.configure(activebackground="#f9f9f9")
    labelLieuNaiss.configure(activeforeground="black")
    labelLieuNaiss.configure(anchor='w')
    labelLieuNaiss.configure(background="#d9d9d9")
    labelLieuNaiss.configure(compound='left')
    labelLieuNaiss.configure(disabledforeground="#a3a3a3")
    labelLieuNaiss.configure(foreground="#000000")
    labelLieuNaiss.configure(highlightbackground="#d9d9d9")
    labelLieuNaiss.configure(highlightcolor="black")
    labelLieuNaiss.configure(text='''à''')

    entryLieuNaiss = tk.Entry(rootFCG)
    entryLieuNaiss.place(relx=0.309, rely=0.742, height=26, relwidth=0.17)
    entryLieuNaiss.configure(background="white")
    entryLieuNaiss.configure(disabledforeground="#a3a3a3")
    entryLieuNaiss.configure(font="TkFixedFont")
    entryLieuNaiss.configure(foreground="#000000")
    entryLieuNaiss.configure(highlightbackground="#d9d9d9")
    entryLieuNaiss.configure(highlightcolor="black")
    entryLieuNaiss.configure(insertbackground="black")
    entryLieuNaiss.configure(selectbackground="blue")
    entryLieuNaiss.configure(selectforeground="white")

### Date d'obtention ####

    labelDateObtention = tk.Label(rootFCG)
    labelDateObtention.place(relx=0.02, rely=0.828, height=25, width=63)
    labelDateObtention.configure(activebackground="#f9f9f9")
    labelDateObtention.configure(activeforeground="black")
    labelDateObtention.configure(anchor='w')
    labelDateObtention.configure(background="#d9d9d9")
    labelDateObtention.configure(compound='left')
    labelDateObtention.configure(disabledforeground="#a3a3a3")
    labelDateObtention.configure(foreground="#000000")
    labelDateObtention.configure(highlightbackground="#d9d9d9")
    labelDateObtention.configure(highlightcolor="black")
    labelDateObtention.configure(text='''Etabli le : ''')

    entryDateObtention = tk.Entry(rootFCG)
    entryDateObtention.place(relx=0.14, rely=0.821, height=26, relwidth=0.145)
    entryDateObtention.configure(background="white")
    entryDateObtention.configure(cursor="fleur")
    entryDateObtention.configure(disabledforeground="#a3a3a3")
    entryDateObtention.configure(font="TkFixedFont")
    entryDateObtention.configure(foreground="#000000")
    entryDateObtention.configure(highlightbackground="#d9d9d9")
    entryDateObtention.configure(highlightcolor="black")
    entryDateObtention.configure(insertbackground="black")
    entryDateObtention.configure(selectbackground="blue")
    entryDateObtention.configure(selectforeground="white")

#### Lieu d'obtention ####

    labelLieuObtention = tk.Label(rootFCG)
    labelLieuObtention.place(relx=0.288, rely=0.828, height=25, width=63)
    labelLieuObtention.configure(activebackground="#f9f9f9")
    labelLieuObtention.configure(activeforeground="black")
    labelLieuObtention.configure(anchor='w')
    labelLieuObtention.configure(background="#d9d9d9")
    labelLieuObtention.configure(compound='left')
    labelLieuObtention.configure(disabledforeground="#a3a3a3")
    labelLieuObtention.configure(foreground="#000000")
    labelLieuObtention.configure(highlightbackground="#d9d9d9")
    labelLieuObtention.configure(highlightcolor="black")
    labelLieuObtention.configure(text='''à  ''')

    entryLieuObtention = tk.Entry(rootFCG)
    entryLieuObtention.place(relx=0.309, rely=0.821, height=26, relwidth=0.17)
    entryLieuObtention.configure(background="white")
    entryLieuObtention.configure(cursor="fleur")
    entryLieuObtention.configure(disabledforeground="#a3a3a3")
    entryLieuObtention.configure(font="TkFixedFont")
    entryLieuObtention.configure(foreground="#000000")
    entryLieuObtention.configure(highlightbackground="#d9d9d9")
    entryLieuObtention.configure(highlightcolor="black")
    entryLieuObtention.configure(insertbackground="black")
    entryLieuObtention.configure(selectbackground="blue")
    entryLieuObtention.configure(selectforeground="white")

    #TSeparator1 = tk.SEPARATOR(rootFCG)
    #TSeparator1.place(relx=0.496, rely=0.019,  relheight=0.878)
    #TSeparator1.configure(orient="vertical")

### Immatriculation ####

    labelImmatriculation = tk.Label(rootFCG)
    labelImmatriculation.place(relx=0.500, rely=0.039, height=25, width=94)
    labelImmatriculation.configure(activebackground="#f9f9f9")
    labelImmatriculation.configure(activeforeground="black")
    labelImmatriculation.configure(anchor='w')
    labelImmatriculation.configure(background="#d9d9d9")
    labelImmatriculation.configure(compound='left')
    labelImmatriculation.configure(disabledforeground="#a3a3a3")
    labelImmatriculation.configure(foreground="#000000")
    labelImmatriculation.configure(highlightbackground="#d9d9d9")
    labelImmatriculation.configure(highlightcolor="black")
    labelImmatriculation.configure(text='''Immatriculation : ''')

    entryImmatriculation = tk.Entry(rootFCG)
    entryImmatriculation.place(relx=0.673, rely=0.038, height=26, relwidth=0.297)
    entryImmatriculation.configure(background="white")
    entryImmatriculation.configure(disabledforeground="#a3a3a3")
    entryImmatriculation.configure(font="TkFixedFont")
    entryImmatriculation.configure(foreground="#000000")
    entryImmatriculation.configure(highlightbackground="#d9d9d9")
    entryImmatriculation.configure(highlightcolor="black")
    entryImmatriculation.configure(insertbackground="black")
    entryImmatriculation.configure(selectbackground="blue")
    entryImmatriculation.configure(selectforeground="white")

#### Version ####

    labelVersion = tk.Label(rootFCG)
    labelVersion.place(relx=0.500, rely=0.212, height=25, width=65)
    labelVersion.configure(activebackground="#f9f9f9")
    labelVersion.configure(activeforeground="black")
    labelVersion.configure(anchor='w')
    labelVersion.configure(background="#d9d9d9")
    labelVersion.configure(compound='left')
    labelVersion.configure(disabledforeground="#a3a3a3")
    labelVersion.configure(foreground="#000000")
    labelVersion.configure(highlightbackground="#d9d9d9")
    labelVersion.configure(highlightcolor="black")
    labelVersion.configure(text='''Version : ''')

    entryVersion = tk.Entry(rootFCG)
    entryVersion.place(relx=0.673, rely=0.118, height=26, relwidth=0.297)
    entryVersion.configure(background="white")
    entryVersion.configure(disabledforeground="#a3a3a3")
    entryVersion.configure(font="TkFixedFont")
    entryVersion.configure(foreground="#000000")
    entryVersion.configure(highlightbackground="#d9d9d9")
    entryVersion.configure(highlightcolor="black")
    entryVersion.configure(insertbackground="black")
    entryVersion.configure(selectbackground="blue")
    entryVersion.configure(selectforeground="white")

#### Marque ####

    labelMarque = tk.Label(rootFCG)
    labelMarque.place(relx=0.500, rely=0.122, height=36, width=69)
    labelMarque.configure(activebackground="#f9f9f9")
    labelMarque.configure(activeforeground="black")
    labelMarque.configure(anchor='w')
    labelMarque.configure(background="#d9d9d9")
    labelMarque.configure(compound='left')
    labelMarque.configure(disabledforeground="#a3a3a3")
    labelMarque.configure(foreground="#000000")
    labelMarque.configure(highlightbackground="#d9d9d9")
    labelMarque.configure(highlightcolor="black")
    labelMarque.configure(text='''Marque : ''')

    labelCategorie = tk.Label(rootFCG)
    labelCategorie.place(relx=0.500, rely=0.2, height=36, width=69)
    labelCategorie.configure(activebackground="#f9f9f9")
    labelCategorie.configure(activeforeground="black")
    labelCategorie.configure(anchor='w')
    labelCategorie.configure(background="#d9d9d9")
    labelCategorie.configure(compound='left')
    labelCategorie.configure(disabledforeground="#a3a3a3")
    labelCategorie.configure(foreground="#000000")
    labelCategorie.configure(highlightbackground="#d9d9d9")
    labelCategorie.configure(highlightcolor="black")
    labelCategorie.configure(text='''Marque : ''')

    EntryCategorie = tk.Entry(rootFCG)
    EntryCategorie.place(relx=0.673, rely=0.2, height=26, relwidth=0.297)
    EntryCategorie.configure(background="white")
    EntryCategorie.configure(cursor="fleur")
    EntryCategorie.configure(disabledforeground="#a3a3a3")
    EntryCategorie.configure(font="TkFixedFont")
    EntryCategorie.configure(foreground="#000000")
    EntryCategorie.configure(highlightbackground="#d9d9d9")
    EntryCategorie.configure(highlightcolor="black")
    EntryCategorie.configure(insertbackground="black")
    EntryCategorie.configure(selectbackground="blue")
    EntryCategorie.configure(selectforeground="white")

    #menubar = tk.Menu(rootFCG,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
    #rootFCG.configure(menu = menubar)

##### Code d'identification ####

    labelCodeId = tk.Label(rootFCG)
    labelCodeId.place(relx=0.500, rely=0.754, height=25, width=126)
    labelCodeId.configure(activebackground="#f9f9f9")
    labelCodeId.configure(activeforeground="black")
    labelCodeId.configure(anchor='w')
    labelCodeId.configure(background="#d9d9d9")
    labelCodeId.configure(compound='left')
    labelCodeId.configure(disabledforeground="#a3a3a3")
    labelCodeId.configure(foreground="#000000")
    labelCodeId.configure(highlightbackground="#d9d9d9")
    labelCodeId.configure(highlightcolor="black")
    labelCodeId.configure(text='''Code d'indentification : ''')

##### Genre national ####

    labelGenreNat = tk.Label(rootFCG)
    labelGenreNat.place(relx=0.500, rely=0.445, height=35, width=92)
    labelGenreNat.configure(activebackground="#f9f9f9")
    labelGenreNat.configure(activeforeground="black")
    labelGenreNat.configure(anchor='w')
    labelGenreNat.configure(background="#d9d9d9")
    labelGenreNat.configure(compound='left')
    labelGenreNat.configure(disabledforeground="#a3a3a3")
    labelGenreNat.configure(foreground="#000000")
    labelGenreNat.configure(highlightbackground="#d9d9d9")
    labelGenreNat.configure(highlightcolor="black")
    labelGenreNat.configure(text='''Genre national : ''')

    entryGenreNat = tk.Entry(rootFCG)
    entryGenreNat.place(relx=0.673, rely=0.363, height=26, relwidth=0.297)
    entryGenreNat.configure(background="white")
    entryGenreNat.configure(disabledforeground="#a3a3a3")
    entryGenreNat.configure(font="TkFixedFont")
    entryGenreNat.configure(foreground="#000000")
    entryGenreNat.configure(highlightbackground="#d9d9d9")
    entryGenreNat.configure(highlightcolor="black")
    entryGenreNat.configure(insertbackground="black")
    entryGenreNat.configure(selectbackground="blue")
    entryGenreNat.configure(selectforeground="white")

#### Catégorie #####

    labelCategorie = tk.Label(rootFCG)
    labelCategorie.place(relx=0.500, rely=0.376, height=25, width=62)
    labelCategorie.configure(activebackground="#f9f9f9")
    labelCategorie.configure(activeforeground="black")
    labelCategorie.configure(anchor='w')
    labelCategorie.configure(background="#d9d9d9")
    labelCategorie.configure(compound='left')
    labelCategorie.configure(disabledforeground="#a3a3a3")
    labelCategorie.configure(foreground="#000000")
    labelCategorie.configure(highlightbackground="#d9d9d9")
    labelCategorie.configure(highlightcolor="black")
    labelCategorie.configure(text='''Catégorie : ''')

#### Carrosserie ####

    labelCarrosserie = tk.Label(rootFCG)
    labelCarrosserie.place(relx=0.500, rely=0.595, height=35 , width=63)
    labelCarrosserie.configure(activebackground="#f9f9f9")
    labelCarrosserie.configure(activeforeground="black")
    labelCarrosserie.configure(anchor='w')
    labelCarrosserie.configure(background="#d9d9d9")
    labelCarrosserie.configure(compound='left')
    labelCarrosserie.configure(disabledforeground="#a3a3a3")
    labelCarrosserie.configure(foreground="#000000")
    labelCarrosserie.configure(highlightbackground="#d9d9d9")
    labelCarrosserie.configure(highlightcolor="black")
    labelCategorie.configure(text='''Carrosserie : ''')



##### Cylindre #####

    labelCylindre = tk.Label(rootFCG)
    labelCylindre.place(relx=0.500, rely=0.683, height=25 , width=62)
    labelCylindre.configure(activebackground="#f9f9f9")
    labelCylindre.configure(activeforeground="black")
    labelCylindre.configure(anchor='w')
    labelCylindre.configure(background="#d9d9d9")
    labelCylindre.configure(compound='left')
    labelCylindre.configure(disabledforeground="#a3a3a3")
    labelCylindre.configure(foreground="#000000")
    labelCylindre.configure(highlightbackground="#d9d9d9")
    labelCylindre.configure(highlightcolor="black")
    labelCylindre.configure(text='''Cylindre : ''')

##### Type de carburant #####

    labelTypeCarburant = tk.Label(rootFCG)
    labelTypeCarburant.place(relx=0.500, rely=0.527, height=25, width=112)
    labelTypeCarburant.configure(activebackground="#f9f9f9")
    labelTypeCarburant.configure(activeforeground="black")
    labelTypeCarburant.configure(anchor='w')
    labelTypeCarburant.configure(background="#d9d9d9")
    labelTypeCarburant.configure(compound='left')
    labelTypeCarburant.configure(disabledforeground="#a3a3a3")
    labelTypeCarburant.configure(foreground="#000000")
    labelTypeCarburant.configure(highlightbackground="#d9d9d9")
    labelTypeCarburant.configure(highlightcolor="black")
    labelTypeCarburant.configure(text='''Type de carburant : ''')

##### Date de visite technique #####

    labelVisiteTech = tk.Label(rootFCG)
    labelVisiteTech.place(relx=0.500, rely=0.826, height=25, width=122)
    labelVisiteTech.configure(activebackground="#f9f9f9")
    labelVisiteTech.configure(activeforeground="black")
    labelVisiteTech.configure(anchor='w')
    labelVisiteTech.configure(background="#d9d9d9")
    labelVisiteTech.configure(compound='left')
    labelVisiteTech.configure(disabledforeground="#a3a3a3")
    labelVisiteTech.configure(foreground="#000000")
    labelVisiteTech.configure(highlightbackground="#d9d9d9")
    labelVisiteTech.configure(highlightcolor="black")
    labelVisiteTech.configure(text='''Date visite technique : ''')

##### Puissance #####

    labelPuissance = tk.Label(rootFCG)
    labelPuissance.place(relx=0.500, rely=0.3, height=25 , width=62)
    labelPuissance.configure(activebackground="#f9f9f9")
    labelPuissance.configure(activeforeground="black")
    labelPuissance.configure(anchor='w')
    labelPuissance.configure(background="#d9d9d9")
    labelPuissance.configure(compound='left')
    labelPuissance.configure(disabledforeground="#a3a3a3")
    labelPuissance.configure(foreground="#000000")
    labelPuissance.configure(highlightbackground="#d9d9d9")
    labelPuissance.configure(highlightcolor="black")
    labelPuissance.configure(text='''Puissance : ''')



    EntryPuissance = tk.Entry(rootFCG)
    EntryPuissance.place(relx=0.673, rely=0.286, height=26 , relwidth=0.297)
    EntryPuissance.configure(background="white")
    EntryPuissance.configure(disabledforeground="#a3a3a3")
    EntryPuissance.configure(font="TkFixedFont")
    EntryPuissance.configure(foreground="#000000")
    EntryPuissance.configure(highlightbackground="#d9d9d9")
    EntryPuissance.configure(highlightcolor="black")
    EntryPuissance.configure(insertbackground="black")
    EntryPuissance.configure(selectbackground="blue")
    EntryPuissance.configure(selectforeground="white")



    EntryGenreNational = tk.Entry(rootFCG)
    EntryGenreNational.place(relx=0.673, rely=0.439, height=26, relwidth=0.297)
    EntryGenreNational.configure(background="white")
    EntryGenreNational.configure(disabledforeground="#a3a3a3")
    EntryGenreNational.configure(font="TkFixedFont")
    EntryGenreNational.configure(foreground="#000000")
    EntryGenreNational.configure(highlightbackground="#d9d9d9")
    EntryGenreNational.configure(highlightcolor="black")
    EntryGenreNational.configure(insertbackground="black")
    EntryGenreNational.configure(selectbackground="blue")
    EntryGenreNational.configure(selectforeground="white")

    EntryTypeCarburant = tk.Entry(rootFCG)
    EntryTypeCarburant.place(relx=0.673, rely=0.515, height=26 , relwidth=0.297)
    EntryTypeCarburant.configure(background="white")
    EntryTypeCarburant.configure(disabledforeground="#a3a3a3")
    EntryTypeCarburant.configure(font="TkFixedFont")
    EntryTypeCarburant.configure(foreground="#000000")
    EntryTypeCarburant.configure(highlightbackground="#d9d9d9")
    EntryTypeCarburant.configure(highlightcolor="black")
    EntryTypeCarburant.configure(insertbackground="black")
    EntryTypeCarburant.configure(selectbackground="blue")
    EntryTypeCarburant.configure(selectforeground="white")

    Entry1_2_4 = tk.Entry(rootFCG)
    Entry1_2_4.place(relx=0.673, rely=0.592, height=26, relwidth=0.297)
    Entry1_2_4.configure(background="white")
    Entry1_2_4.configure(disabledforeground="#a3a3a3")
    Entry1_2_4.configure(font="TkFixedFont")
    Entry1_2_4.configure(foreground="#000000")
    Entry1_2_4.configure(highlightbackground="#d9d9d9")
    Entry1_2_4.configure(highlightcolor="black")
    Entry1_2_4.configure(insertbackground="black")
    Entry1_2_4.configure(selectbackground="blue")
    Entry1_2_4.configure(selectforeground="white")

    EntryCylindre = tk.Entry(rootFCG)
    EntryCylindre.place(relx=0.673, rely=0.668, height=26 , relwidth=0.297)
    EntryCylindre.configure(background="white")
    EntryCylindre.configure(cursor="fleur")
    EntryCylindre.configure(disabledforeground="#a3a3a3")
    EntryCylindre.configure(font="TkFixedFont")
    EntryCylindre.configure(foreground="#000000")
    EntryCylindre.configure(highlightbackground="#d9d9d9")
    EntryCylindre.configure(highlightcolor="black")
    EntryCylindre.configure(insertbackground="black")
    EntryCylindre.configure(selectbackground="blue")
    EntryCylindre.configure(selectforeground="white")

    EntryCodeIdentification = tk.Entry(rootFCG)
    EntryCodeIdentification.place(relx=0.673, rely=0.744, height=26, relwidth=0.297)
    EntryCodeIdentification.configure(background="white")
    EntryCodeIdentification.configure(disabledforeground="#a3a3a3")
    EntryCodeIdentification.configure(font="TkFixedFont")
    EntryCodeIdentification.configure(foreground="#000000")
    EntryCodeIdentification.configure(highlightbackground="#d9d9d9")
    EntryCodeIdentification.configure(highlightcolor="black")
    EntryCodeIdentification.configure(insertbackground="black")
    EntryCodeIdentification.configure(selectbackground="blue")
    EntryCodeIdentification.configure(selectforeground="white")

    EntryDateVisiteTech = tk.Entry(rootFCG)
    EntryDateVisiteTech.place(relx=0.673, rely=0.821, height=26, relwidth=0.297)
    EntryDateVisiteTech.configure(background="white")
    EntryDateVisiteTech.configure(disabledforeground="#a3a3a3")
    EntryDateVisiteTech.configure(font="TkFixedFont")
    EntryDateVisiteTech.configure(foreground="#000000")
    EntryDateVisiteTech.configure(highlightbackground="#d9d9d9")
    EntryDateVisiteTech.configure(highlightcolor="black")
    EntryDateVisiteTech.configure(insertbackground="black")
    EntryDateVisiteTech.configure(selectbackground="blue")
    EntryDateVisiteTech.configure(selectforeground="white")


    buttonLoadData = tk.Button(rootFCG)
    buttonLoadData.place(x=708, y=509, height=34, width=67)
    buttonLoadData.configure(activebackground="#ececec")
    buttonLoadData.configure(activeforeground="#000000")
    buttonLoadData.configure(background="#d9d9d9")
    buttonLoadData.configure(compound='left')
    buttonLoadData.configure(disabledforeground="#a3a3a3")
    buttonLoadData.configure(foreground="#000000")
    buttonLoadData.configure(highlightbackground="#d9d9d9")
    buttonLoadData.configure(highlightcolor="black")
    buttonLoadData.configure(pady="0")
    buttonLoadData.configure(text='''Enregistrer''')

    buttonExit = tk.Button(rootFCG, command=lambda: exit())
    buttonExit.place(x=780, y=509, height=34, width=67)
    buttonExit.configure(activeforeground="#000000")
    buttonExit.configure(background="#d9d9d9")
    buttonExit.configure(compound='left')
    buttonExit.configure(disabledforeground="#a3a3a3")
    buttonExit.configure(foreground="#000000")
    buttonExit.configure(highlightbackground="#d9d9d9")
    buttonExit.configure(highlightcolor="black")
    buttonExit.configure(pady="0")
    buttonExit.configure(text='''Sortir''')

    buttonReturn = tk.Button(rootFCG, command=lambda : return_cg(window, rootFCG))
    buttonReturn.place(x=44, y=509, height=34, width=67)
    buttonReturn.configure(activebackground="#ececec")
    buttonReturn.configure(activeforeground="#000000")
    buttonReturn.configure(background="#d9d9d9")
    buttonReturn.configure(compound='right')
    buttonReturn.configure(cursor="fleur")
    buttonReturn.configure(disabledforeground="#a3a3a3")
    buttonReturn.configure(foreground="#000000")
    buttonReturn.configure(highlightbackground="#d9d9d9")
    buttonReturn.configure(highlightcolor="black")
    buttonReturn.configure(pady="0")
    buttonReturn.configure(text='''Return''')

