# This is a sample Python script.

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


def upload_file():
    image_Path = filedialog.askopenfilename(initialdir='C:\\', filetypes=[("png files", '.png')])
    image = Image.open(image_Path)
    image.thumbnail((350, 450))
    image = ImageTk.PhotoImage(image)
    label.configure(image=image)
    label.image = image


def return_home():
    root.destroy()
    import interfaces.accueil


root = Tk()

##################image recto
label = Label(root)
label.place(x=63, y=152, height=266, width=668)
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
btn = Button(root, command=upload_file)
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

labelTitle = tk.Label(root)
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

buttonReturn = tk.Button(root, command=lambda: return_home())
buttonReturn.place(x=44, y=470, height=34, width=67)
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

buttonExtract = tk.Button(root)
buttonExtract.place(x=700, y=470, height=34, width=67)
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

buttonExit = tk.Button(root, command=lambda: exit())
buttonExit.place(x=620, y=470, height=34, width=67)
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

root.title("Image Browser")
root.geometry("872x568+219+46")
root.minsize(120, 1)
root.maxsize(1370, 749)
root.resizable(0, 0)
root.title("Toplevel 0")
root.configure(background="#bebebe")

root.geometry("787x524+346+75")
root.minsize(120, 1)
root.maxsize(1370, 749)
root.resizable(1, 1)
root.title("Toplevel 0")
root.configure(background="#d9d9d9")
root.mainloop()
