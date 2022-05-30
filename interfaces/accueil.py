# This is a sample Python script.
import tkinter as tk
from tkinter import *




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


# Function btn
def choice_btn():
    choice = fileChoice.get()
    if choice == 1:
        home.destroy()
        import interfaces.CarteGrise.CarteGrise
    elif choice == 2:
        home.destroy()
        import interfaces.CarteIdentite.CarteIdentite
    elif choice == 3:
        home.destroy()
        import interfaces.permisdeconduire.PermisDeConduire


# Radio button
fileChoice = IntVar()
rb1 = Radiobutton(home, text="Gray card", value=1, variable=fileChoice)
rb2 = Radiobutton(home, text="Id card", value=2, variable=fileChoice)
rb3 = Radiobutton(home, text="Driver License", value=3, variable=fileChoice)
rb1.pack()
rb2.pack()
rb3.pack()

rb1.select()

cmd = Button(home, text="Ok", command=choice_btn)
cmd.pack()
home.mainloop()
