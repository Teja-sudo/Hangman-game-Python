# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 01:18:37 2019

@author: sanik
"""
from tkinter import *
def helpgamewin():
    
    win2 = Tk()
   # win2.geometry('900x800')
    win2.title('Help')
    win2.configure(background='cyan')
    a='-->Game is simple,\n you just need to guess a letter in a given secret word.'
    b='-->You have given eight chances.'
    c='-->If you guess correct letters in 8 chances \nthen you win the game or else you lose the game.'
    d='Note : Only one player offline mode contains hint.'
    l1=Label(win2, text = a,font='Times 22 bold ',bg='cyan',anchor=W)
    l1.grid(row=0,column=0)
    l2=Label(win2, text =b,bg='cyan',font='Times 22 bold ',anchor=W)
    l2.grid(row=1,column=0)
    l3=Label(win2, text = c,bg='cyan',font='Times 22 bold ',anchor=W)
    l3.grid(row=2,column=0)
    l4=Label(win2, text = d,bg='cyan',font='Times 22 bold ',anchor=W)
    l4.grid(row=3,column=0)
    clo= Button(win2, text = "Close",bd=6,activebackground = "red2",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='red',relief='raised',command=win2.destroy)#,command=bexit 
    clo.grid()
    win2.mainloop()
