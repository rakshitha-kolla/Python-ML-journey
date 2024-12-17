n=int(input("enter num of rows: "))
for i in range(n):
    for j in range(i,-1,-1):
        print(2**j,end=" ")
    print()