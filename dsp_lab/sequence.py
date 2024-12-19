n=int(input("enter n: "))
for i in range(5,n+1,5):
    if(i % 10 == 0):
        print(i,end=" ")
    else:
        print(-i,end=" ")
    