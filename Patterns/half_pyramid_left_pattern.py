n=int(input("Enter number of rows: "))
for i in range(n):
    print(2*(n-i-1)*" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n-2,-1,-1):
    print(2*(n-i-1)*" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()