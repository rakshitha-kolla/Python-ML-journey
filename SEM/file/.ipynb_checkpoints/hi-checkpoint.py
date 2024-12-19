a=open("hi.txt","w")
while(1):
    str=input("enter line: ")
    a.writelines(str+"\n")
    n=int(input("do u want to continue: "))
    if(n==0):
        break
a.close()