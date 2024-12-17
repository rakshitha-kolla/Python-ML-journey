n=int(input("Enter num of rows: "))
for i in range(1,n+1):
    print((n-i+1)*" ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()