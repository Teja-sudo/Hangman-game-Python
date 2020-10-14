def offlinew():
    import random as rd
    with open("wordsfile2.txt","r") as f:
        b=[]   
        for i in f:
            l=i.split(',')
            b.append(l)
        #print(b)
    f.close()
    a=rd.randrange(0,52)
    wohi=[str(b[a][0]),str(b[a][1])]
    #hi=str(b[a][1])
    print('word :',str(b[a][0]))
    print('hint :',str(b[a][1]))
    return wohi

'''a0=offlinew()
print(str(a0[1]))'''
try:
    fileptr = open("file2.txt","r")  
    print(1234)
    if fileptr:  
       print("file is opened successfully")
       fileptr.close()
except Exception as e:
    print(e)
