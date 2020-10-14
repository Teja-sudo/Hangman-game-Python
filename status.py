# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:58:58 2019

@author: sanik
"""
import pandas as pd
import sendemail
import passwordcheck0
import forgotpassword
import upwd
global win1
global count,count1,df,emverify,sml1,cpwd0,cnpwd0,vfcode01,emverifyget
count,count1=0,0
df=pd.read_csv('upwd.csv')
df1 = df[df['status'].str.contains('log_in')]
#print(df1)

if not df1.empty :
    username0=(df1.user_name.values)
    #print(username0)
    email0=(df1.email_id.values)
    print(str(username0[0]))
    username0=str(username0[0])
    email0=str(email0[0])
    import gamehome
else :
    from tkinter import *
    import tkinter.messagebox
    
    def win1function():
        global win1
        win1 = Tk()
        win1.geometry('1900x800')
        win1.title('Sign in/Sign Up-->H A N G M A N')
        return win1
    #win1function()
    def winwidget():
        win1function()
        frame1=Frame(win1)
        canvas = Canvas(width=1790,height=900)
        canvas.pack()
        photo=PhotoImage(file='images\\bg.png')
        canvas.create_image(0,0,image=photo,anchor=NW)
        def destroying(d0):
            li=win1.winfo_children()
            #print(li)
            for child in range(d0,len(li)):
                li[child].destroy()
        
        def bforgotp() :
            global df,emidinget
            emidinget=emidin.get()
            df4=df[df['email_id'].str.contains(emidinget)]
            if df4.empty : tkinter.messagebox.showerror('wrong','User does not exist\nEnter correct Email Id to change password')
            else :
                def true0():
                    global countrue
                    countrue=0
                    try:
                        destroying(2)
                        ena = Label(win1, text = "Email Id",font='Times 20 bold',bg='deep sky blue',relief='sunken' ).place(x = 500,y = 300)
                        global emverify
                        emverify=StringVar()
                        e6 = Entry(win1,bg='light cyan',font='Times 20 bold ',textvariable=emverify).place(x = 700, y = 300)
                        def bafteremail():
                             sub1.configure(state='disabled')
                             global emverify,sml1,cpwd0,cnpwd0,vfcode01,emverifyget
                             emverifyget=emverify.get() 
                             try:
                                 sml1=sendemail.mailing(emverifyget)
                                 global count1
                                 count1+=1
                                 if count1>1:tkinter.messagebox.showinfo("Resent", "Verfication code has been resent")
                                 # else:tkinter.messagebox.showinfo("Verification code", "Verfication code has been sent to your Email Id")
                                 
                                 tkinter.messagebox.showinfo("Verification code", "Verfication code has been sent to your Email Id")
                                 destroying(2)
                                 cpwd0=StringVar()
                                 cnpwd0=StringVar()
                                 vfcode01=StringVar()
                                 vfc=Label(win1, text = "Verification Code",font='Times 18 bold',bg='cyan',relief='sunken' ).place(x = 600,y = 200)
                                 cp = Label(win1, text = "New password",font='Times 18 bold',bg='MediumOrchid2',relief='sunken' ).place(x = 600,y = 270)
                                 cnp = Label(win1, text = "Confirm Password",font='Times 18 bold',bg='yellow',relief='sunken' ).place(x = 600,y = 340)
                                 e8 = Entry(win1,bg='light cyan',font='Times 18 bold',textvariable=vfcode01).place(x = 870,y = 200) 
                                 e8 = Entry(win1,bg='light cyan',font='Times 18 bold',show='*',textvariable=cpwd0).place(x = 870,y = 270)  
                                 e9 = Entry(win1,bg='light cyan',font='Times 18 bold',show='*',textvariable=cnpwd0).place(x = 870, y = 340)  
                                 def bsubnewp():
                                     global emverifyget,sml1,cpwd0,cnpwd0,vfcode01,emverifyget1
                                     emverifyget=emverify.get() 
                                     emverifyget1=emverifyget
                                     vfcode01get=vfcode01.get()
                                     cpwd0get=cpwd0.get()
                                     cnpwd0get=cnpwd0.get()
                                     if sml1==vfcode01get :
                                         if cpwd0get==cnpwd0get :
                                             cpc=passwordcheck0.pwdcheck0(cpwd0get)
                                             if cpc==True:
                                                 sub2['state']=DISABLED
                                                 forgotpassword.newpassw(emverifyget,cnpwd0get)
                                                 tkinter.messagebox.showinfo("Sucess","Password changed sucessfully")
                                                 win1.destroy()
                                                 import gamehome
                                             else:tkinter.messagebox.showwarning('Required','password should be atleast 6 letters,one uppercase,lowercase and a digit and specialcharacter')
                                         else : tkinter.messagebox.showinfo("match failed", "New password and Confirm password should be same")
                                     else : tkinter.messagebox.showinfo("match failed", "Wrong verification code")
                                 sub2 = Button(win1, text = "Submit",bd=6,activebackground = "red", width=7,activeforeground = "white",cursor='hand2',font='Times 20 bold ',bg='green2',relief='raised',command=bsubnewp)
                                 sub2.place(x =600, y = 450)
                                 re = Button(win1, text = "Resend",bd=6,activebackground = "green2", width=7,activeforeground = "white",cursor='hand2',font='Times 20 bold ',bg='red',relief='raised',command=bafteremail).place(x = 830, y = 450)  
                             except Exception as e:
                                 retry0=tkinter.messagebox.askretrycancel('Something went wrong',e)
                                 if retry0==True :true0()
                                 else :
                                     win1.destroy()
                                     winwidget() 
                        sub1 = Button(win1, text = "Submit",bd=6,activebackground = "red", width=7,activeforeground = "white",cursor='hand2',font='Times 18 bold ',bg='green2',relief='raised',command=bafteremail)
                        sub1.place(x = 770, y = 400)
                    except Exception as e:
                        retry0=tkinter.messagebox.askretrycancel('Something went wrong',e)
                        if retry0==True :true0()
                        else :
                            win1.destroy()
                            winwidget()   
                true0()
        def bsignin0() :
            global emidinget,pwdinget,df
            emidinget=emidin.get()
            pwdinget=pwdin.get()
            df2 = df[df['email_id'].str.contains(emidinget)]
            df2pwd=df2.password.values
            df2pwd=str(df2pwd).strip("[,],','")
            df2emid=df2.email_id.values
            df2emid=str(df2emid).strip("[,],','")
            print('emidinget,pwdinget',df2emid,df2pwd)
            if not emidinget.strip() or not pwdinget.strip() :
                tkinter.messagebox.showwarning('Required','Email Id and password field above sign in must not be empty')
            else :   
                if df2emid==emidinget:
                    if df2pwd==pwdinget :
                        #destroying(1)
                        #global df
                        df.loc[df["email_id"]==emidinget, "status"] = 'log_in'
                        df.to_csv("upwd.csv", index=False)
                        tkinter.messagebox.showinfo('Welcome','You are redirected to homepage')
                        win1.destroy()
                        import gamehome
                    else:
                        tkinter.messagebox.showerror('wrong Email_Id','User does not exist')
                else:
                    tkinter.messagebox.showerror('wrong Email_Id','User does not exist')
        def bsignup0():
            global emidupget,pwdupget,userupget,df
            emidupget=emidup.get()
            pwdupget=pwdup.get()
            userupget=userup.get()
            df3=df[df['email_id'].str.contains(emidupget)]
            if not emidupget.strip() or not pwdupget.strip() or not userupget.strip() :tkinter.messagebox.showwarning('Required','All fields Must be required')
            else :
                if not df3.empty:tkinter.messagebox.showwarning('exist','User already exist')
               
                else :
                    ret=passwordcheck0.pwdcheck0(pwdupget)
                    if ret==True:
                        def verifying123():
                            try:
                                global emidupget,pwdupget,userupget,df
                                emidupget=emidup.get()
                                pwdupget=pwdup.get()
                                userupget=userup.get()
                                sml=sendemail.mailing(emidupget)
                                global count
                                count=count+1
                                if count>1:tkinter.messagebox.showinfo("Resent", "Verfication code has been resent")
                                else:tkinter.messagebox.showinfo("Verification code", "Verfication code has been sent to your Email Id")
                                destroying(2)
                                vname = Label(win1, text = "Verification code",font='Times 20 bold',bg='blue2',relief='sunken' ).place(x = 500,y = 300)
                                global verify0
                                verify0=StringVar()
                                e6 = Entry(win1,bg='light cyan',font='Times 20 bold ',textvariable=verify0).place(x = 750, y = 300)
                                def bsubmitvcode0():
                                   global verify0
                                   verify0get=verify0.get()
                                   if verify0get==sml :
                                       sub['state']=DISABLED
                                       upwd.storingdet(userupget,emidupget,pwdupget)
                                       tkinter.messagebox.showinfo('Successful','Your account creation successful')
                                       win1.destroy()
                                       import gamehome
                                   else:tkinter.messagebox.showerror('wrong','Verification code does not match')  
                                sub = Button(win1, text = "Submit",bd=6,activebackground = "red", width=7,activeforeground = "white",cursor='hand2',font='Times 18 bold ',bg='green2',relief='raised',command=bsubmitvcode0)
                                sub.place(x = 600, y = 400)  
                                re = Button(win1, text = "Resend",bd=6,activebackground = "green2", width=7,activeforeground = "white",cursor='hand2',font='Times 18 bold ',bg='red',relief='raised',command=bsignup0).place(x = 800, y = 400)  
                               
                                
                            except Exception as e:
                                retry0=tkinter.messagebox.askretrycancel('Something went wrong',e)
                                if retry0==True :verifying123()
                                else :winwidget()
                        verifying123()
                    else :tkinter.messagebox.showwarning('Required','password should be atleast 6 letters,one uppercase,lowercase and a digit and specialcharacter')
            
             
        emailin = Label(win1, text = "Email Id",font='Times 18 bold ',bg='deep sky blue',relief='sunken').place(x = 600, y = 50)  
  
        passwordin = Label(win1, text = "Password",font='Times 18 bold ',bg='yellow',relief='sunken').place(x = 600, y = 100)  
  
        sgin = Button(win1, text = "Sign In",bd=7,activebackground = "red",anchor=W,pady=-1,padx=5, activeforeground = "white",cursor='hand2',font='Times 18 bold ',bg='green2',relief='raised',command=bsignin0).place(x = 700, y = 180) 
        fgpd= Button(win1, text = "Forgot password",bd=7,activebackground = "red",width=12,  anchor=W,pady=-1,padx=5, activeforeground = "white",cursor='hand2',font='Times 18 bold ',bg='red',relief='raised',command=bforgotp).place(x = 900, y = 180)  
        global emidin,pwdin,emailup,userup,emidup,pwdup 
        emidin=StringVar()
        e1 = Entry(win1,bg='light cyan',font='Times 18',textvariable=emidin).place(x = 800, y = 50)
        pwdin=StringVar()
        e2 = Entry(win1,bg='light cyan',font='Times 18 bold',show='*',textvariable=pwdin).place(x = 800, y = 100)
        uname = Label(win1, text = "User Name",font='Times 18 bold',bg='MediumOrchid2',relief='sunken' ).place(x = 600,y = 300)  
  
        emailup = Label(win1, text = "Email Id",font='Times 18 bold ',bg='deep sky blue',relief='sunken').place(x = 600, y = 350)  
  
        passwordup = Label(win1, text = "Password",font='Times 18 bold ',bg='yellow',relief='sunken').place(x = 600, y = 400)  
  
        sgup = Button(win1, text = "Sign Up",bd=6,activebackground = "red", width=7,activeforeground = "white",cursor='hand2',font='Times 18 bold ',bg='green2',relief='raised',command=bsignup0)
        sgup.place(x = 700, y = 490)
        userup=StringVar()
        e3 = Entry(win1,bg='light cyan',font='Times 18 ',textvariable=userup).place(x = 800, y = 300)  
        emidup=StringVar()
        e4 = Entry(win1,bg='light cyan',font='Times 18 ',textvariable=emidup).place(x = 800, y = 350) 
        pwdup=StringVar()
        e5 = Entry(win1,bg='light cyan',font='Times 18 bold',show='*',textvariable=pwdup).place(x = 800, y = 400)  
        win1.mainloop()
    winwidget()
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        