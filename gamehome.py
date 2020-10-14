# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:42:46 2019

@author: sanik
"""


'''def outerFunction(text): 
    text = text '''
'''global c
c=0    
def innerFunction(): 
        global c
        c+=1
        print(5) 
        def f1():
          print(0)
        def f2():
            print(1)
        if c>1:
            f2()  
            f1()
        #else:print('n')
innerFunction()
innerFunction()
innerFunction()'''
from time import time 
import usc
import pygame
import string
import pandas as pd
from functools import partial
import onlinewords
import logout
from time import time
from tkinter import *
import tkinter.messagebox
import os
os.getcwd()
global count,count1,offret1,checkpoint,ock,dff30,dff31,bucl,uscue,uscun#,df,emverify,sml1,cpwd0,cnpwd0,vfcode01,emverifyget
count,count1,checkpoint,ock=0,0,0,0
bgmck=1
offret1=''
bucl="music\\buttonclick.mp3"
df=pd.read_csv("upwd.csv") 
df3 = df[df['status'].str.contains('log_in')]
dff30= df3.user_name.values
uscun=str(dff30)
dff30='User : '+str(dff30).strip("[,],'")
dff31=df3.email_id.values
uscue=str(dff31)
dffloge=str(dff31).strip("[,],'")
dff31='Email : '+dffloge
global win1
def win1function():
        global win1
        win1 = Tk()
        #pygame.mixer.init()
        pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
        pygame.init() #turn all of pygame on.
        win1.geometry('1900x800')
        win1.title('H A N G M A N')
        return win1
    #win1function()
def winwidget():
        win1function()
        global bgmusic0,bgmck
        #if bgmck==1:
        bgmusic0=pygame.mixer.Sound("music\\BGMUSIC5.wav")
        bgmusic0.play(-1)
        #bgmusic0.play(-1)
        frame1=Frame(win1)
        canvas = Canvas(win1,width=1790,height=900)
        canvas.pack()
        photo=PhotoImage(file='images\\bg.png')
        canvas.create_image(0,0,image=photo,anchor=NW)
        menubar = Menu(win1,activebackground='lime green')#,activeborderwidth=10,bg='red',bd=10,cursor='hand2',relief='raised',font='arial 40 bold '	)  
        Main_Menu = Menu(menubar, tearoff=0)  
        Main_Menu.add_command(label=dff30)  
        Main_Menu.add_command(label=dff31)  
        def Mhelp():
            import helpgame
            helpgame.helpgamewin()
        Main_Menu.add_command(label='Help',command=Mhelp)
        def Mgamehome():
               destroying(3)
               gamehome()
        Main_Menu.add_command(label="Home",command=Mgamehome)  
        def bslogout():
               bgmusic0.stop()
               logout.logout0(dffloge)
               win1.destroy()
               import status
        Main_Menu.add_command(label="Log out",command=bslogout)  
        Main_Menu.add_separator()  
        def winexit00():
            bgmusic0.stop()
            win1.destroy()
        Main_Menu.add_command(label="Exit", command=winexit00)  
        menubar.add_cascade(label="    = Main Menu ", menu=Main_Menu)  
        win1.config(menu=menubar)     
        lblimage=PhotoImage(file='images\\0.png')
        lbl1image=PhotoImage(file='images\\1.png')
        lbl2image=PhotoImage(file='images\\2.png')
        lbl3image=PhotoImage(file='images\\3.png')
        lbl4image=PhotoImage(file='images\\4.png')
        lbl5image=PhotoImage(file='images\\5.png')
        lbl6image=PhotoImage(file='images\\6.png')
        lbl7image=PhotoImage(file='images\\7.png')
        lbl81image=PhotoImage(file='images\\losep1.png')
        lbl82image=PhotoImage(file='images\\losep2.png')
        lbl83image=PhotoImage(file='images\\losep3.png')
        lbl84image=PhotoImage(file='images\\losep4.png')
        lbl85image=PhotoImage(file='images\\losep5.png')
        lbl86image=PhotoImage(file='images\\losep6.png')
        lbl87image=PhotoImage(file='images\\losep7.png')
        lbl88image=PhotoImage(file='images\\losep8.png')
        lbl89image=PhotoImage(file='images\\losep9.png')
        lbl810image=PhotoImage(file='images\\losep10.png')
        lbl811image=PhotoImage(file='images\\lose11.png')
        lbl812image=PhotoImage(file='images\\losep11.png')
        lbl813image=PhotoImage(file='images\\losep12.png')
        lbl9image=PhotoImage(file='images\\won.png')
        def destroying(d0):
            global bgmck
            bgmck=0
            li=win1.winfo_children()
            #print(li)
            for child in range(d0,len(li)):
                li[child].destroy()
        def Exit1():
            win1.destroy()
        def backfun():
                        def bback():
                            pygame.mixer.music.load(bucl) 
                            pygame.mixer.music.play()
                            destroying(3)
                            gamehome()
                        pb1 = Button(win1, text = "<-back",width=8,bd=8,activebackground = "red", fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green2',relief='raised', command=bback)
                        pb1.place(x = 1300, y = 660)
        def spoff():
                    destroying(3)
                    plr2 = Label(win1, text = "Second Player Enter Word : ",font='Times 30 bold ',bg='deep sky blue',fg='white',relief='sunken')
                    plr2.place(x = 200, y = 350) 
                    global p2in
                    p2in=StringVar()
                    eplr2 = Entry(win1,bg='light cyan',font='Times 26 bold',show='-',fg='white',textvariable=p2in ).place(x = 700, y = 354)
                    def bstart02():
                    
                        global p2in,checkpoint
                        checkpoint=2
                        p2inget=p2in.get()
                        st02=list(string.punctuation+' '+string.digits)
                        print(st02)
                        print(p2inget in st02)
                        if len(p2inget)>=3 :
                            c002=0
                            for i002 in p2inget:
                                if i002 in st02:
                                    c002=1
                            if c002==0:
                                p2inget=p2inget.upper()
                                tkinter.messagebox.showinfo('First Player','First player you have to Guess the word')
                                destroying(3)
                                maingame(p2inget)
                            if c002==1:tkinter.messagebox.showwarning('Rule','Your word must contains only letters')
                              
                        else:tkinter.messagebox.showwarning('Rule','Your word must contain atleast 3 letters')
                    ps2 = Button(win1, text = "Start",width=8,bd=8,activebackground = "red", fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green2',relief='raised', command=bstart02)
                    ps2.place(x = 640, y = 450)
                    
                    backfun()
        def maingame(wvar) :
            bgmusic0.stop()
            punctremov=list(string.punctuation)
            for xy in range(len(wvar)):
                            if wvar[xy] in punctremov:
                                wvar = wvar[0:xy]+wvar[xy+1:]
            global wvar1,ewvar,chance,ewl,imlb
            chance=0
            wvar1=wvar
            ewvar='-'*len(wvar)
            wl=str(len(wvar))  
            c0lab=Label(win1, text = 'Chances Left : ',font='arial 28 bold ',bg='khaki',fg='firebrick2',relief='sunken')
            c0lab.place(x = 10, y = 130)
            clab=Label(win1, text = '8',font='arial 28 bold ',bg='cyan',fg='firebrick2',relief='sunken')
            clab.place(x = 310, y = 130) 
            if not ock==1 :
                  def bhin():
                      pygame.mixer.music.load(bucl) 
                      pygame.mixer.music.play()
                      global chance
                      if chance<=5:
                          hin1.configure(bg='red',state='disabled')
                          chance=chance+2
                          hc=str(8-chance)
                          clab.configure(text=hc)
                          messagebox.showinfo("Information","You have taken hint so your remaining chances get substracted with 2") 
                          hil=Label(win1, text = offret1,font='Times 22 bold ',bg='blue2',fg='white')
                          hil.place(x = 190, y = 40) 
                      else:messagebox.showinfo("Information","Sorry,You can't get hint because you dont have sufficient number of chances") 
                  hin1= Button(win1, text = "HINT : ",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='purple3',relief='raised',command=bhin)#,command=bexit 
                  hin1.place(x = 20, y = 40)
                  
                
           
            
            wl0lab=Label(win1, text = 'Number of Words to guess :',font='arial 26 bold ',bg='khaki',fg='firebrick2',relief='sunken')
            wl0lab.place(x = 10, y = 210)
            wllab=Label(win1, text = wl,font='arial 28 bold ',bg='cyan',fg='firebrick2',relief='sunken')
            wllab.place(x = 500, y = 210) 
            ewlab=Label(win1, text = ewvar,width=16,font='arial 60 bold ',bg='cyan',fg='firebrick2',relief='sunken')
            ewlab.place(x = 60, y = 280) 
            imlb=Label(win1,image=lblimage)
            imlb.place(x=900,y=80)
            def rungame(al) :
                
                global wtg,wg,score
                global alp,ewvar,chance,ewl,imlb
                alp=al
                if alp=='A':abut.configure(bg='red',state='disabled')
                if alp=='B':bbut.configure(bg='red',state='disabled')
                if alp=='C':cbut.configure(bg='red',state='disabled')
                if alp=='D':dbut.configure(bg='red',state='disabled')
                if alp=='E':ebut.configure(bg='red',state='disabled')
                if alp=='F':fbut.configure(bg='red',state='disabled')
                if alp=='G':gbut.configure(bg='red',state='disabled')
                if alp=='H':hbut.configure(bg='red',state='disabled')
                if alp=='I':ibut.configure(bg='red',state='disabled')
                if alp=='J':jbut.configure(bg='red',state='disabled')
                if alp=='K':kbut.configure(bg='red',state='disabled')
                if alp=='L':lbut.configure(bg='red',state='disabled')
                if alp=='M':mbut.configure(bg='red',state='disabled')
                if alp=='N':nbut.configure(bg='red',state='disabled')
                if alp=='O':obut.configure(bg='red',state='disabled')
                if alp=='P':pbut.configure(bg='red',state='disabled')
                if alp=='Q':qbut.configure(bg='red',state='disabled')
                if alp=='R':rbut.configure(bg='red',state='disabled')
                if alp=='S':sbut.configure(bg='red',state='disabled')
                if alp=='T':tbut.configure(bg='red',state='disabled')
                if alp=='U':ubut.configure(bg='red',state='disabled')
                if alp=='V':vbut.configure(bg='red',state='disabled')
                if alp=='W':wbut.configure(bg='red',state='disabled')
                if alp=='X':xbut.configure(bg='red',state='disabled')
                if alp=='Y':ybut.configure(bg='red',state='disabled')
                if alp=='Z':zbut.configure(bg='red',state='disabled')
                def bpagain():
                                pygame.mixer.music.load(bucl) 
                                pygame.mixer.music.play()
                                destroying(3)
                                global bgmck
                                bgmck=1
                                gamehome()
                if alp in wvar1 :
                        pygame.mixer.music.load("music\\correct1.mp3") 
                        pygame.mixer.music.play() 
                        for x in range(len(wvar1)):
                            if wvar1[x] == alp:
                                ewvar = ewvar[0:x]+alp+ewvar[x+1:]
                        ewlab.configure(text=ewvar)
                        wl=str(ewvar.count('-'))
                        wllab.configure(text=wl)
                else:
                    pygame.mixer.music.load("music\\wrong5.mp3")
                    pygame.mixer.music.play() 
                    chance+=1
                    ch0=str(8-chance)
                    clab.configure(text=ch0)
                if chance==1:imlb.configure(image=lbl1image)
                if chance==2:imlb.configure(image=lbl2image)
                if chance==3:imlb.configure(image=lbl3image)
                if chance==4:imlb.configure(image=lbl4image)
                if chance==5:imlb.configure(image=lbl5image)
                if chance==6:imlb.configure(image=lbl6image)
                if chance==7:imlb.configure(image=lbl7image)
                if chance==8:
                    pygame.mixer.music.load("music\\Tapions_Flute.mp3") 
                    pygame.mixer.music.play(1)
                    abut.configure(state='disabled')
                    bbut.configure(state='disabled')
                    cbut.configure(state='disabled')
                    dbut.configure(state='disabled')
                    ebut.configure(state='disabled')
                    fbut.configure(state='disabled')
                    gbut.configure(state='disabled')
                    hbut.configure(state='disabled')
                    ibut.configure(state='disabled')
                    jbut.configure(state='disabled')
                    kbut.configure(state='disabled')
                    lbut.configure(state='disabled')
                    mbut.configure(state='disabled')
                    nbut.configure(state='disabled')
                    obut.configure(state='disabled')
                    pbut.configure(state='disabled')
                    qbut.configure(state='disabled')
                    rbut.configure(state='disabled')
                    sbut.configure(state='disabled')
                    tbut.configure(state='disabled')
                    ubut.configure(state='disabled')
                    vbut.configure(state='disabled')
                    wbut.configure(state='disabled')
                    xbut.configure(state='disabled')
                    ybut.configure(state='disabled')
                    zbut.configure(state='disabled')
                    start=time()
                    def Tf1():
                        imlb.configure(image=lbl81image)
                    def Tf2():imlb.configure(image=lbl82image)
                    def Tf3():imlb.configure(image=lbl83image)
                    def Tf4():imlb.configure(image=lbl84image)
                    def Tf5():imlb.configure(image=lbl85image)
                    def Tf6():imlb.configure(image=lbl86image)
                    def Tf7():imlb.configure(image=lbl87image)
                    def Tf8():imlb.configure(image=lbl88image)
                    def Tf9():imlb.configure(image=lbl89image)
                    def Tf10():imlb.configure(image=lbl810image)
                    def Tf11():imlb.configure(image=lbl811image)
                    def Tf12():imlb.configure(image=lbl812image)
                    def Tf13():imlb.configure(image=lbl813image)
                    win1.after(500,Tf1)
                    win1.after(1000,Tf2)
                    win1.after(1500,Tf3)
                    win1.after(2000,Tf4)
                    win1.after(2500,Tf5)
                    win1.after(3000,Tf6)
                    win1.after(3500,Tf7)
                    win1.after(4000,Tf8)
                    win1.after(4500,Tf9)
                    win1.after(5000,Tf10)
                    win1.after(5500,Tf11)
                    win1.after(6000,Tf12)
                    win1.after(6500,Tf13)
                    def des0():
                        destroying(3)
                        yowd='The Word Is : '+wvar1
                        losewlab=Label(win1, text = yowd,font='Times 62 bold ',bg='DarkOrchid3',fg='white')
                        losewlab.place(x = 100, y = 50)
                        # global wtg,wg,score
                        wtg=ewvar.count('-')
                    
                        le=len(wvar1)
                        wg=le-wtg
                    
                        score=wg/le*100
                        score=round(score,2)
                        if checkpoint==0:
                            usc.uscore(uscue,uscun,score,chance)
                            rearrange=pd.read_csv('userscore.csv')
                            rearrange.to_csv('userscore.csv',index=False)
                        wtg1='words to guess : '+str(wtg)
                        wg1='words guessed : '+str(wg)
                        score1='score : '+str(score)
                        wtglab=Label(win1, text = wtg1,font='Times 36 bold ',bg='blue2',fg='white')
                        wtglab.place(x=200,y=180)
                        wtglab=Label(win1, text = wg1,font='Times 36 bold ',bg='blue2',fg='white')
                        wtglab.place(x=200,y=290)
                        wtglab=Label(win1, text = score1,font='Times 36 bold ',bg='blue2',fg='white')
                        wtglab.place(x=200,y=390)
                        loselab=Label(win1, text = '              YOU LOSE',anchor=W,width=30,font='arial 102 bold ',bg='red',fg='white')
                        loselab.place(x = 0, y = 500)
                    
                    
                        if checkpoint==0:
                           ck0= Button(win1, text = "play again ",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green2',relief='raised',command=bpagain)#,command=bexit 
                           ck0.place(x = 300, y = 690)
                           ce0= Button(win1, text = " <-[ ] Exit",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='red',relief='raised',command=Exit1)#,command=bexit 
                           ce0.place(x = 1300, y = 690)
                        if checkpoint==1:
                           ck1= Button(win1, text = "Next-> ",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green2',relief='raised',command=spoff)#,command=bexit 
                           ck1.place(x = 300, y = 700)
                           ce= Button(win1, text = " <-[ ] Exit",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='red',relief='raised',command=Exit1)#,command=bexit 
                           ce.place(x = 1300, y = 700)
                        elif checkpoint==2:
                          ck2= Button(win1, text = "play again ",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green2',relief='raised',command=bpagain)#,command=bexit 
                          ck2.place(x = 300, y = 700)
                          ce2= Button(win1, text = " <-[ ] Exit",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='red',relief='raised',command=Exit1)#,command=bexit 
                          ce2.place(x = 1300, y = 700)
                    win1.after(7000,des0)
                elif chance<8 and not '-' in ewvar :
                        imlb.configure(image=lbl9image)
                        pygame.mixer.music.load("music\\a_won.mp3") 
                        pygame.mixer.music.play() 
                        #global wtg,wg,score
                        abut.configure(state='disabled')
                        bbut.configure(state='disabled')
                        cbut.configure(state='disabled')
                        dbut.configure(state='disabled')
                        ebut.configure(state='disabled')
                        fbut.configure(state='disabled')
                        gbut.configure(state='disabled')
                        hbut.configure(state='disabled')
                        ibut.configure(state='disabled')
                        jbut.configure(state='disabled')
                        kbut.configure(state='disabled')
                        lbut.configure(state='disabled')
                        mbut.configure(state='disabled')
                        nbut.configure(state='disabled')
                        obut.configure(state='disabled')
                        pbut.configure(state='disabled')
                        qbut.configure(state='disabled')
                        rbut.configure(state='disabled')
                        sbut.configure(state='disabled')
                        tbut.configure(state='disabled')
                        ubut.configure(state='disabled')
                        vbut.configure(state='disabled')
                        wbut.configure(state='disabled')
                        xbut.configure(state='disabled')
                        ybut.configure(state='disabled')
                        zbut.configure(state='disabled')
                        wtg=ewvar.count('-')
                        le=len(wvar1)
                        wg=le-wtg
                        start=time()
                        def des0():
                            destroying(3)
                       
                            score=wg/le*100
                            score=round(score,2)
                            wtg1='words to guess : '+str(wtg)
                            wg1='words guessed : '+str(wg)
                            score1='score : '+str(score)
                            if checkpoint==0:
                                usc.uscore(uscue,uscun,score,chance)
                                rearrange=pd.read_csv('userscore.csv')
                                rearrange.to_csv('userscore.csv',index=False)
                            wtglab=Label(win1, text = wtg1,font='Times 40 bold ',bg='blue2',fg='white')
                            wtglab.place(x=300,y=100)
                            wtglab=Label(win1, text = wg1,font='Times 40 bold ',bg='blue2',fg='white')
                            wtglab.place(x=300,y=210)
                            wtglab=Label(win1, text = score1,font='Times 40 bold ',bg='blue2',fg='white')
                            wtglab.place(x=300,y=310)
                            wonlab=Label(win1, text = '         YOU WON',anchor=W,width=30,font='arial 102 bold ',bg='green4',fg='white')
                            wonlab.place(x = 0, y = 450)
                            if checkpoint==0:
                                ck0= Button(win1, text = "play again ",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green2',relief='raised',command=bpagain)#,command=bexit 
                                ck0.place(x = 300, y = 690)
                                ce0= Button(win1, text = " <-[ ] Exit",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='red',relief='raised',command=Exit1)#,command=bexit 
                                ce0.place(x = 1300, y = 690)
                            
                            if checkpoint==1:
                                ck1= Button(win1, text = "Next-> ",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green2',relief='raised',command=spoff)#,command=bexit 
                                ck1.place(x = 300, y = 700)
                                ce= Button(win1, text = " <-[ ] Exit",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='red',relief='raised',command=Exit1)#,command=bexit 
                                ce.place(x = 1300, y = 700)
                            elif checkpoint==2:
                            
                                ck2= Button(win1, text = "play again ",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green2',relief='raised',command=bpagain)#,command=bexit 
                                ck2.place(x = 300, y = 690)
                                ce2= Button(win1, text = " <-[ ] Exit",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='red',relief='raised',command=Exit1)#,command=bexit 
                                ce2.place(x = 1300, y = 690)
                        win1.after(4000,des0)
            abut= Button(win1, text = "A",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'A'))#,command=bexit 
            abut.place(x = 20, y = 430)
            bbut= Button(win1, text = "B",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'B')) 
            bbut.place(x = 90, y = 430)
            cbut= Button(win1, text = "C",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'C'))#,command=bexit) 
            cbut.place(x = 180, y = 430)
            dbut= Button(win1, text = "D",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'D'))#,command=bexit) 
            dbut.place(x = 270, y = 430)
            ebut= Button(win1, text = "E",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'E'))#,command=bexit) 
            ebut.place(x = 360, y = 430)
            fbut= Button(win1, text = "F",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'F'))#,command=bexit) 
            fbut.place(x = 450, y = 430)
            gbut= Button(win1, text = "g",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'G'))#,command=bexit) 
            gbut.place(x = 540, y = 430)
            hbut= Button(win1, text = "H",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'H'))#,command=bexit) 
            hbut.place(x = 630, y = 430)
            ibut= Button(win1, text = "I",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'I'))#,command=bexit) 
            ibut.place(x = 720, y = 430)
            jbut= Button(win1, text = "J",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'J'))#,command=bexit) 
            jbut.place(x = 810, y = 430)
            kbut= Button(win1, text = "K",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'K'))#,command=bexit) 
            kbut.place(x = 100, y = 520)
            lbut= Button(win1, text = "L",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'L'))#,command=bexit) 
            lbut.place(x =190, y = 520)
            mbut= Button(win1, text = "M",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'M'))#,command=bexit) 
            mbut.place(x = 280, y = 520)
            nbut= Button(win1, text = "N",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'N'))#,command=bexit) 
            nbut.place(x = 370, y = 520)
            obut= Button(win1, text = "O",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'O'))#,command=bexit) 
            obut.place(x = 460, y = 520)
            pbut= Button(win1, text = "P",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'P'))#,command=bexit) 
            pbut.place(x = 550, y = 520)
            qbut= Button(win1, text = "Q",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'Q'))#,command=bexit) 
            qbut.place(x = 640, y = 520)
            rbut= Button(win1, text = "R",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'R'))#,command=bexit) 
            rbut.place(x = 730, y = 520)
            sbut= Button(win1, text = "S",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'S'))#,command=bexit) 
            sbut.place(x = 180, y = 610)
            tbut= Button(win1, text = "T",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'T'))#,command=bexit) 
            tbut.place(x = 270, y = 610)
            ubut= Button(win1, text = "U",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'U'))#,command=bexit) 
            ubut.place(x = 360, y = 610)
            vbut= Button(win1, text = "V",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'V'))#,command=bexit) 
            vbut.place(x = 450, y = 610)
            wbut= Button(win1, text = "W",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'W'))#,command=bexit) 
            wbut.place(x = 540, y = 610)
            xbut= Button(win1, text = "X",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'X'))#,command=bexit) 
            xbut.place(x = 630, y = 610)
            ybut= Button(win1, text = "Y",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'Y'))#,command=bexit) 
            ybut.place(x = 350, y = 700)
            zbut= Button(win1, text = "Z",bd=6,activebackground = "red",fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised',command=partial(rungame,'Z'))#,command=bexit) 
            zbut.place(x = 440, y = 700)
            
             
            
        
        def gamehome():
            global checkpoint
            checkpoint=0
            han0 = Label(win1, text = "H",font='Times 65 bold ',bg='blue2',fg='white',relief='sunken').place(x = 400, y = 80) 
            han1 = Label(win1, text = "A",font='Times 65 bold ',bg='green2',fg='white',relief='sunken').place(x = 500, y = 80) 
            han2 = Label(win1, text = "N",font='Times 65 bold ',bg='cyan',fg='white',relief='sunken').place(x = 600, y = 80) 
            han3 = Label(win1, text = "G",font='Times 65 bold ',bg='yellow2',fg='white',relief='sunken').place(x = 700, y = 80) 
            han4 = Label(win1, text = "M",font='Times 65 bold ',bg='purple1',fg='white',relief='sunken').place(x = 800, y = 80) 
            han5 = Label(win1, text = "A",font='Times 65 bold ',bg='orange red',fg='white',relief='sunken').place(x = 910, y = 80) 
            han6 = Label(win1, text = "N",font='Times 65 bold ',bg='deep sky blue',fg='white',relief='sunken').place(x = 1010, y = 80) 
            
            def boplay():
                pygame.mixer.music.load(bucl) 
                pygame.mixer.music.play()
               # p1['color']=firebrick1
                p1['state']=DISABLED
                #p1.configure(state = 'disabled')
                destroying(10)
                def boonline() :
                    pygame.mixer.music.load(bucl) 
                    pygame.mixer.music.play()
                    global ock
                    ock=1
                    
                    
                    try :
                        
                        onlret=onlinewords.onlinew()
                        oonl.configure(bg='firebrick1',state='disabled')
                        onlret=str(onlret).upper()
                        destroying(3)
                        maingame(onlret)
                        
                        
                    except Exception as e :
                        nerm=tkinter.messagebox.askretrycancel('Some thing went wrong','Please check your Internet connection')
                        if nerm==True:boonline()
                        else:gamehome()
                def booffline():
                    pygame.mixer.music.load(bucl) 
                    pygame.mixer.music.play()
                    global ock
                    ock=0
                    oofl['state']=DISABLED
                    destroying(3)
                    import offlinewords
                    offret=offlinewords.offlinew()
                    global offret0,offret1
                    offret0=str(offret[0]).upper()
                    offret1=str(offret[1])
                    maingame(offret0)
                oonl = Button(win1, text = "Online",bd=8,activebackground = "red", fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green2',relief='raised', command=boonline)
                oonl.place(x = 650, y = 250) 
                oofl = Button(win1, text = "Offline",bd=8,activebackground = "red", fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green2',relief='raised',command=booffline) 
                oofl.place(x = 645, y = 350)
                backfun()
            def btplay():
                pygame.mixer.music.load(bucl) 
                pygame.mixer.music.play()
                global ock
                ock=1
                destroying(10)
               # def btonline() :
                    #tkinter.messagebox.showinfo("Sorry","Availabe on Next Update")
                def btoffline() :
                    pygame.mixer.music.load(bucl) 
                    pygame.mixer.music.play()
                    destroying(3)
                    plr1 = Label(win1, text = "First Player Enter Word : ",font='Times 30 bold ',bg='deep sky blue',fg='white',relief='sunken')
                    plr1.place(x = 200, y = 350) 
                    global p1in
                    p1in=StringVar()
                    eplr1 = Entry(win1,bg='light cyan',font='Times 26 bold',show='-',fg='red',textvariable=p1in ).place(x = 700, y = 354)
                    def bstart0():
                        pygame.mixer.music.load(bucl) 
                        pygame.mixer.music.play()
                        global p1in,checkpoint
                        checkpoint=1
                        p1inget=p1in.get()
                        st0=list(string.punctuation+' '+string.digits)
                        print(st0)
                        print(p1inget in st0)
                        if len(p1inget)>=3 :
                            c00=0
                            for i00 in p1inget:
                                if i00 in st0:
                                    c00=1
                            if c00==0:
                                p1inget=p1inget.upper()
                                tkinter.messagebox.showinfo('Second Player','Second player you have to Guess the word')
                                destroying(3)
                                maingame(p1inget)
                            if c00==1:tkinter.messagebox.showwarning('Rule','Your word must contains only letters')
                              
                        else:tkinter.messagebox.showwarning('Rule','Your word must contain atleast 3 letters')
                    ps = Button(win1, text = "Start",width=8,bd=8,activebackground = "red", fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green2',relief='raised', command=bstart0)
                    ps.place(x = 640, y = 450)
                    
                    backfun()
                #tonl = Button(win1, text = "Online",bd=8,activebackground = "red", fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green2',relief='raised', command=btonline)
                #tonl.place(x = 650, y = 270)
                tofl = Button(win1, text = "Offline",bd=8,activebackground = "red", fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green2',relief='raised',command=btoffline) 
                tofl.place(x = 650, y = 380)
            def bexit():
                pygame.mixer.music.load(bucl) 
                pygame.mixer.music.play() 
                win1.destroy()
            
            
           
            global p1
           
           
            p1 = Button(win1, text = "One Player",bd=8,activebackground = "red", fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green3',relief='raised', command=boplay)
            p1.place(x = 650, y = 250) 
            p2 = Button(win1, text = "Two Players",bd=8,activebackground = "red", fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='green2',relief='raised',command=btplay) 
            p2.place(x = 645, y = 350) 
            p2 = Button(win1, text = "<-[ ] Exit",bd=8,activebackground = "red3",width=9, fg='white',activeforeground = "white",cursor='hand2',font='arial 22 bold ',bg='red2',relief='raised',command=bexit) 
            p2.place(x = 655, y = 450) 
            
            
            
        gamehome()
            
            
            
            
        win1.mainloop()
        bgmusic0.stop()
        end=time()
      
winwidget()