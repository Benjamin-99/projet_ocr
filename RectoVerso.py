# This is a sample Python script.

import img2pdf
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import PIL as P
from PIL import Image, ImageTk


def upload_file():
    image_Path = filedialog.askopenfilename(initialdir='C:\\', filetypes=[("png files", '.png')])
    image = Image.open(image_Path)
    image.thumbnail((350, 450))
    image = ImageTk.PhotoImage(image)
    label.configure(image=image)
    label.image = image
    label2.configure(text=image_Path)


def upload_file1():
    image_Path = filedialog.askopenfilename(initialdir='C:\\', filetypes=[("png files", '.png')])
    image = Image.open(image_Path)
    image.thumbnail((350, 450))
    image = ImageTk.PhotoImage(image)
    label1.configure(image=image)
    label1.image = image


root = Tk()

frn = Frame(root)
frn.pack(side=TOP, padx=15, pady=15)

frn1 = Frame(root)
frn1.pack(side=BOTTOM, padx=0, pady=0)

btn = Button(frn1, text="Extraire", command=upload_file1)
btn.pack(side=tk.LEFT)

btn2 = Button(frn1, text="Exit", command=lambda: exit())
btn2.pack(side=tk.RIGHT, padx=10)

frn2 = Frame(root)
frn2.pack(side=LEFT, padx=10, pady=10)
label = Label(frn2)
label.pack(side=tk.LEFT)

btn = Button(frn, text="Choisir1", command=upload_file)
btn.pack(side=tk.LEFT)

label2 = Label(frn)
label2.pack(side=tk.LEFT)

frn3 = Frame(root)
frn3.pack(side=RIGHT, padx=10, pady=10)
label1 = Label(frn3)
label1.pack(side=tk.RIGHT)
btn3 = Button(frn, text="Choisir2", command=upload_file1)
btn3.pack(side=tk.RIGHT)

root.title("Image Browser")
root.geometry("800x550")


root.mainloop()


