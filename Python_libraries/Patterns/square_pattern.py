n=int(input("Enter num of rows and cols: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
print("\n")
for i in range(n):
    for j in range(n):
        print("$",end=" ")
    print()