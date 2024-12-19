list=[]
t=1
while(t):
    n=(input("ENter name:"))
    list.append(n)
    t=int(input("do u want to add more numbers 0?1: "))
t=tuple(list)
s=input("enter name to search: ")
flag=0
for i in t:
    if s==i:
        print("name found")
        flag=1
if(flag==0):
    print("name not found")