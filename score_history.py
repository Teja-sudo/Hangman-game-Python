# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:06:20 2019

@author: sanik
"""
from tkinter import *
import pandas as pd
def schist():
    scwin = Tk()
   # win2.geometry('900x800')
    scwin.title('Score History')
    scdf=pd.read_csv('userscore.csv')
    scwin.configure(background='black')
    
    
    
    
    
    

scdf=str(pd.read_csv('userscore.csv'))
print(scdf)