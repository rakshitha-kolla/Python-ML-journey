d={}
t=1
while(t):
    n=(input("ENter emp name:"))
    s=int(input("ENter emp salary:"))
    d.update({n:s})
    t=int(input("do u want to add more numbers 0?1: "))
print(d)