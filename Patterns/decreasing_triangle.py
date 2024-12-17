n=int(input("Enter num of rows: "))
i=0
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
