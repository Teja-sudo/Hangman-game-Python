# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 05:26:03 2019

@author: sanik
"""

def newpassw(e01,p01):
    import pandas as pd
    df=pd.read_csv('upwd.csv')
    df.loc[df["email_id"]==e01, "password"] = p01
    df.loc[df["email_id"]==e01, "status"] = 'log_in'
    df.to_csv("upwd.csv", index=False)
 