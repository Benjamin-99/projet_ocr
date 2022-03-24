from tkinter import *

fenetre = Tk()
fenetre.geometry('400x400')
fenetre.title('Interface - Projet OCR')
fenetre['bg'] = 'red'
fenetre.resizable(height=False, width=False)

photo = PhotoImage(file='permis4 - Copie.gif')
label = Label(fenetre, image=photo)
label.pack()


fenetre.mainloop()
"""
from tkinter import *
from tkinter.filedialog import *

fenetre = Tk()

filepath = askopenfilename(title="Ouvrir une image", filetypes=[('png files', '.png'), ('all files', '.*')])

photo = PhotoImage(file=filepath)

canvas = Canvas(fenetre, width=photo.width(), height=photo.height(), bg="yellow")

canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

fenetre.mainloop()
"""