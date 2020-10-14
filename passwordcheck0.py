def pwdcheck0(a):
    import string
    #a=str(input("Enter New Password : "))
    A,B,C,d,s=0,0,0,0,0
    sc=string.punctuation
    if len(a)>5:
            A=1
    for x in a:
        if x.isupper():
            B=1
        if x.islower():
            C=1
        if x.isspace():
            s=1
        if x in sc:
            d=1
    e=d+A+B+C+s       
    if e>=4:
        #print("password successfully created")
        return True
    else:
        #print('password should be atleast 6 letters,one uppercase,lowercase and a digit and specialcharacter')
        return False


