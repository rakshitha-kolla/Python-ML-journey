'''given a n,n matrix print spiral pattern from given matrix
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
'''
import numpy as np
def print_spiral(m):
    if m.all()==0 :
        return
    r,c=m.shape
    top=0
    bottom=r-1
    left=0
    right=c-1
    while(top<=bottom and left<=right):
        #left to right
        l=left
        while(l<=right):
            print(m[top][l],end=" ")
            l+=1
        top+=1
        #top to bottom
        t=top
        while(t<=bottom):
            print(m[t][right],end=" ")
            t+=1
        right-=1
        #right to left
        r=right
        while(r>=left):
            print(m[bottom][r],end=" ")
            r-=1
        bottom-=1
        #bottom to top
        b=bottom
        while(b>=top):
            print(m[b][left],end=" ")
            b-=1
        left+=1



if __name__=="__main__":
    m=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    print(m)
    print_spiral(m)