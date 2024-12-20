m=int(input("Enter m: "))
n=int(input("Enter n: "))
for i in range(m):
    for j in range(n):
        if i==m-1:
            print("*",end=" ")
        elif j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()