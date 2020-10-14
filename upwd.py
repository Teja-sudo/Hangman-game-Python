# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 02:57:48 2019

@author: sanik
"""
def storingdet(un,u,p):
    import pandas as pd
    #un=input('enter user name') 
    #u=input('enter email id')
    #p=input('enter pwd')
    status='log_in'
    data = [[u,p,un,status]] 
    df = pd.DataFrame(data,columns=['email_id','password','user_name','status'])
    print (df)
    with open('upwd.csv', 'a') as f:
          df.to_csv(f, mode='a', header=f.tell()==0)
