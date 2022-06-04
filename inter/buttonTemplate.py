import tkinter as tk
from tkinter import *
import inter.accueil1 as ac


def return_home(window, frame):
    frame.destroy()
    ac.choice_interface(window)


def button_return(window, frame):
    buttonReturn = tk.Button(frame, command=lambda: return_home(window, frame))
    buttonReturn.place(x=44, y=500, height=34, width=67)
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


def button_exit(frame):
    buttonExit = tk.Button(frame, command=lambda: exit())
    buttonExit.place(x=780, y=500, height=34, width=67)
    buttonExit.configure(activebackground="#ececec")
    buttonExit.configure(activeforeground="#000000")
    buttonExit.configure(background="#d9d9d9")
    buttonExit.configure(compound='right')
    buttonExit.configure(disabledforeground="#a3a3a3")
    buttonExit.configure(foreground="#000000")
    buttonExit.configure(highlightbackground="#d9d9d9")
    buttonExit.configure(highlightcolor="black")
    buttonExit.configure(pady="0")
    buttonExit.configure(text='''Exit''')