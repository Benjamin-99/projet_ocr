import tkinter as tk
from tkinter import *
import inter.accueil1 as ac


window = tk.Tk()
ac.choice_interface(window)

window.title("Image Browser")
window.geometry("872x568+219+46")
window.minsize(120, 1)
window.maxsize(1370, 749)
window.resizable(0, 0)
window.title("Toplevel 0")
window.configure(background="#d9d9d9")
window.mainloop()