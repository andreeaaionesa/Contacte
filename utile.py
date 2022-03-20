def identify(l,f):
    a=[]
    for i in range (0,len(l)):
        if f(l[i]):
            a.append(l[i])
    return a