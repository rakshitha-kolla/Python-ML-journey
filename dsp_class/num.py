
list=[]
t=1
while(t):
    n=int(input("ENter num:"))
    list.append(n)
    t=int(input("do u want to add more numbers 0?1: "))
num=int(input("eneter the num u want to search:"))
flag=0
for i in list:
    if num==i:
        print("index of ",num," is ",list.index(i))
        flag=1
        break
if(flag==0):
    print("num not found")

