n=int(input("Enter num of rows: "))
for i in range(n):
    print((n-i)*" ",end="")
    for j in range(i+1):
        if i==n-1:
            print("*",end=" ")
        elif j==i or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()