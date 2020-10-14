def mailing(emailid_get) :
    import smtplib, ssl
    import string 
    import random
    global c1
    a1=string.digits+string.ascii_letters
    b1=6
    c1=''.join(random.choice(a1) for i in range(b1))
    print(c1)
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "hman63025@gmail.com"
    receiver_email = emailid_get
    a = "hwoman73307"
    message = """\
    Subject: Hangman

    verification code : %s"""%(c1)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo() 
        server.starttls(context=context)
        server.ehlo() 
        server.login(sender_email, a)
        server.sendmail(sender_email, receiver_email, message)
        print('Email Sent')
        server.quit() 
        return c1
        '''except Exception as e:
            
            print(e)
        finally:
            server.quit() '''
