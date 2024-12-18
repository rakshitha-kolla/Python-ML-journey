n=int(input("enter n: "))
for i in range(n-1,-1,-1):
    print((n-i)*" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()