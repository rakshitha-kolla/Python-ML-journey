n=int(input("Enter num of rows: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print(4*(n-i-1)*" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n-1,-1,-1):
    for j in range(i):
        print("*",end=" ")
    print(4*(n-i)*" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()