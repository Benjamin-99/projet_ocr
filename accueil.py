# This is a sample Python script.
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf

import PIL as P
from PIL import Image, ImageTk

home = Tk()

# Frame
home.geometry("210x160")

# Windows'title
home.title("Accueil")

# Font family
home_font = ('times', 12, 'bold')

# Title's page
l1 = tk.Label(home, text='Choix du type de fichier', width=30, font=home_font)
l1.pack()

fileChoice = StringVar()
rb1 = Radiobutton(home, text="Gray card", value='Carte_G', variable=fileChoice)
rb2 = Radiobutton(home, text="Id card     ", value='Carte_I', variable=fileChoice)
rb3 = Radiobutton(home, text="Passport  ", value='P', variable=fileChoice)
rb1.pack()
rb2.pack()
rb3.pack()

rb1.select()


def test_radio():
    home.destroy()
    import RectoVerso


cmd = Button(home, text="Ok", command=test_radio)
cmd.pack()

home.mainloop()
