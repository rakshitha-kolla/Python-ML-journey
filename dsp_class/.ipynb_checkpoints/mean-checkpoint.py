def mean(list):
    sum=0
    m=0
    n=len(list)
    print(n)
    for i in list:
        sum+=i
    print(sum)
    mean=sum/n
    return mean
list=[]
t=1
while(t):
    n=float(input("enter num: "))
    list.append(n)
    t=int(input("enter 0/1:"))
m=mean(list)
print(m)