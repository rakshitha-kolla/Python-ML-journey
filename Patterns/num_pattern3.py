'''
1
3 2
6 5 4
10 9 8 7
'''
n=int(input("enter num of rows: "))
c=0
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(c+j,end=" ")
    c+=i
    print()