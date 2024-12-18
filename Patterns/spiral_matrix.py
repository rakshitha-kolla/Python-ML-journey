'''
1.
given n as the size of matrix the task is to print a spiral pattern in 2d array of size n
 1  2  3  4  5
 16 17 18 19 6
 15 24 25 20 7
 14 23 22 21 8
 13 12 11 10 9
'''
import numpy as np
n=int(input("enter matrix size: "))
m=np.full((n,n),0)
top=0
bottom=n-1
left=0
right=n-1
c=1
while top<=bottom and left<=right:
    #left to right
    l=left
    while(l<=right):
        m[top][l]=c
        c+=1
        l+=1
    top+=1
    #top to bottom
    t=top
    while(t<=bottom):
        m[t][right]=c
        c+=1
        t+=1
    right-=1
    #right to left
    r=right
    while(r>=left):
        m[bottom][r]=c
        c+=1
        r-=1
    bottom-=1
    #bottom to top
    b=bottom
    while(b>=top):
        m[b][left]=c
        c+=1
        b-=1
    left+=1

print(m)