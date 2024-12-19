d={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
num=int(input("enter num: "))
temp=num
str=""
while(temp):
    r=temp%10
    str=d[r]+" "+str
    temp=temp//10
print(str)