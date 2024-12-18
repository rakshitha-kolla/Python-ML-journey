n=int(input("enter num of rows: "))
ch=65
for i in range(1,n+1):
    print(2*(n-i)*" ",end="")
    for j in range(i-1,-1,-1):
        print(chr(ch+j),end=" ")
    print()
    ch+=i