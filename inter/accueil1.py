# This is a sample Python script.
import tkinter
import tkinter as tk
from tkinter import *
import inter.CarteGrise.CarteGrise1 as cg
import inter.CarteIdentite.CarteIdentite1 as ci
import  inter.permisdeconduire.PermisDeConduire1 as pc


# Function btn
print(cg.x)


def choice_btn(frame, fileChoice, window):
    choice = fileChoice.get()
    if choice == 1:
        frame.destroy()
        cg.frameCG(window)
    elif choice == 2:
        frame.destroy()
        ci.frameCI(window)
    elif choice == 3:
        frame.destroy()
        pc.framePCF(window)


def choice_interface(window):
    frame = tk.Frame(window, height=2000, width=2000, border=2)
    frame.place(relx=0, rely=0, relheight=1, relwidth=1)
    frame.configure(relief='groove')
    frame.configure(borderwidth="2")
    frame.configure(relief="groove")

    fileChoice = IntVar()
    rb1 = Radiobutton(frame, text="Gray card", value=1, variable=fileChoice)
    rb1.pack()
    rb2 = Radiobutton(frame, text="Id card", value=2, variable=fileChoice)
    rb2.pack()
    rb3 = Radiobutton(frame, text="Driver License", value=3, variable=fileChoice)
    rb3.pack()
    #rb1.select()
    cmd = Button(frame, text="Ok", command=lambda: choice_btn(frame, fileChoice,window))
    cmd.pack()



