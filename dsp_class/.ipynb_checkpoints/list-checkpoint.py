list=[]
t=1
while(t):
    n=int(input("ENter num:"))
    list.append(n)
    t=int(input("do u want to add more numbers 0?1: "))
pos=[]
neg=[]
for i in list:
    if(i>=0):
        pos.append(i)
    else:
        neg.append(i)
print(list,pos,neg)