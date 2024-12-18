def fact(c):
    if c==0 or c==1:
        return 1
    return c*fact(c-1)
n=int(input("enter num of rows: "))
for i in range(n):
    for k in range(n-1-i):
        print("  ",end="")
    for j in range(i+1):
        c=int(fact(i)/(fact(i-j)*fact(j)))
        print(c,end="   ")
    print("\n")


#Method 2
n1=int(input("Enter n: "))
for i in range(1,n+1):
    for k in range(n-i+1):
        print("  ",end="")
    c=1
    for j in range(1,i+1):
        print(c,end="   ")
        c=c*(i-j)//j
    print()