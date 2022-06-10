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
    label2.configure(text=image_Path)


def upload_file1():
    image_Path = filedialog.askopenfilename(initialdir='C:\\', filetypes=[("png files", '.png')])
    image = Image.open(image_Path)
    image.thumbnail((350, 450))
    image = ImageTk.PhotoImage(image)
    label1.configure(image=image)
    label1.image = image
    labelPath2.configure(text=image_Path)

def return_home():
    rootFPC.destroy()
    import interfaces.accueil


rootFPC = tk.Tk()

##################image recto
label = Label(rootFPC)
label.place(x=44, y=152, height=266, width=368)
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
btn = Button(rootFPC, command=upload_file)
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

#################### button choice 2 ################################
btn3 = Button(rootFPC, command=upload_file1)
btn3.place(x=460, y=80, height=34, width=67)
btn3.configure(activebackground="#ececec")
btn3.configure(activeforeground="#000000")
btn3.configure(background="#d9d9d9")
btn3.configure(compound='right')
btn3.configure(disabledforeground="#a3a3a3")
btn3.configure(foreground="#000000")
btn3.configure(highlightbackground="#d9d9d9")
btn3.configure(highlightcolor="black")
btn3.configure(pady="0")
btn3.configure(text='''choisir2''')

###################label choice 1
label2 = Label(rootFPC)
label2.place(x=140, y=90, height=27, width=268)
label2.configure(activebackground="#f9f9f9")
label2.configure(activeforeground="black")
label2.configure(anchor='w')
label2.configure(background="#bebebe")
label2.configure(compound='left')
label2.configure(disabledforeground="#a3a3a3")
label2.configure(foreground="#000000")
label2.configure(highlightbackground="#d9d9d9")
label2.configure(highlightcolor="black")

#######img verso
label1 = Label(rootFPC)
label1.place(x=460, y=150, height=266, width=369)
label1.configure(activebackground="#0d0003")
label1.configure(activeforeground="white")
label1.configure(activeforeground="#000000")
label1.configure(background="#adadad")
label1.configure(compound='center')
label1.configure(disabledforeground="#000000")
label1.configure(font="-family {Segoe UI} -size 20")
label1.configure(foreground="#000000")
label1.configure(highlightbackground="#d9d9d9")
label1.configure(highlightcolor="black")
label1.configure(highlightthickness="3")

#################label choice 2
label3 = Label(rootFPC)
label3.place(x=540, y=86, height=27, width=368)
label3.configure(activebackground="#f9f9f9")
label3.configure(activeforeground="black")
label3.configure(anchor='w')
label3.configure(background="#bebebe")
label3.configure(compound='left')
label3.configure(disabledforeground="#a3a3a3")
label3.configure(foreground="#000000")
label3.configure(highlightbackground="#d9d9d9")
label3.configure(highlightcolor="black")

labelTitle = tk.Label(rootFPC)
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
labelTitle.configure(text='''PERMIS DE CONDUIRE''')

buttonReturn = tk.Button(rootFPC, command=lambda: return_home())
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

buttonExtract = tk.Button(rootFPC)
buttonExtract.place(x=760, y=500, height=34, width=67)
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

buttonExit = tk.Button(rootFPC, command=lambda: exit())
buttonExit.place(x=660, y=500, height=34, width=67)
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

labelPath2 = tk.Label(rootFPC)
labelPath2.place(x=560, y=86, height=27, width=268)
labelPath2.configure(activebackground="#f9f9f9")
labelPath2.configure(activeforeground="black")
labelPath2.configure(anchor='w')
labelPath2.configure(background="#bebebe")
labelPath2.configure(compound='left')
labelPath2.configure(disabledforeground="#a3a3a3")
labelPath2.configure(foreground="#000000")
labelPath2.configure(highlightbackground="#d9d9d9")
labelPath2.configure(highlightcolor="black")

rootFPC.title("Image Browser")
rootFPC.geometry("872x568+219+46")
rootFPC.minsize(120, 1)
rootFPC.maxsize(1370, 749)
rootFPC.resizable(0, 0)
rootFPC.title("Toplevel 0")
rootFPC.configure(background="#bebebe")



rootFPC.mainloop()


