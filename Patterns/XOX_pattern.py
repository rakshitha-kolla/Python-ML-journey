n=int(input("Enter number of rows: "))
for i in range(n):
    for j in range((n//2)+1):
        if (i%2)==0:
            print("X",end=" ")
            print("O",end=" ")
        else:
            print("O",end=" ")
            print("X",end=" ")
    print()
