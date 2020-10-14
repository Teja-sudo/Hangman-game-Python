def onlinew():
    import requests
    import random
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    a=random.choice(WORDS)
    #b=str(a).strip("'")
    #print(b[2::])
    b=a.decode()
    return b
