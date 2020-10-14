# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 04:29:16 2019

@author: sanik
"""
def logout0(em):
    import pandas as pd
    df=pd.read_csv('upwd.csv')
    df.loc[df["email_id"]==em, "status"] = 'log_out'
    df.to_csv("upwd.csv", index=False)
 
    
    
    
    
    
    
    
    
    
    
    
