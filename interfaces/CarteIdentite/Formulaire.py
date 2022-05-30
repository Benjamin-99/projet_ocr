#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 18, 2022 04:09:50 PM CEST  platform: Windows NT

import sys
import tkinter as tk
from tkinter.tix import Tk

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9'  # X11 color: 'gray85'
_ana1color = '#d9d9d9'  # X11 color: 'gray85'
_ana2color = '#ececec'  # Closest X11 color: 'gray92'

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = tk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("787x524+346+75")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.top = top

        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.14, rely=0.363, height=30, relwidth=0.335)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry1_1 = tk.Entry(self.top)
        self.Entry1_1.place(relx=0.14, rely=0.515, height=30, relwidth=0.335)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.064, rely=0.363, height=25, width=45)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Nom(s)''')

        self.Label1_1 = tk.Label(self.top)
        self.Label1_1.place(relx=0.038, rely=0.515, height=25, width=63)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Prénom(s)''')

        self.Label1_1_1 = tk.Label(self.top)
        self.Label1_1_1.place(relx=0.027, rely=0.706, height=36, width=71)
        self.Label1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1.configure(activeforeground="black")
        self.Label1_1_1.configure(anchor='w')
        self.Label1_1_1.configure(background="#d9d9d9")
        self.Label1_1_1.configure(compound='left')
        self.Label1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1.configure(foreground="#000000")
        self.Label1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1.configure(highlightcolor="black")
        self.Label1_1_1.configure(text='''Né(e) le''')

        self.Label1_1_1_1 = tk.Label(self.top)
        self.Label1_1_1_1.place(relx=0.286, rely=0.7, height=36, width=8)
        self.Label1_1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1_1.configure(activeforeground="black")
        self.Label1_1_1_1.configure(anchor='w')
        self.Label1_1_1_1.configure(background="#d9d9d9")
        self.Label1_1_1_1.configure(compound='left')
        self.Label1_1_1_1.configure(cursor="fleur")
        self.Label1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_1.configure(foreground="#000000")
        self.Label1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_1.configure(highlightcolor="black")
        self.Label1_1_1_1.configure(text='''à''')

        self.Label1_2 = tk.Label(self.top)
        self.Label1_2.place(relx=0.521, rely=0.229, height=25, width=60)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(anchor='w')
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(compound='left')
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''Catégorie:''')

        self.Label1_2_1 = tk.Label(self.top)
        self.Label1_2_1.place(relx=0.009, rely=0.229, height=25, width=89)
        self.Label1_2_1.configure(activebackground="#f9f9f9")
        self.Label1_2_1.configure(activeforeground="black")
        self.Label1_2_1.configure(anchor='w')
        self.Label1_2_1.configure(background="#d9d9d9")
        self.Label1_2_1.configure(compound='left')
        self.Label1_2_1.configure(disabledforeground="#a3a3a3")
        self.Label1_2_1.configure(foreground="#000000")
        self.Label1_2_1.configure(highlightbackground="#d9d9d9")
        self.Label1_2_1.configure(highlightcolor="black")
        self.Label1_2_1.configure(text='''Permis Numero''')

        self.Entry1_2 = tk.Entry(self.top)
        self.Entry1_2.place(relx=0.61, rely=0.229, height=30, relwidth=0.348)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(cursor="fleur")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font="TkFixedFont")
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="blue")
        self.Entry1_2.configure(selectforeground="white")

        self.Label1_2_2 = tk.Label(self.top)
        self.Label1_2_2.place(relx=0.524, rely=0.706, height=25, width=62)
        self.Label1_2_2.configure(activebackground="#f9f9f9")
        self.Label1_2_2.configure(activeforeground="black")
        self.Label1_2_2.configure(anchor='w')
        self.Label1_2_2.configure(background="#d9d9d9")
        self.Label1_2_2.configure(compound='left')
        self.Label1_2_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2_2.configure(foreground="#000000")
        self.Label1_2_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2_2.configure(highlightcolor="black")
        self.Label1_2_2.configure(text='''Etabli le :''')

        self.Entry1_2_1 = tk.Entry(self.top)
        self.Entry1_2_1.place(relx=0.61, rely=0.706, height=30, relwidth=0.145)
        self.Entry1_2_1.configure(background="white")
        self.Entry1_2_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_2_1.configure(font="TkFixedFont")
        self.Entry1_2_1.configure(foreground="#000000")
        self.Entry1_2_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_2_1.configure(highlightcolor="black")
        self.Entry1_2_1.configure(insertbackground="black")
        self.Entry1_2_1.configure(selectbackground="blue")
        self.Entry1_2_1.configure(selectforeground="white")

        self.Label1_2_2_1 = tk.Label(self.top)
        self.Label1_2_2_1.place(relx=0.761, rely=0.716, height=15, width=10)
        self.Label1_2_2_1.configure(activebackground="#f9f9f9")
        self.Label1_2_2_1.configure(activeforeground="black")
        self.Label1_2_2_1.configure(anchor='w')
        self.Label1_2_2_1.configure(background="#d9d9d9")
        self.Label1_2_2_1.configure(compound='left')
        self.Label1_2_2_1.configure(disabledforeground="#a3a3a3")
        self.Label1_2_2_1.configure(foreground="#000000")
        self.Label1_2_2_1.configure(highlightbackground="#d9d9d9")
        self.Label1_2_2_1.configure(highlightcolor="black")
        self.Label1_2_2_1.configure(text='''à''')

        self.Entry1_2_1_1 = tk.Entry(self.top)
        self.Entry1_2_1_1.place(relx=0.788, rely=0.706, height=30
                                , relwidth=0.183)
        self.Entry1_2_1_1.configure(background="white")
        self.Entry1_2_1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_2_1_1.configure(font="TkFixedFont")
        self.Entry1_2_1_1.configure(foreground="#000000")
        self.Entry1_2_1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_2_1_1.configure(highlightcolor="black")
        self.Entry1_2_1_1.configure(insertbackground="black")
        self.Entry1_2_1_1.configure(selectbackground="blue")
        self.Entry1_2_1_1.configure(selectforeground="white")

        self.Entry1_1_1 = tk.Entry(self.top)
        self.Entry1_1_1.place(relx=0.14, rely=0.706, height=30, relwidth=0.145)
        self.Entry1_1_1.configure(background="white")
        self.Entry1_1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1_1.configure(font="TkFixedFont")
        self.Entry1_1_1.configure(foreground="#000000")
        self.Entry1_1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1_1.configure(highlightcolor="black")
        self.Entry1_1_1.configure(insertbackground="black")
        self.Entry1_1_1.configure(selectbackground="blue")
        self.Entry1_1_1.configure(selectforeground="white")

        self.Entry1_1_1_1 = tk.Entry(self.top)
        self.Entry1_1_1_1.place(relx=0.305, rely=0.704, height=30, relwidth=0.17)

        self.Entry1_1_1_1.configure(background="white")
        self.Entry1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1_1_1.configure(font="TkFixedFont")
        self.Entry1_1_1_1.configure(foreground="#000000")
        self.Entry1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1_1_1.configure(highlightcolor="black")
        self.Entry1_1_1_1.configure(insertbackground="black")
        self.Entry1_1_1_1.configure(selectbackground="blue")
        self.Entry1_1_1_1.configure(selectforeground="white")

        self.Label1_2_2_2 = tk.Label(self.top)
        self.Label1_2_2_2.place(relx=0.521, rely=0.515, height=25, width=62)
        self.Label1_2_2_2.configure(activebackground="#f9f9f9")
        self.Label1_2_2_2.configure(activeforeground="black")
        self.Label1_2_2_2.configure(anchor='w')
        self.Label1_2_2_2.configure(background="#d9d9d9")
        self.Label1_2_2_2.configure(compound='left')
        self.Label1_2_2_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2_2_2.configure(foreground="#000000")
        self.Label1_2_2_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2_2_2.configure(highlightcolor="black")
        self.Label1_2_2_2.configure(text='''Expire le:''')

        self.Entry1_2_1_1_1 = tk.Entry(self.top)
        self.Entry1_2_1_1_1.place(relx=0.61, rely=0.515, height=30
                                  , relwidth=0.348)
        self.Entry1_2_1_1_1.configure(background="white")
        self.Entry1_2_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_2_1_1_1.configure(font="TkFixedFont")
        self.Entry1_2_1_1_1.configure(foreground="#000000")
        self.Entry1_2_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_2_1_1_1.configure(highlightcolor="black")
        self.Entry1_2_1_1_1.configure(insertbackground="black")
        self.Entry1_2_1_1_1.configure(selectbackground="blue")
        self.Entry1_2_1_1_1.configure(selectforeground="white")

        self.Label1_1_1_2 = tk.Label(self.top)
        self.Label1_1_1_2.place(relx=0.516, rely=0.353, height=36, width=67)
        self.Label1_1_1_2.configure(activebackground="#f9f9f9")
        self.Label1_1_1_2.configure(activeforeground="black")
        self.Label1_1_1_2.configure(anchor='w')
        self.Label1_1_1_2.configure(background="#d9d9d9")
        self.Label1_1_1_2.configure(compound='left')
        self.Label1_1_1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_2.configure(foreground="#000000")
        self.Label1_1_1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_2.configure(highlightcolor="black")
        self.Label1_1_1_2.configure(text='''Bande Mrz''')

        self.Entry1_2_2 = tk.Entry(self.top)
        self.Entry1_2_2.place(relx=0.61, rely=0.363, height=30, relwidth=0.348)
        self.Entry1_2_2.configure(background="white")
        self.Entry1_2_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2_2.configure(font="TkFixedFont")
        self.Entry1_2_2.configure(foreground="#000000")
        self.Entry1_2_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2_2.configure(highlightcolor="black")
        self.Entry1_2_2.configure(insertbackground="black")
        self.Entry1_2_2.configure(selectbackground="blue")
        self.Entry1_2_2.configure(selectforeground="white")

        self.Entry1_2_3 = tk.Entry(self.top)
        self.Entry1_2_3.place(relx=0.25, rely=0.067, height=1, relwidth=0.183)
        self.Entry1_2_3.configure(background="white")
        self.Entry1_2_3.configure(disabledforeground="#a3a3a3")
        self.Entry1_2_3.configure(font="TkFixedFont")
        self.Entry1_2_3.configure(foreground="#000000")
        self.Entry1_2_3.configure(highlightbackground="#d9d9d9")
        self.Entry1_2_3.configure(highlightcolor="black")
        self.Entry1_2_3.configure(insertbackground="black")
        self.Entry1_2_3.configure(selectbackground="blue")
        self.Entry1_2_3.configure(selectforeground="white")

        self.TSeparator1 = tk.Separator(self.top)
        self.TSeparator1.place(relx=0.496, rely=0.191, relheight=0.63)
        self.TSeparator1.configure(orient="vertical")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.Entry1_3 = tk.Entry(self.top)
        self.Entry1_3.place(relx=0.14, rely=0.229, height=30, relwidth=0.335)
        self.Entry1_3.configure(background="white")
        self.Entry1_3.configure(disabledforeground="#a3a3a3")
        self.Entry1_3.configure(font="TkFixedFont")
        self.Entry1_3.configure(foreground="#000000")
        self.Entry1_3.configure(highlightbackground="#d9d9d9")
        self.Entry1_3.configure(highlightcolor="black")
        self.Entry1_3.configure(insertbackground="black")
        self.Entry1_3.configure(selectbackground="blue")
        self.Entry1_3.configure(selectforeground="white")

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.839, rely=0.897, height=24, width=67)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')


root = Tk()
Entry1 = tk.Entry(root)
Entry1.place(relx=0.14, rely=0.363, height=30, relwidth=0.335)
Entry1.configure(background="white")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font="TkFixedFont")
Entry1.configure(foreground="#000000")
Entry1.configure(insertbackground="black")

Entry1_1 = tk.Entry(root)
Entry1_1.place(relx=0.14, rely=0.515, height=30, relwidth=0.335)
Entry1_1.configure(background="white")
Entry1_1.configure(disabledforeground="#a3a3a3")
Entry1_1.configure(font="TkFixedFont")
Entry1_1.configure(foreground="#000000")
Entry1_1.configure(highlightbackground="#d9d9d9")
Entry1_1.configure(highlightcolor="black")
Entry1_1.configure(insertbackground="black")
Entry1_1.configure(selectbackground="blue")
Entry1_1.configure(selectforeground="white")

Label1 = tk.Label(root)
Label1.place(relx=0.064, rely=0.363, height=25, width=45)
Label1.configure(anchor='w')
Label1.configure(background="#d9d9d9")
Label1.configure(compound='left')
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(foreground="#000000")
Label1.configure(text='''Nom(s)''')

Label1_1 = tk.Label(root)
Label1_1.place(relx=0.038, rely=0.515, height=25, width=63)
Label1_1.configure(activebackground="#f9f9f9")
Label1_1.configure(activeforeground="black")
Label1_1.configure(anchor='w')
Label1_1.configure(background="#d9d9d9")
Label1_1.configure(compound='left')
Label1_1.configure(disabledforeground="#a3a3a3")
Label1_1.configure(foreground="#000000")
Label1_1.configure(highlightbackground="#d9d9d9")
Label1_1.configure(highlightcolor="black")
Label1_1.configure(text='''Prénom(s)''')

Label1_1_1 = tk.Label(root)
Label1_1_1.place(relx=0.027, rely=0.706, height=36, width=71)
Label1_1_1.configure(activebackground="#f9f9f9")
Label1_1_1.configure(activeforeground="black")
Label1_1_1.configure(anchor='w')
Label1_1_1.configure(background="#d9d9d9")
Label1_1_1.configure(compound='left')
Label1_1_1.configure(disabledforeground="#a3a3a3")
Label1_1_1.configure(foreground="#000000")
Label1_1_1.configure(highlightbackground="#d9d9d9")
Label1_1_1.configure(highlightcolor="black")
Label1_1_1.configure(text='''Né(e) le''')

Label1_1_1_1 = tk.Label(root)
Label1_1_1_1.place(relx=0.286, rely=0.7, height=36, width=8)
Label1_1_1_1.configure(activebackground="#f9f9f9")
Label1_1_1_1.configure(activeforeground="black")
Label1_1_1_1.configure(anchor='w')
Label1_1_1_1.configure(background="#d9d9d9")
Label1_1_1_1.configure(compound='left')
Label1_1_1_1.configure(cursor="fleur")
Label1_1_1_1.configure(disabledforeground="#a3a3a3")
Label1_1_1_1.configure(foreground="#000000")
Label1_1_1_1.configure(highlightbackground="#d9d9d9")
Label1_1_1_1.configure(highlightcolor="black")
Label1_1_1_1.configure(text='''à''')

Label1_2 = tk.Label(root)
Label1_2.place(relx=0.521, rely=0.229, height=25, width=60)
Label1_2.configure(activebackground="#f9f9f9")
Label1_2.configure(activeforeground="black")
Label1_2.configure(anchor='w')
Label1_2.configure(background="#d9d9d9")
Label1_2.configure(compound='left')
Label1_2.configure(disabledforeground="#a3a3a3")
Label1_2.configure(foreground="#000000")
Label1_2.configure(highlightbackground="#d9d9d9")
Label1_2.configure(highlightcolor="black")
Label1_2.configure(text='''Catégorie:''')

Label1_2_1 = tk.Label(root)
Label1_2_1.place(relx=0.009, rely=0.229, height=25, width=89)
Label1_2_1.configure(activebackground="#f9f9f9")
Label1_2_1.configure(activeforeground="black")
Label1_2_1.configure(anchor='w')
Label1_2_1.configure(background="#d9d9d9")
Label1_2_1.configure(compound='left')
Label1_2_1.configure(disabledforeground="#a3a3a3")
Label1_2_1.configure(foreground="#000000")
Label1_2_1.configure(highlightbackground="#d9d9d9")
Label1_2_1.configure(highlightcolor="black")
Label1_2_1.configure(text='''Permis Numero''')

Entry1_2 = tk.Entry(root)
Entry1_2.place(relx=0.61, rely=0.229, height=30, relwidth=0.348)
Entry1_2.configure(background="white")
Entry1_2.configure(cursor="fleur")
Entry1_2.configure(disabledforeground="#a3a3a3")
Entry1_2.configure(font="TkFixedFont")
Entry1_2.configure(foreground="#000000")
Entry1_2.configure(highlightbackground="#d9d9d9")
Entry1_2.configure(highlightcolor="black")
Entry1_2.configure(insertbackground="black")
Entry1_2.configure(selectbackground="blue")
Entry1_2.configure(selectforeground="white")

Label1_2_2 = tk.Label(root)
Label1_2_2.place(relx=0.524, rely=0.706, height=25, width=62)
Label1_2_2.configure(activebackground="#f9f9f9")
Label1_2_2.configure(activeforeground="black")
Label1_2_2.configure(anchor='w')
Label1_2_2.configure(background="#d9d9d9")
Label1_2_2.configure(compound='left')
Label1_2_2.configure(disabledforeground="#a3a3a3")
Label1_2_2.configure(foreground="#000000")
Label1_2_2.configure(highlightbackground="#d9d9d9")
Label1_2_2.configure(highlightcolor="black")
Label1_2_2.configure(text='''Etabli le :''')

Entry1_2_1 = tk.Entry(root)
Entry1_2_1.place(relx=0.61, rely=0.706, height=30, relwidth=0.145)
Entry1_2_1.configure(background="white")
Entry1_2_1.configure(disabledforeground="#a3a3a3")
Entry1_2_1.configure(font="TkFixedFont")
Entry1_2_1.configure(foreground="#000000")
Entry1_2_1.configure(highlightbackground="#d9d9d9")
Entry1_2_1.configure(highlightcolor="black")
Entry1_2_1.configure(insertbackground="black")
Entry1_2_1.configure(selectbackground="blue")
Entry1_2_1.configure(selectforeground="white")

Label1_2_2_1 = tk.Label(root)
Label1_2_2_1.place(relx=0.761, rely=0.716, height=15, width=10)
Label1_2_2_1.configure(activebackground="#f9f9f9")
Label1_2_2_1.configure(activeforeground="black")
Label1_2_2_1.configure(anchor='w')
Label1_2_2_1.configure(background="#d9d9d9")
Label1_2_2_1.configure(compound='left')
Label1_2_2_1.configure(disabledforeground="#a3a3a3")
Label1_2_2_1.configure(foreground="#000000")
Label1_2_2_1.configure(highlightbackground="#d9d9d9")
Label1_2_2_1.configure(highlightcolor="black")
Label1_2_2_1.configure(text='''à''')

Entry1_2_1_1 = tk.Entry(root)
Entry1_2_1_1.place(relx=0.788, rely=0.706, height=30
                                , relwidth=0.183)
Entry1_2_1_1.configure(background="white")
Entry1_2_1_1.configure(disabledforeground="#a3a3a3")
Entry1_2_1_1.configure(font="TkFixedFont")
Entry1_2_1_1.configure(foreground="#000000")
Entry1_2_1_1.configure(highlightbackground="#d9d9d9")
Entry1_2_1_1.configure(highlightcolor="black")
Entry1_2_1_1.configure(insertbackground="black")
Entry1_2_1_1.configure(selectbackground="blue")
Entry1_2_1_1.configure(selectforeground="white")

Entry1_1_1 = tk.Entry(root)
Entry1_1_1.place(relx=0.14, rely=0.706, height=30, relwidth=0.145)
Entry1_1_1.configure(background="white")
Entry1_1_1.configure(disabledforeground="#a3a3a3")
Entry1_1_1.configure(font="TkFixedFont")
Entry1_1_1.configure(foreground="#000000")
Entry1_1_1.configure(highlightbackground="#d9d9d9")
Entry1_1_1.configure(highlightcolor="black")
Entry1_1_1.configure(insertbackground="black")
Entry1_1_1.configure(selectbackground="blue")
Entry1_1_1.configure(selectforeground="white")

Entry1_1_1_1 = tk.Entry(root)
Entry1_1_1_1.place(relx=0.305, rely=0.704, height=30, relwidth=0.17)

Entry1_1_1_1.configure(background="white")
Entry1_1_1_1.configure(disabledforeground="#a3a3a3")
Entry1_1_1_1.configure(font="TkFixedFont")
Entry1_1_1_1.configure(foreground="#000000")
Entry1_1_1_1.configure(highlightbackground="#d9d9d9")
Entry1_1_1_1.configure(highlightcolor="black")
Entry1_1_1_1.configure(insertbackground="black")
Entry1_1_1_1.configure(selectbackground="blue")
Entry1_1_1_1.configure(selectforeground="white")

Label1_2_2_2 = tk.Label(root)
Label1_2_2_2.place(relx=0.521, rely=0.515, height=25, width=62)
Label1_2_2_2.configure(activebackground="#f9f9f9")
Label1_2_2_2.configure(activeforeground="black")
Label1_2_2_2.configure(anchor='w')
Label1_2_2_2.configure(background="#d9d9d9")
Label1_2_2_2.configure(compound='left')
Label1_2_2_2.configure(disabledforeground="#a3a3a3")
Label1_2_2_2.configure(foreground="#000000")
Label1_2_2_2.configure(highlightbackground="#d9d9d9")
Label1_2_2_2.configure(highlightcolor="black")
Label1_2_2_2.configure(text='''Expire le:''')

Entry1_2_1_1_1 = tk.Entry(root)
Entry1_2_1_1_1.place(relx=0.61, rely=0.515, height=30
                                  , relwidth=0.348)
Entry1_2_1_1_1.configure(background="white")
Entry1_2_1_1_1.configure(disabledforeground="#a3a3a3")
Entry1_2_1_1_1.configure(font="TkFixedFont")
Entry1_2_1_1_1.configure(foreground="#000000")
Entry1_2_1_1_1.configure(highlightbackground="#d9d9d9")
Entry1_2_1_1_1.configure(highlightcolor="black")
Entry1_2_1_1_1.configure(insertbackground="black")
Entry1_2_1_1_1.configure(selectbackground="blue")
Entry1_2_1_1_1.configure(selectforeground="white")

Label1_1_1_2 = tk.Label(root)
Label1_1_1_2.place(relx=0.516, rely=0.353, height=36, width=67)
Label1_1_1_2.configure(activebackground="#f9f9f9")
Label1_1_1_2.configure(activeforeground="black")
Label1_1_1_2.configure(anchor='w')
Label1_1_1_2.configure(background="#d9d9d9")
Label1_1_1_2.configure(compound='left')
Label1_1_1_2.configure(disabledforeground="#a3a3a3")
Label1_1_1_2.configure(foreground="#000000")
Label1_1_1_2.configure(highlightbackground="#d9d9d9")
Label1_1_1_2.configure(highlightcolor="black")
Label1_1_1_2.configure(text='''Bande Mrz''')

Entry1_2_2 = tk.Entry(root)
Entry1_2_2.place(relx=0.61, rely=0.363, height=30, relwidth=0.348)
Entry1_2_2.configure(background="white")
Entry1_2_2.configure(disabledforeground="#a3a3a3")
Entry1_2_2.configure(font="TkFixedFont")
Entry1_2_2.configure(foreground="#000000")
Entry1_2_2.configure(highlightbackground="#d9d9d9")
Entry1_2_2.configure(highlightcolor="black")
Entry1_2_2.configure(insertbackground="black")
Entry1_2_2.configure(selectbackground="blue")
Entry1_2_2.configure(selectforeground="white")

"""TSeparator1 = tk.SEPARATOR(root)
TSeparator1.place(relx=0.496, rely=0.191, relheight=0.63)
TSeparator1.configure(orient="vertical")"""

menubar = tk.Menu(root, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
root.configure(menu=menubar)

Entry1_3 = tk.Entry(root)
Entry1_3.place(relx=0.14, rely=0.229, height=30, relwidth=0.335)
Entry1_3.configure(background="white")
Entry1_3.configure(disabledforeground="#a3a3a3")
Entry1_3.configure(font="TkFixedFont")
Entry1_3.configure(foreground="#000000")
Entry1_3.configure(highlightbackground="#d9d9d9")
Entry1_3.configure(highlightcolor="black")
Entry1_3.configure(insertbackground="black")
Entry1_3.configure(selectbackground="blue")
Entry1_3.configure(selectforeground="white")

Button1 = tk.Button(root)
Button1.place(relx=0.839, rely=0.897, height=24, width=67)
Button1.configure(activebackground="#ececec")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#d9d9d9")
Button1.configure(compound='left')
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''Button''')

root.geometry("787x524+346+75")
root.minsize(120, 1)
root.maxsize(1370, 749)
root.resizable(1, 1)
root.title("Carte d'identité")
root.configure(background="#d9d9d9")

root.mainloop()
