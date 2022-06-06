# This is a sample Python script.
import tkinter
import tkinter as tk
from tkinter import *
import inter.CarteGrise.CarteGrise1 as cg
import inter.CarteIdentite.CarteIdentite1 as ci
import inter.permisdeconduire.PermisDeConduire1 as pc

global _img0

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
    frame = tk.Frame(window, height=1000, width=700, border=2)
    frame.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.98)
    frame.configure(relief='groove')
    frame.configure(borderwidth="2")

    TLabel1 = Label(frame)
    TLabel1.place(relx=-0.04, rely=0.252, height=410, width=607)
    TLabel1.configure(foreground="#000000")
    TLabel1.configure(font="TkDefaultFont")
    TLabel1.configure(relief="flat")
    TLabel1.configure(anchor='w')
    TLabel1.configure(justify='left')
    photo_location = "background.png"
    global _img0
    _img0 = tk.PhotoImage(file=photo_location)
    TLabel1.configure(image=_img0)
    TLabel1.configure(compound='left')

    frame2 = Frame(frame)
    frame2.place(relx=0.679, rely=0.409, relheight=0.225, relwidth=0.287)
    frame2.configure(relief='groove')
    frame2.configure(borderwidth="2")
    frame2.configure(relief="groove")

    label1 = tk.Label(frame)
    label1.place(relx=0.153, rely=0.012, height=71, width=590)
    label1.configure(anchor='w')
    label1.configure(disabledforeground="#a3a3a3")
    label1.configure(font="-family {Segoe UI} -size 28")
    label1.configure(foreground="#000000")

    label1.configure(activebackground="#f9f9f9")
    label1.configure(activeforeground="black")
    label1.configure(background="#d9d9d9")
    label1.configure(compound='center')
    label1.configure(font="-family {Imprint MT Shadow} -size 28")
    label1.configure(highlightbackground="#d9d9d9")
    label1.configure(highlightcolor="black")
    label1.configure(relief="solid")

    label1.configure(text='''BIENVENUE SUR EXTRACT ++''')

    label2 = tk.Label(frame)
    label2.place(relx=0.69, rely=0.34, height=31, width=224)
    label2.configure(anchor='w')
    label2.configure(compound='left')
    label2.configure(disabledforeground="#a3a3a3")
    label2.configure(foreground="#000000")
    label2.configure(text='''Quel document souhaitez vous extraire ?''')


    fileChoice = IntVar()
    rb1 = Radiobutton(frame2, text="Carte grise     ", value=1, variable=fileChoice)
    rb1.place(relx=0.7, rely=12, relwidth=0.9, relheight=0.8)
    rb1.pack()

    rb2 = Radiobutton(frame2, text="Carte d'identité     ", value=2, variable=fileChoice, compound='left')
    rb2.place(relx=0.7, rely=12, relwidth=0.404, relheight=0.0, height=21)
    rb2.pack()

    rb3 = Radiobutton(frame2, text="Permis de conduire", value=3, variable=fileChoice, compound='left')
    rb3.place(relx=0.7, rely=1, relwidth=0.608, relheight=0.0, height=21)
    rb3.pack()

    #rb1.select()
    cmd = Button(frame2, text="Ok", command=lambda: choice_btn(frame, fileChoice,window))
    cmd.place(relx=0.367, rely=0.814, height=24, width=57)
    cmd.pack()






   # style.map('TRadiobutton', background=[('selected', _bgcolor), ('active', _ana2color)])





