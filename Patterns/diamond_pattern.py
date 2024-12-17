n=int(input("Enter number of rows: "))
for i in range(n-1):
    print((n-i-1)*"  ",end="")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(n-1,-1,-1):
    print((n-i-1)*"  ",end="")
    for j in range(2*i+1):
        print("*",end=" ")
    print()