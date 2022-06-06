# This is a sample Python script.

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import inter.CarteGrise.Formulaire1 as cgf
import inter.buttonTemplate as bt

x = "abc"


def upload_file(label):
    image_Path = filedialog.askopenfilename(initialdir='C:\\', filetypes=[("images files", "*.png; *.jpg; *.jpeg")])
    if image_Path:
        image = Image.open(image_Path)
        image.thumbnail((350, 450))
        image = ImageTk.PhotoImage(image)
        label.configure(image=image)
        label.image = image
        x=image_Path
        print(x)


def goToExtract(window, frame):
    frame.destroy()
    cgf.frameCGF(window)


def frameCG(window):
    #frame.destroy()
    frameCI1 = tk.Frame(window, height=2000, width=2000, border=2)
    frameCI1.place(relx=0, rely=0, relheight=1, relwidth=1)
    frameCI1.configure(relief='groove')
    frameCI1.configure(borderwidth="2")
    frameCI1.configure(relief="groove")

    label = Label(frameCI1)
    label.place(x=200, y=132, height=366, width=468)
    label.configure(activebackground="#0d0003")
    label.configure(activeforeground="white")
    label.configure(activeforeground="#000000")
    label.configure(background="#adadad")
    label.configure(compound='center')
    label.configure(disabledforeground="#000000")
    label.configure(font="-family {Segoe UI} -size 20")
    label.configure(foreground="#000000")
    label.configure(highlightbackground="#d9d9d9")
    label.configure(highlightcolor="black")
    label.configure(highlightthickness="3")

    ########button choisir 1
    btn = Button(frameCI1, command=lambda : upload_file(label))
    btn.place(x=44, y=80, height=34, width=67)
    btn.configure(activebackground="#ececec")
    btn.configure(activeforeground="#000000")
    btn.configure(background="#d9d9d9")
    btn.configure(compound='left')
    btn.configure(disabledforeground="#a3a3a3")
    btn.configure(foreground="#000000")
    btn.configure(highlightbackground="#d9d9d9")
    btn.configure(highlightcolor="black")
    btn.configure(pady="0")
    btn.configure(text='''choisir''')

    labelTitle = tk.Label(frameCI1)
    labelTitle.place(x=220, y=20, height=41, width=395)
    labelTitle.configure(activebackground="#f9f9f9")
    labelTitle.configure(activeforeground="black")
    labelTitle.configure(background="#d9d9d9")
    labelTitle.configure(compound='center')
    labelTitle.configure(disabledforeground="#a3a3a3")
    labelTitle.configure(font="-family {Imprint MT Shadow} -size 24")
    labelTitle.configure(foreground="#000000")
    labelTitle.configure(highlightbackground="#d9d9d9")
    labelTitle.configure(highlightcolor="black")
    labelTitle.configure(relief="solid")
    labelTitle.configure(text='''CARTE GRISE''')

    buttonExtract = tk.Button(frameCI1, command=lambda: goToExtract(window, frameCI1))
    buttonExtract.place(x=710, y=500, height=34, width=67)
    buttonExtract.configure(activebackground="#ececec")
    buttonExtract.configure(activeforeground="#000000")
    buttonExtract.configure(background="#d9d9d9")
    buttonExtract.configure(compound='right')
    buttonExtract.configure(cursor="fleur")
    buttonExtract.configure(disabledforeground="#a3a3a3")
    buttonExtract.configure(foreground="#000000")
    buttonExtract.configure(highlightbackground="#d9d9d9")
    buttonExtract.configure(highlightcolor="black")
    buttonExtract.configure(pady="0")
    buttonExtract.configure(text='''Extract''')

    bt.button_exit(frameCI1)
    bt.button_return(window, frameCI1)

    print(x)




