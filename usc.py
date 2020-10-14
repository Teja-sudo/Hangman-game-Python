# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:52:07 2019

@author: sanik
"""
def uscore(ue,un,sc,ch):
    import pandas as pd
    data = [[ue,un,sc,ch]] 
    df = pd.DataFrame(data,columns=['email_id','user_name','score','chances'])
    print (df)
    with open('userscore.csv', 'a') as f:
        df.to_csv(f, mode='a', header=f.tell()==0)

