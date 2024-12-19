a=int(input("enter a= "))
b=int(input("enter b= "))
print("ENTER YOUR CHOICE a.\"+\" b.\"-\"  c.\"*\"  d.\"\\\" : ")
c=input()
if(c=="a"):
    print("sum= ",a+b)
elif(c=="b"):
    print("diff= ",a-b)
elif(c=="c"):
    print("multiplication= ",a*b)
else:
    print("division= ",a/b)