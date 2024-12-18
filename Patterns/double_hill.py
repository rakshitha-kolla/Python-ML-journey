n=int(input("enter number of rows: "))
for i in range(n):
    print((n-i)*"  ",end="")
    for j in range(2*i+1):
        print("*",end=" ")
    print(2*(n-i-1)*"  ",end="")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
