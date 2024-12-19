for i in range(1,101):
    x=2
    for x in range(2,i):
        if(i%x==0):
           break
        else:
            x+=1
    if(x==i):
        print(x)
    i+=1