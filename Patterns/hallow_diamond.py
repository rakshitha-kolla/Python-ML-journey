n=int(input("Enter num of rows: "))
for i in range(n):
    print((n-i)*" ",end="")
    for j in range(i+1):
        if j==i or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n-2,-1,-1):
    print((n-i)*" ",end="")
    for j in range(i+1):
        if j==0 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()