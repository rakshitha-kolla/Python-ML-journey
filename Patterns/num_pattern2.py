'''
1
1 2 1
1 2 4 2 1
1 2 4 8 4 2 1
1 2 4 8 16 8 4 2 1
1 2 4 8 16 32 16 8 4 2 1
1 2 4 8 16 32 64 32 16 8 4 2 1
1 2 4 8 16 32 64 128 64 32 16 8 4 2 1
'''
n=int(input("enter num of rows: "))
for i in range(1,n+1):
    for j in range((2*i)//2):
        print(2**j,end=" ")
    for j in range(((2*i)//2)-2,-1,-1):
        print(2**j,end=" ")
    print()