num=int(input("enter num: "))
i=1
print("factors of ",num,"are: ")
while(i<=num):
    if(num%i==0):
        print(i,end=" ")
    i+=1