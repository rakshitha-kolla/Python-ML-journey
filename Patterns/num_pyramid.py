n=int(input("Enter n: "))
for i in range(n):
    print((n-i)*"  ",end="")
    for j in range(1,i+2):
        print(j,end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()