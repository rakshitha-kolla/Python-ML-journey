n=int(input("Enter num of rows: "))
for i in range(n):
    print((n-i)*"  ",end="")
    for j in range(2*i+1):
        print("*",end=" ")
    print()